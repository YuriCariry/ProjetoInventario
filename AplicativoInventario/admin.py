from django.contrib import admin
from .models import Inventario

admin.site.register(Inventario)

class InventarioAdmin(admin.ModelAdmin):    
    list_display = ('tombo', 'descricao_abreviada')
    #Tombo,Descrição_Abreviada,Aquisição,Empenho,Processo,Termo,Tipo_Termo,Recebedor,Responsável,Inservível,Observação,Grupo,Localidade,Valor