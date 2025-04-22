## 📦 Sistema de Inventário + Relatórios

### Índice

- 💡[ Sobre](#-sobre)
- 🛠[ Tecnologias utilizadas](#-tecnologias-utilizadas)
- 📥[ Como baixar o projeto](#-como-baixar-o-projeto)
- ⚙️[ Funcionalidades](#-funcionalidades)

---

## 💡 Sobre

O **Sistema de Inventário + Relatórios** é uma aplicação web desenvolvida para controle de estoque e geração de relatórios. Voltado para empresas que precisam registrar entradas e saídas de produtos, cadastrar fornecedores e gerenciar o acesso de funcionários e administradores.

A aplicação é dividida em dois perfis:

- **Administrador**: Pode cadastrar usuários, fornecedores e produtos, além de acessar todos os relatórios.
- **Funcionário**: Pode cadastrar e visualizar produtos e fornecedores.

---

## 🛠 Tecnologias utilizadas

### 🔙 Back-end

- 🐍 Python  
- ⚡ FastAPI  
- 🔃 Uvicorn  
- 🧱 SQLAlchemy  
- 🐬 PyMySQL  
- 🔐 Python-JOSE & Passlib (JWT e autenticação)

### 💻 Front-end

- ⚛️ React.js  
- 📘 TypeScript  
- 🔗 Axios  
- 🔀 React Router DOM

---

## 📥 Como baixar o projeto

```bash
# 1. Clonar o repositório
$ git clone https://github.com/juniorbraz93/inventory_control.git

# 2. Configurar o Backend
$ cd /backend

# Crie o ambiente virtual
$ python -m venv venv
$ source venv/bin/activate  # ou venv\Scripts\activate no Windows

# Instale as dependências
$ pip install -r requirements.txt

# Configure a variável DATABASE_URL no arquivo .env
DATABASE_URL=mysql+pymysql://usuario:senha@localhost/inventario

# Rode o backend
$ uvicorn app.main:app --reload

# 3. Configurar o Frontend
$ cd ../frontend

# Instale as dependências
$ yarn or npm install

# Execute o frontend
$ yarn start or npm start
```

---

## ⚙️ Funcionalidades

### 👤 Autenticação e Perfis

- Login com email e senha.
- Geração de token JWT para acesso às rotas.
- Permissões de acesso diferentes para **administradores** e **funcionários**.

### 📦 Produtos

- Cadastro, listagem, edição e exclusão de produtos.
- Cada produto pode conter: nome, descrição, quantidade, preço e fornecedor.

### 🧾 Fornecedores

- Cadastro e gerenciamento de fornecedores com nome, e-mail e telefone.

### 👥 Usuários

- Cadastro de novos usuários com definição de perfil (admin ou funcionário).
- Apenas administradores podem registrar novos usuários.

### 📈 Relatórios (em breve)

- Geração de relatórios por **data**, **categoria** ou **produto**.
- Exportação em **PDF** ou **CSV** (funcionalidade planejada).

---

Desenvolvido com 💻 por [Junior Braz](https://github.com/juniorbraz93)
