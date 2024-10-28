from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView, LogoutView, redirect_to_login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
from .models import Candidate
from .forms import CandidateForm, CandidateSearchForm
from django.db.models import Count
from django.http import HttpResponseForbidden, HttpResponseRedirect

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_staff

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            return redirect_to_login(
                self.request.get_full_path(),
                self.get_login_url(),
                self.get_redirect_field_name()
            )
        return redirect(self.get_login_url())

class AdminLoginView(LoginView):
    template_name = 'candidates/login.html'
    
    def get_success_url(self):
        next_url = self.request.GET.get('next')
        if next_url:
            return next_url
        return reverse_lazy('candidates:dashboard')
    
    def form_valid(self, form):
        user = form.get_user()
        if not user.is_staff:
            messages.error(self.request, "Access denied. Admin privileges required.")
            return self.form_invalid(form)
        return super().form_valid(form)

class AdminLogoutView(LogoutView):
    next_page = reverse_lazy('candidates:login')

class CandidateListView(LoginRequiredMixin,ListView):
    model = Candidate
    template_name = 'candidates/candidate_list.html'
    context_object_name = 'candidates'
    login_url = reverse_lazy('candidates:login')

    def get_queryset(self):
        form = CandidateSearchForm(self.request.GET)
        form.is_valid()
        search = form.cleaned_data.get('search')
        start_date = form.cleaned_data.get('start_date')
        end_date = form.cleaned_data.get('end_date')
        
        candidates = Candidate.objects.all()
        if search:
            candidates = candidates.filter(first_name__icontains=search) | candidates.filter(last_name__icontains=search) | candidates.filter(email__icontains=search)
        if start_date:
            candidates = candidates.filter(date_of_birth__gte=start_date)
        if end_date:
            candidates = candidates.filter(date_of_birth__lte=end_date)
    
        return candidates

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CandidateSearchForm(self.request.GET)
        return context

class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'candidates/candidate_detail.html'
    context_object_name = 'candidate'

    def dispatch(self, request, *args, **kwargs):
        referer = request.META.get('HTTP_REFERER')
        success_url = self.request.build_absolute_uri(reverse_lazy('candidates:candidate_success', kwargs={'pk': self.get_object().pk}))
        dashboard_url = self.request.build_absolute_uri(reverse_lazy('candidates:dashboard'))
        
        if referer not in [success_url, dashboard_url]:
            return HttpResponseForbidden("You are not allowed to access this page directly.")
        
        return super().dispatch(request, *args, **kwargs)

class CandidateCreateView(CreateView):
    model = Candidate
    form_class = CandidateForm
    template_name = 'candidates/candidate_form.html'

    def get_success_url(self):
        return reverse_lazy('candidates:candidate_success', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.resume = self.request.FILES.get('resume')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error submitting your application.')
        return super().form_invalid(form)

class CandidateUpdateView(UpdateView):
    model = Candidate
    form_class = CandidateForm
    template_name = 'candidates/candidate_form.html'

    def get_success_url(self):
        return reverse_lazy('candidates:candidate_success', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.resume = self.request.FILES.get('resume')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error updating your application.')
        return super().form_invalid(form)

class CandidateDeleteView(DeleteView):
    model = Candidate
    template_name = 'candidates/candidate_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Application deleted successfully.')
        return super().delete(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['candidate'] = self.get_object()
        return context
    
    def get_success_url(self):
        return_to_list = self.request.GET.get('return_to_list')
        if return_to_list:
            return reverse_lazy('candidates:candidate_list')
        return reverse_lazy('candidates:candidate_create')
    
class DashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'candidates/dashboard.html'
    login_url = reverse_lazy('candidates:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_candidates'] = Candidate.objects.count()
        context['recent_candidates'] = Candidate.objects.order_by('-id')[:5]
        
        position_stats = Candidate.objects.exclude(position='').values('position').annotate(
            count=Count('position')).order_by('-count')[:5]
        context['position_stats'] = position_stats
        
        degree_stats = Candidate.objects.exclude(degree='').values('degree').annotate(
            count=Count('degree')).order_by('-count')[:5]
        context['degree_stats'] = degree_stats
        
        return context
    
    def test_func(self):
        return self.request.user.is_staff  # Ensure the user is an admin

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, 'You do not have permission to view this page.')
            return self.render_to_response({'error': 'You do not have permission to view this page.'})
        else:
            return super().handle_no_permission()

class CandidateSuccessView(TemplateView):
    template_name = 'candidates/candidate_success.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        candidate = get_object_or_404(Candidate, pk=pk)
        context['candidate'] = candidate
        return context