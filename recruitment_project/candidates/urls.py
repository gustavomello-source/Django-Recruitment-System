from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name = 'candidates' # namespace

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('', views.AdminLoginView.as_view(), name='login'),
    path('login/', views.AdminLoginView.as_view(), name='login'),
    path('logout/', views.AdminLogoutView.as_view(next_page='candidates:login'), name='logout'),
    path('list/', views.CandidateListView.as_view(), name='candidate_list'),
    path('detail/<int:pk>/', views.CandidateDetailView.as_view(), name='candidate_detail'),
    path('create/', views.CandidateCreateView.as_view(), name='candidate_create'),
    path('update/<int:pk>/', views.CandidateUpdateView.as_view(), name='candidate_update'),
    path('delete/<int:pk>/', views.CandidateDeleteView.as_view(), name='candidate_delete'),
    path('success/<int:pk>/', views.CandidateSuccessView.as_view(), name='candidate_success'),
]