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
├── base/                    # App base/global — templates e partials globais
├── blog/                    # App do blog
├── home/                    # App da página inicial
│
├── projeto_01/              # Configurações centrais do projeto Django
│   ├── settings.py          # Configuração de DIRS, apps instalados, etc.
│   ├── urls.py              # Roteamento principal
│   └── wsgi.py / asgi.py
│
├── manage.py                # CLI do Django
├── db.sqlite3               # Banco de dados local (SQLite)
├── .codex                   # Anotações e referências pessoais de estudo
└── .gitignore
```

---

## 📚 Conteúdo Abordado

### ✅ Fundamentos
- Criação de projetos com `django-admin startproject`
- Criação de apps com `manage.py startapp`
- Renderização de HTML com `render()` e `HttpResponse`
- Configuração de URLs com `path()` e `include()`

### ✅ Templates
- Configuração de templates globais com `DIRS` no `settings.py`
- Herança de templates com `{% extends %}` e `{% block %}`
- Organização com **partials** usando `{% include %}`
- Separação de layouts reutilizáveis (header, footer, nav)

### ✅ Estrutura de Apps
- Separação de responsabilidades: `home`, `blog`, `base`
- Templates globais compartilhados entre múltiplos apps
- Organização de arquivos estáticos por app

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

# Rode as migrações
python manage.py migrate

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

## 🛠️ Stack

| Tecnologia | Uso | % no repo |
|------------|-----|-----------|
| Python | Linguagem principal / views / config | 92.1% |
| HTML/DTL | Templates com Django Template Language | 4.8% |
| CSS | Estilização dos templates | 3.1% |
| SQLite | Banco de dados (ambiente de dev) | — |

---

## 🧭 Roadmap de Estudos

- [x] Criar projeto e apps com `manage.py`
- [x] Renderizar HTML com views (`render`, `HttpResponse`)
- [x] Templates globais com `DIRS`
- [x] Herança de templates com `{% extends %}` e `{% block %}`
- [x] Partials com `{% include %}`
- [ ] Models e ORM do Django
- [ ] QuerySets e relacionamentos entre models
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
