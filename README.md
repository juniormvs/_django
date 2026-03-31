# 🎸 Django Studies — _django
 
> Repositório de estudos práticos com o framework Django, construído do zero com foco em aprender os fundamentos reais do desenvolvimento web com Python.
 
---
 
## 🧠 O que está sendo estudado
 
Este repositório documenta minha jornada de aprendizado com Django, abordando desde a estrutura básica de projetos até conceitos intermediários de templates, herança e renderização de views.
 
---
 
## 📁 Estrutura do Projeto
 
```
_django/
│
├── projeto_01/              # Projeto principal de estudos
│   ├── base/                # App base/global da aplicação
│   ├── blog/                # App do blog
│   ├── home/                # App da página inicial
│   ├── manage.py            # CLI do Django
│   └── db.sqlite3           # Banco de dados local (SQLite)
│
└── .codex                   # Anotações e referências pessoais de estudo
```
 
---
 
## 📚 Conteúdo Abordado
 
### ✅ Fundamentos
- Criação de projetos e apps com `django-admin` e `manage.py startapp`
- Renderização de HTML com `render()` e `HttpResponse`
 
### ✅ Templates
- Configuração de templates globais com `DIRS` no `settings.py`
- Herança de templates com `{% extends %}` e `{% block %}`
- Organização com **partials** usando `{% include %}`
 
### ✅ Estrutura de Apps
- Separação de responsabilidades: `home`, `blog`, `base`
- Templates globais compartilhados entre múltiplos apps
 
---
 
## 🚀 Como rodar localmente
 
### Pré-requisitos
- Python 3.10+
- pip
 
### Passos
 
```bash
# Clone o repositório
git clone https://github.com/juniormvs/_django.git
cd _django
 
# Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
 
# Instale as dependências
pip install django
 
# Acesse o projeto principal
cd projeto_01
 
# Rode as migrações
python manage.py migrate
 
# Inicie o servidor de desenvolvimento
python manage.py runserver
```
 
Acesse em: [http://localhost:8000](http://localhost:8000)
 
---
 
## 🛠️ Stack
 
| Tecnologia | Uso |
|------------|-----|
| Python 3.x | Linguagem principal |
| Django | Framework web |
| SQLite | Banco de dados (dev) |
| HTML/DTL | Templates com Django Template Language |
 
---
 
## 🧭 Roadmap de Estudos
 
- [x] Criar projeto e apps com `manage.py`
- [x] Renderizar HTML com views
- [x] Templates globais com `DIRS`
- [x] Herança de templates com `extends`
- [x] Partials com `include`
- [ ] Models e ORM do Django
- [ ] Forms e validação
- [ ] Class-Based Views (CBVs)
- [ ] Autenticação de usuários
- [ ] Django REST Framework (DRF)
- [ ] Deploy em produção
 
---
 
## 👤 Autor
 
**Mário Jr.**  
Desenvolvedor em transição para Python, Data Engineering e IA Generativa.
 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/juniormvs)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/juniormvs)
 
---
 
## 📄 Licença
 
Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
 
---
 
> *"Construindo consistentemente, um curso por vez. 🚀"*
