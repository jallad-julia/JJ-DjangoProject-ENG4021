from django.db import models

#Aqui são criados os modelos (ou classes) com seus respectivos atributos. Para transportar modelos para o banco de dados, siga as instruções na pasta ReadMe.

class Técnicos(models.Model):
  title = models.CharField(max_length = 20)
  lastname = models.CharField(max_length= 20)
  entradanoct = models.DateField()
  pagamento= models.BooleanField()

class Ranking(models.Model):
    title = models.CharField(max_length= 20)
    lastname = models.CharField(max_length= 20)
    aniversario = models.DateField()
    primeiraparticipacao= models.BooleanField()

