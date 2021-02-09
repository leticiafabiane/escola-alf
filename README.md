# ESCOLA ALF
Programa #Código&lt;para>todXs

### Pré-requisitos
Python 3

### Instalação
Criação da pasta do projeto
```
mkdir escola_alf
```
```
cd escola_alf
```

Criação do ambiente virtual para isolar as dependencias localmente
```
python -m venv env
```
```
Unix: source env/bin/activate
```
```
Windows: env\Scripts\activate
```

Instalar o Django e o Django REST Framework no ambiente virtual
```
pip install django
```
```
pip install djangorestframework
```

Clonar o projeto
```
git clone https://github.com/leticiafabiane/escola-alf.git
```

Entrar na pasta do projeto Django
```
cd escola-alf
```

Criar as migrações do banco de dados
```
python manage.py makemigrations
```

Criar as migrações do banco de dados
```
python manage.py migrate
```

Criar super user
```
python manage.py createsuperuser --email seu@email.com --username admin
```

Iniciar o servidor
```
python manage.py runserver
```

Para explorar a API entrar no endereço:
```
http://127.0.0.1:8000/
```
