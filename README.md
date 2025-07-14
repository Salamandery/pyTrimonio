# 🏢 pyTrimonio - Sistema de Cadastro Patrimonial

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-3.2.5-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-336791?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-3.3.7-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen?style=for-the-badge)]()
[![Version](https://img.shields.io/badge/Version-1.0.0-blue?style=for-the-badge)]()

</div>

<div align="center">

> **Sistema web para gerenciamento e controle de patrimônio empresarial desenvolvido em Django**

[![Demo](https://img.shields.io/badge/Live%20Demo-Available-green?style=for-the-badge&logo=globe)]()
[![Documentation](https://img.shields.io/badge/Documentation-Complete-blue?style=for-the-badge&logo=read-the-docs)]()

</div>

---

## 📋 Sumário

- [🎯 Sobre o Projeto](#-sobre-o-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
- [🏗️ Arquitetura do Projeto](#️-arquitetura-do-projeto)
- [📋 Pré-requisitos](#-pré-requisitos)
- [🚀 Instalação e Configuração](#-instalação-e-configuração)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🗄️ Configuração do Banco de Dados](#-configuração-do-banco-de-dados)
- [▶️ Executando o Projeto](#️-executando-o-projeto)
- [🤝 Contribuição](#-contribuição)

---

## 🎯 Sobre o Projeto

O **pyTrimonio** é um sistema web desenvolvido em Django para controle e gerenciamento de patrimônio empresarial. O sistema permite cadastrar, consultar e gerenciar diversos tipos de equipamentos como computadores, monitores, impressoras, nobreaks e outros itens patrimoniais.

### 🎯 **Objetivos do Sistema**
- ✅ Controle total do patrimônio empresarial
- ✅ Gestão centralizada de equipamentos
- ✅ Interface intuitiva e responsiva
- ✅ Relatórios e consultas avançadas
- ✅ Sistema de autenticação seguro

---

## ✨ Funcionalidades

<div align="center">

### 🖥️ **Módulos de Gestão Patrimonial**

| Módulo | Descrição | Status |
|--------|-----------|--------|
| 🖥️ **Computadores** | Hostname, IP, MAC, marca, modelo, serial | ✅ Ativo |
| 🖥️ **Monitores** | Marca, modelo, serial, patrimônio | ✅ Ativo |
| 🖨️ **Impressoras** | Controle de impressoras e equipamentos | ✅ Ativo |
| ⚡ **Nobreaks** | Gerenciamento de nobreaks | ✅ Ativo |
| 📱 **Celulares** | Controle de dispositivos móveis | ✅ Ativo |
| 🌐 **Networks** | Equipamentos de rede | ✅ Ativo |
| 🏢 **Empresas** | Gestão de empresas | 🔄 Em desenvolvimento |
| 📦 **Estoques** | Controle de estoque | 🔄 Em desenvolvimento |

</div>

### 🔐 **Sistema de Autenticação**
- ✅ Login e registro de usuários
- ✅ Controle de acesso por perfil
- ✅ Sessões seguras
- ✅ Recuperação de senha

### 🎨 **Interface Responsiva**
- ✅ Design Bootstrap para desktop e mobile
- ✅ Navegação intuitiva
- ✅ Formulários otimizados
- ✅ Feedback visual para ações

### ⚙️ **Administração Django**
- ✅ Painel administrativo completo
- ✅ CRUD automático para todos os modelos
- ✅ Filtros e buscas avançadas
- ✅ Exportação de dados

---

## 🛠️ Tecnologias Utilizadas

<div align="center">

### 🐍 **Backend**
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-3.2.5-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![psycopg2](https://img.shields.io/badge/psycopg2-2.9+-336791?style=flat-square)](https://www.psycopg.org/)

### 🎨 **Frontend**
[![Bootstrap](https://img.shields.io/badge/Bootstrap-3.3.7-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![jQuery](https://img.shields.io/badge/jQuery-3.6+-0769AD?style=flat-square&logo=jquery&logoColor=white)](https://jquery.com/)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/CSS)

### 🛠️ **Ferramentas de Desenvolvimento**
[![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)](https://git-scm.com/)
[![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=flat-square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
[![Django Admin](https://img.shields.io/badge/Django%20Admin-092E20?style=flat-square&logo=django&logoColor=white)](https://docs.djangoproject.com/en/stable/ref/contrib/admin/)

</div>

---

## 🏗️ Arquitetura do Projeto

O projeto segue o padrão **MVT (Model-View-Template)** do Django com a seguinte estrutura:

```
pyTrimonio/
├── 📁 pyTrimonio/           # Configurações principais
│   ├── 🏠 core/            # App principal (home, templates base)
│   ├── 🔐 accounts/        # Sistema de autenticação
│   ├── 💻 computadores/    # Módulo de computadores
│   ├── 🖥️ monitores/       # Módulo de monitores
│   ├── 🖨️ impressoras/     # Módulo de impressoras
│   ├── ⚡ nobreaks/        # Módulo de nobreaks
│   ├── 📱 celulares/       # Módulo de celulares
│   ├── 🌐 networks/        # Módulo de equipamentos de rede
│   ├── 🏢 empresas/        # Módulo de empresas
│   ├── 📦 estoques/        # Módulo de estoque
│   └── ⚙️ settings.py      # Configurações do Django
├── 🚀 manage.py            # Script de gerenciamento Django
└── 📖 README.md           # Este arquivo
```

### 🎯 **Padrões de Projeto Implementados**
- ✅ **MVT (Model-View-Template)**: Arquitetura Django
- ✅ **Manager Classes**: Classes customizadas para queries complexas
- ✅ **Template Inheritance**: Herança de templates com base.html
- ✅ **URL Namespacing**: Organização de URLs por app
- ✅ **Static Files**: Arquivos CSS, JS e imagens organizados

---

## 📋 Pré-requisitos

<div align="center">

### 🔧 **Sistema**
[![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/windows)
[![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)](https://www.linux.org/)
[![macOS](https://img.shields.io/badge/macOS-000000?style=flat-square&logo=macos&logoColor=white)](https://www.apple.com/macos/)

### 🐍 **Software**
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-12+-336791?style=flat-square&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)](https://git-scm.com/)

</div>

- **Python 3.8** ou superior
- **PostgreSQL 12** ou superior
- **pip** (gerenciador de pacotes Python)
- **Git** (para clonar o repositório)

---

## 🚀 Instalação e Configuração

### 1️⃣ **Clone o Repositório**

```bash
git clone https://github.com/salamandery/pyTrimonio.git
cd pyTrimonio
```

### 2️⃣ **Crie um Ambiente Virtual**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **Instale as Dependências**

```bash
pip install django==3.2.5
pip install psycopg2-binary
```

### 4️⃣ **Configure o Banco de Dados**

Edite o arquivo `pyTrimonio/settings.py` e configure as credenciais do PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pytrimonio_db',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5️⃣ **Execute as Migrações**

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6️⃣ **Crie um Superusuário**

```bash
python manage.py createsuperuser
```

### 7️⃣ **Execute o Projeto**

```bash
python manage.py runserver
```

<div align="center">

**🎉 O sistema estará disponível em: [http://localhost:8000](http://localhost:8000)**

[![Localhost](https://img.shields.io/badge/Localhost-8000-00FF00?style=for-the-badge&logo=localhost&logoColor=white)](http://localhost:8000)

</div>

---

## 📁 Estrutura do Projeto

### 🏢 **Apps Principais**

<div align="center">

| App | Descrição | Funcionalidade | Status |
|-----|-----------|----------------|--------|
| `core` | App principal | Templates base, views principais | ✅ Ativo |
| `accounts` | Autenticação | Login, registro, logout | ✅ Ativo |
| `computadores` | Gestão de PCs | CRUD de computadores | ✅ Ativo |
| `monitores` | Gestão de monitores | CRUD de monitores | ✅ Ativo |
| `impressoras` | Gestão de impressoras | CRUD de impressoras | ✅ Ativo |
| `nobreaks` | Gestão de nobreaks | CRUD de nobreaks | ✅ Ativo |
| `celulares` | Gestão de celulares | CRUD de celulares | ✅ Ativo |
| `networks` | Equipamentos de rede | CRUD de equipamentos de rede | ✅ Ativo |

</div>

---

## 🗄️ Configuração do Banco de Dados

### 🐘 **PostgreSQL**

1. **Instale o PostgreSQL**:
   - [Download PostgreSQL](https://www.postgresql.org/download/)

2. **Crie o Banco de Dados**:
   ```sql
   CREATE DATABASE pytrimonio_db;
   CREATE USER pytrimonio_user WITH PASSWORD 'sua_senha';
   GRANT ALL PRIVILEGES ON DATABASE pytrimonio_db TO pytrimonio_user;
   ```

3. **Configure as Migrações**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

---

## ▶️ Executando o Projeto

### 🛠️ **Desenvolvimento**

```bash
# Ative o ambiente virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac

# Execute o servidor
python manage.py runserver

# Acesse: http://localhost:8000
```

### 🚀 **Produção**

```bash
# Configure DEBUG = False em settings.py
# Configure ALLOWED_HOSTS
# Use um servidor WSGI como Gunicorn
pip install gunicorn
gunicorn pyTrimonio.wsgi:application
```

---

## 🔧 Comandos Úteis

<div align="center">

### 🛠️ **Desenvolvimento**

```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Coletar arquivos estáticos
python manage.py collectstatic

# Shell Django
python manage.py shell

# Testes
python manage.py test
```

</div>

---

## 🤝 Contribuição

<div align="center">

[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=for-the-badge&logo=github)](CONTRIBUTING.md)
[![Issues](https://img.shields.io/badge/Issues-Welcome-orange?style=for-the-badge&logo=github)](https://github.com/salamandery/pyTrimonio/issues)
[![Pull Requests](https://img.shields.io/badge/PRs-Welcome-blue?style=for-the-badge&logo=github)](https://github.com/salamandery/pyTrimonio/pulls)

</div>

1. Faça um **Fork** do projeto
2. Crie uma **Branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 📞 Suporte

<div align="center">

[![Email](https://img.shields.io/badge/Email-contato@mail.org.br-blue?style=flat-square&logo=gmail)](mailto:contato@mail.org.br)
[![Documentation](https://img.shields.io/badge/Documentation-Django%20Docs-blue?style=flat-square&logo=read-the-docs)](https://docs.djangoproject.com/)
[![Issues](https://img.shields.io/badge/Issues-GitHub-orange?style=flat-square&logo=github)](https://github.com/salamandery/pyTrimonio/issues)

</div>

- **Email**: contato@mail.org.br
- **Documentação**: [Django Docs](https://docs.djangoproject.com/)
- **Issues**: [GitHub Issues](https://github.com/salamandery/pyTrimonio/issues)

---

## 👨‍💻 Autor

<div align="center">

![Developer](https://img.shields.io/badge/Developer-Rodolfo%20M.%20F.%20Abreu-blue?style=for-the-badge&logo=github)
![Python](https://img.shields.io/badge/Python-Developer-green?style=for-the-badge&logo=python)
![Django](https://img.shields.io/badge/Django-Expert-orange?style=for-the-badge&logo=django)
![Web Dev](https://img.shields.io/badge/Web-Developer-purple?style=for-the-badge&logo=web)

**by [Rodolfo M. F. Abreu](https://github.com/salamandery)**

[![GitHub](https://img.shields.io/badge/GitHub-rodolfomfabreu-black?style=for-the-badge&logo=github)](https://github.com/salamandery)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Rodolfo%20Abreu-blue?style=for-the-badge&logo=linkedin)](https://linkedin.com/in/rodolfo-marques-ferreira-de-abreu/)

</div>

---

<div align="center">

**🏢 Desenvolvido com ❤️ usando Django e Python 🐍**

[![Made with Love](https://img.shields.io/badge/Made%20with-Love-red.svg?style=for-the-badge&logo=heart)]()
[![Django](https://img.shields.io/badge/Powered%20by-Django-green.svg?style=for-the-badge&logo=django)]()
[![Python](https://img.shields.io/badge/Built%20with-Python-blue.svg?style=for-the-badge&logo=python)]()

</div>