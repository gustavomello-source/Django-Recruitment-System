# Sistema de recrutamento
<!-- TABLE OF CONTENTS -->

Sistema de gerenciamento e cadastro de candidatos, desenvolvido com Django, o qual permite que o candidato realize todas as funções CRUD e auxilia o usuário administrador a visualizar e gerenciar os dados.

## Tabela de Conteúdo

- [Sistema de recrutamento](#sistema-de-recrutamento)
  - [Tabela de Conteúdo](#tabela-de-conteúdo)
  - [Sobre o Projeto](#sobre-o-projeto)
    - [Feito Com](#feito-com)
  - [Começando](#começando)
    - [Pré-requisitos](#pré-requisitos)
    - [Estrutura de Arquivos](#estrutura-de-arquivos)
    - [Instalação e Preparação de ambiente](#instalação-e-preparação-de-ambiente)
  - [Executando a aplicação](#executando-a-aplicação)
    - [CRUD do candidato](#crud-do-candidato)
    - [Funções de administrador](#funções-de-administrador)
  - [Edição](#edição)

<!-- ABOUT THE PROJECT -->

## Sobre o Projeto

Este repositório organiza os dados necessários para utilização da aplicação web responsável por hospedar e exibir as funcionalidades do sistema de recrutamento.

O projeto possui modelo de banco de dados o qual armazena informações dos candidatos, os quais podem realizar todas as operações CRUD em seus próprios dados. A aplicação valida certos formatos de dados, como por exemplo a necessidade de um e-mail encerrar em '@exemplo.com'

Usuários administradores podem realizar um login para acessar informações de todos os candidatos e gerenciá-las.

### Feito Com

Lista das principais tecnologias e ferramentas utilizadas no desenvolvimento do projeto:

- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - A linguagem de marcação padrão para criar páginas web. É usada para estruturar o conteúdo na web e funciona em conjunto com CSS e JavaScript para criar sites visualmente atraentes e interativos.
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) - Linguagem de programação de alto nível conhecida por sua versatilidade e uso no desenvolvimento web. Utilizada para criar páginas web interativas e aplicações do lado do servidor.
- [Python](https://www.python.org/) - Linguagem de programação de alto nível conhecida por sua simplicidade e legibilidade. É amplamente utilizada para desenvolvimento web, automação, análise de dados, e aprendizado de máquina.
- [Django](https://www.djangoproject.com/) - Um framework web de alto nível e gratuito para Python, que promove o desenvolvimento rápido e o design limpo e pragmático. É amplamente utilizado para construir aplicações web e oferece uma estrutura completa com ORM, autenticação, e administração automática.
- [Bootstrap](https://getbootstrap.com/) - Um framework de front-end open source que facilita a criação de sites responsivos e com design moderno. Ele fornece uma coleção de componentes pré-estilizados em HTML, CSS e JavaScript, permitindo o desenvolvimento rápido e eficiente de interfaces de usuário.

<!-- GETTING STARTED -->

## Começando

Para começar a utilizar este projeto, é necessário ter alguns pré-requisitos de ambiente.

### Pré-requisitos

1. A utilização do ambiente requer a instalação do Python 3.12. Outras bibliotecas Python são necessárias para o funcionamento correto e estão descritas no arquivo requirements.txt
2. A documentação das principais bibliotecas e tecnologias aqui utilizadas pode ser encontrada nos links fornecidos em [Feito Com](#feito-com)
3. É necessário que seja seguida a estrutura de arquivos descrita em [Estrutura de Arquivos](#estrutura-de-arquivos) para o funcionamento dos códigos.

### Estrutura de Arquivos

A estrutura de arquivos deve estar disposta da seguinte maneira no momento de instalação:

```bash
Django-Recruitment-System
├── recruitment_project
│   ├── candidates
│   │   ├── templates
│   │   │   └── candidates
│   │   │   │   ├── candidate_confirm_delete.html
│   │   │   │   ├── candidate_detail.html
│   │   │   │   ├── candidate_form.html
│   │   │   │   ├── candidate_list.html
│   │   │   │   ├── candidate_success.html
│   │   │   │   ├── dashboard.html
│   │   │   │   ├── login.html
│   │   │   │   └── logout.html
│   │   ├── templatetags
│   │   │   ├── __init__.py
│   │   │   └── form_tags.py
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └──views.py
│   ├── media
│   │   └── resumes
│   ├── recruitment_project
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── templates
│   │   └── base.html
│   └── manage.py
├── .gitattributes
├── LICENSE
├── readme.md
└── requirements.txt
```

Serão explicados os principais arquivos e diretórios na seção de [Edição](#edição).

### Instalação e Preparação de ambiente
1. Para instalar e utilizar esse projeto, basta clonar o projeto. [Documentação github](https://docs.github.com/en). 

- Exemplo da realização de clone de um repositório:
```
git clone https://endereco.do.projeto/pasta-principal.git
```
Onde o endereco.do.projeto representa o endereço do repositório e pasta-principal.git representa o arquivo .git principal do repositório.

2. Após o clone do projeto, abra um terminal na pasta raiz do projeto e acesse o diretório "recruitment_project". 

```
$ cd recruitment_project
```

3. Crie e ative a sua virtualenv utilizando os comandos:

- **Para sistemas Unix (Linux/macOS):**
```
virtualenv -p python3 .venv
. .venv/bin/activate
```
- **Para Windows:**
```
python -m venv .venv
.venv\Scripts\activate
```

Para mais detalhes sobre como utilizar o virtualenv, acesse este [link](https://virtualenv.pypa.io/en/latest/)

4. Instale as dependências
```
(.venv) ....$ pip3 install -r ../requirements.txt
```

5. Faça as migrações necessárias do banco de dados da aplicação
```
python manage.py makemigrations candidates
python manage.py migrate
```

6. Crie o superusuário para administradores
- Exemplo
```
python manage.py createsuperuser

Username: admin
Email address: admin@admin.com
Password: admin
```

## Executando a aplicação
Para executar a aplicação e iniciar o gerenciamento ou cadastramento, as seguintes etapas devem ser seguidas, após o ambiente virtual e as etapas em [Instalação e Preparação de ambiente](#instalação-e-preparação-de-ambiente):

1. Execute o arquivo manage.py para rodar o servidor:
```
(.venv) ....$ python manage.py runserver
```

2. Abra o endereço impresso no terminal, após execução, utilizando o navegador web do sistema. Exemplo:
```
Running on http://127.0.0.1:8000
```

### CRUD do candidato
Partindo da execução correta do arquivo manage.py e abrindo o endereço em um navegador web, o usuário encontra a página de login da aplicação. No caso do candidato, ele pode pressionar o botão "I am a Candidate", o qual o redirecionará para o formulário que deve ser preenchido corretamente.

Quando completo o formulário, o usuário pode submeter as informações, o que fará com que ele seja redirecionado para uma página que exibe seus detalhes e uma mensagem de sucesso na criação de sua página de candidato. Nessa página, o usuário pode pressionar o botão "Edit Candidate" ou "Delete Candidate".

Caso o botão edit seja pressionado, o usuário retorna para a página de formulário, no qual ele pode suas informações de cadastro e submeter novamente.

No caso do botão de deletar candidato, a página o redireciona para uma página de confirmação deleção e, caso o usuário confirme-a, o cadastro é removido do sistema e ele é novamente redirecionado para a página de formulário. Se a deleção for cancelada, o usuário retorna para a página de detalhes.

### Funções de administrador
Na página de login, o usuário pode introduzir um usuário de senha, assim sendo capaz de ser autenticado como administrador na aplicação.

Uma vez autenticado como administrador, o usuário tem acesso a uma página de 'dashboard', a qual exibe qual é o número total de candidatos atualmente cadastrados e uma lista de candidatos recentes.

Nesta mesma página, o administrador pode clicar em um dos nomes de candidatos recentes para abrir detalhes ou clicar no botão "Candidates", o qual agrupa todos os detalhes de todos os candidatos em uma única página e permite também que o administrador delete qualquer cadastro feito com o botão "Delete Candidate", observe os detalhes e acesse o arquivo de currículo enviado pelo candidato no momento de cadastro.

Caso ele clique no botão "Delete Candidate", ele é enviado para a tela de confirmação de deleção. Se for confirmada, o cadastro do candidato é deletado do sistema e o administrador retorna para a lista de candidatos, e se ela for cancelada, o administrador apenas retorna para a mesma página de lista.

Por fim, o administrador pode realizar o logout, assim saindo de sua conta na aplicação e perdendo autenticação.

## Edição
Esta seção descreve brevemente os principais diretórios e arquivos criados.

- **candidates**: Diretório relativo ao app do django chamado candidates. Nele, todo o padrão de pastas e arquivos de aplicações Django é aplicado, assim possuindo as pastas e arquivos:

  -  **templates**: Pasta que armazena as páginas .html utilizadas na aplicação
  
  -  **views.py, urls.py, forms.py**: Alguns dos arquivos Django que gerenciam o funcionamento das páginas.

-  **media/resumes**: Diretório no qual os arquivos de currículos enviados pelos candidatos são armazenados. 

- **recruitment_project**: Diretório com o mesmo nome que o projeto principal, o qual carrega scripts importantes do Django, como:

  -  **settings**: Arquivo de configurações de toda a aplicação Django.
  
  -  **urls.py**: Arquivo que armazena e gerencia urls das páginas para operações, como de redirecionamento.

-  **templates**: Pasta que armazena o arquivo **base.html**.

-  **manage.py**: Script principal do Django.

- **README.md**: Este arquivo contém informações sobre o sistema, como instalá-lo e usá-lo.

- **requirements.txt**: Este arquivo contém uma lista de pacotes Python necessários para executar o sistema.