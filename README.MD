Para rodar o projeto:

- É necessário python3.8 com o pacote pipenv instalado:

  ``pip3 install pipenv``

- Clone o repositório:

  ``git clone https://github.com/Mr-Saxobeat/jeraflix.git``

- Dentro da pasta do repositório, instale o ambiente virtual e rode-o:
 ```
  cd jeraflix
  pipenv install
  pipenv shell
 ```
- Crie um arquivo .env na raíz da pasta jeraflix, insira a seguinte linha nele para configurar o banco de dados e salve-o:
 
  ``DATABASE_URL=sqlite:///db.sqlite3``
 
- Aplique as migrações do Django:
 
  ``python manage.py migrate``
 
- Rode o servidor:
 
  ``python manage.py runserver``
