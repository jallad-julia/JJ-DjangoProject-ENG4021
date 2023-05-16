from django.shortcuts import render,redirect
#Os modelos criados devem ser importados para que possam ser utilizados nas funções.
from .models import Técnicos
from .models import Ranking


# Funções que irão renderizar os URLs na pasta templates: 

#Função para renderizar 'home.html':
def home (request):
  todosTecnicos = Técnicos.objects.all()
  atletasRanking= Ranking.objects.all()
  context = {"todosTecnicos": todosTecnicos, "atletasRanking": atletasRanking}
  return render(request, 'home.html',context=context)


#Função para renderizar 'tecnicos_form.html':
#São criados objetos do modelo Técnicos nos quais: a chave em 'request.POST' é o nome da informação indicada no html e o valor, colocado pelo usuário, é atribuído ao atributo determinado na criação do modelo. 

def create_listas(request):
  if request.method == "POST":
      print(request.POST)
      Técnicos.objects.create(
        title  = request.POST["title"],
        lastname= request.POST["lastname"],
        entradanoct= request.POST["entradanoCT"],
        pagamento= False
    
      )
      return redirect('home')  #O usuário é redirecionado para a página principal.
  return render(request,"tecnicos_form.html")


#Função para renderizar 'ranking_form.html':
#São criados objetos do modelo Ranking nos quais: a chave em 'request.POST' é o nome do atributo indicado no html e o valor é atribuído ao nome do atributo determinado na criação do modelo. 
def create_ranking(request):
  if request.method == "POST":
      print(request.POST)
      Ranking.objects.create(
        title  = request.POST["title"],
        lastname= request.POST["lastname"],
        aniversario= request.POST["dtAniversario"],
        primeiraparticipacao= False
    
      )
      return redirect('home') #O usuário é redirecionado para a página principal.
  return render(request,"ranking_form.html")

#Função para renderizar "update_tecnicos.html":
#É necessário passar o id do objeto técnico para que possa ser acessado para edição o técnico selecionado. No contexto fornecido no return, a chave (string) corresponde ao nome utilizado para se referir ao objeto no arquivo html e o valor corresponde à variável definida no início da função, no caso, tecnico.  
#O value do input de cada dado do objeto técnico no arquivo html utiliza a chave definida para exibir o dado sobre o objeto já existente. 
def update_tecnicos(request,tecnico_id):
  tecnico= Técnicos.objects.get(id=tecnico_id)
  tecnico.entradanoct= tecnico.entradanoct.strftime('%Y-%m-%d')
  if request.method == "POST":
    tecnico.title= request.POST["title"],
    tecnico.lastname=request.POST["lastname"],
    tecnico.entradanoct=request.POST["entradanoCT"],
    if 'done' not in request.POST:
      tecnico.pagamento = False
    else:
      tecnico.pagamento= True
    tecnico.save()
    return redirect("list_tec_rank")
  
  return render(request,'update_tecnicos.html',context= {'tecnico': tecnico })


#Função para renderizar "delete_tecnicos.html":
#É necessário passar o id do objeto técnico para que possa ser acessado para remoção o técnico selecionado. 
def delete_tecnicos(request,tecnico_id):
  tecnico=Técnicos.objects.get(id=tecnico_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      tecnico.delete()
    return redirect('list_tec_rank') 
  return render(request, "delete_tecnicos.html", context={"tecnico": tecnico})


#Função para renderizar "update_ranking.html":
#É necessário passar o id do objeto atleta para que possa ser acessado para edição o atleta selecionado. No contexto fornecido no return, a chave (string) corresponde ao nome utilizado para se referir ao objeto no arquivo html e o valor corresponde à variável definida no início da função, no caso, tecnico.  
# O value do input de cada dado do objeto atleta no arquivo html utiliza a chave definida para exibir o dado sobre o objeto já existente. 
# 
def update_atletas(request,atleta_id):
  atleta= Ranking.objects.get(id=atleta_id)
  atleta.primeiraparticipacao= atleta.primeiraparticipacao.strftime('%Y-%m-%d')
  if request.method == "POST":
    atleta.title= request.POST["title"],
    atleta.lastname=request.POST["lastname"],
    atleta.entradanoct=request.POST["dtAniversario"],
    if 'done' not in request.POST:
      atleta.primeiraparticipacao = False
    else:
      atleta.primeiraparticipacao= True
    atleta.save()
    return redirect('list_tec_rank')
  
  return render(request,'update_ranking.html',context= {'atleta': atleta })


#Função para renderizar "delete_ranking.html":
#É necessário passar o id do objeto atleta para que possa ser acessado para remover o atleta selecionado. 

def delete_atletas(request,atleta_id):
  atleta=Ranking.objects.get(id=atleta_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      atleta.delete()
    return redirect('list_tec_rank') 
  return render(request, "delete_ranking.html", context={"atleta": atleta})


#Função para renderizar "list_tecnicos_ranking.html":
#Nesse URL, são enumerados todos os objetos tecnicos e atletas, com a opção de edição e remoção dos objetos. 
def list_tecnicos_ranking(request):
  todosTecnicos = Técnicos.objects.all()
  atletasRanking= Ranking.objects.all()
  context = {"todosTecnicos": todosTecnicos, "atletasRanking": atletasRanking}
  return render(request, 'list_tecnicos_ranking.html',context=context)


