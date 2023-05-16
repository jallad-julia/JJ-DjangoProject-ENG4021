# JJ-DjangoProject-ENG4021
## Setting up a secret key

1. Setup a new secret environment variable (the lock icon) where the key is `SECRET_KEY` and the value is
   a randomly generated token of 32 bits of randomnese. To generate such a token type this into the shell and hit Enter:
```
python
import secrets
secrets.token_urlsafe(32)
```
2. Hit run!

See this 1 minute video for a walkthrough: [https://www.loom.com/share/ecc4e738149f4d1db3bcff01758b3e71](https://www.loom.com/share/341b5574d12040fb9fcbbff150777f1c)

## Passo a Passo para configurar o projeto Django
1. Crie uma 'secret key' de acordo com os comandos descritos em 'Setting up a secret key'. Em seguida, recarregue a página.
   
2. Para criar um app, digite no shell o seguinte comando e tecle Enter. No local para nome do app, coloque o nome desejado.
```
python
manage.py
startapp nomedoapp
```

3. Para transportar os modelos ao banco de dados, digite no shell o seguinte comando e tecle Enter.
```
python
manage.py
makemigrations
```
Em seguida:
```
python
manage.py
migrate
```

4. Para criar um superusuário para acessar a página do admin, onde podem ser criados e alterados os objetos do modelo, digite no shell o seguinte comando e tecle Enter. Crie um nome para login e uma senha.  
```
python
manage.py
createsuperuser
```
Obs: Ao digitar a senha, atente-se: os caracteres não aparecerão na tela.
