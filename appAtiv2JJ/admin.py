from django.contrib import admin
from .models import Ranking
from .models import Técnicos

# Os modelos são registrados aqui. Aparecerão na página do "admin" do URL criado.

admin.site.register(Ranking)
admin.site.register(Técnicos)


