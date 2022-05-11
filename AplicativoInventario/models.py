from django.db import models
from django.forms import ModelForm
from django.forms import modelform_factory
 
class Inventario(models.Model):
	#Tombo,Descrição_Abreviada,Aquisição,Empenho,Processo,Termo,Tipo_Termo,Recebedor,Responsável,Inservível,Observação,Grupo,Localidade,Valor
    tombo               = models.CharField("Tombo",                 max_length=255, primary_key=True)    
    descricao_abreviada = models.CharField("Descrição Abreviada",   max_length=255, blank=True)
    aquisicao           = models.CharField("Aquisição",             max_length=255, blank=True)    
    empenho             = models.CharField("Empenho",               max_length=255, blank=True)
    processo            = models.CharField("Processo",              max_length=255, blank=True)
    termo               = models.CharField("Termo",                 max_length=255, blank=True)
    tipo_termo          = models.CharField("Tipo Termo",            max_length=255, blank=True)
    recebedor           = models.CharField("Recebedor",             max_length=255, blank=True)
    responsavel         = models.CharField("Responsável",           max_length=255, blank=True)
    inservivel          = models.CharField("Inservível",            max_length=255, blank=True)
    observacao          = models.CharField("Observação",            max_length=255, blank=True)
    grupo               = models.CharField("Grupo",                 max_length=255, blank=True)
    localidade          = models.CharField("Localidade",            max_length=255, blank=True)
    valor               = models.CharField("Valor",                 max_length=255, blank=True)
        
    # Inventario.equipamento.all() provê lista de todos Inventarios.
    equipamento         = models.Manager()
    
    def __str__(self):
        return self.tombo 
    
    class Meta:
        ordering = ["tombo"]
        verbose_name_plural = "Tombos"    
        
InventarioForm = modelform_factory(Inventario, fields=("tombo", "descricao_abreviada","aquisicao","empenho","processo","termo","tipo_termo","recebedor","responsavel","inservivel","observacao","grupo","localidade","valor"))










#class InventarioForm(ModelForm):
#    class Meta:
#        model = Inventario
#        fields = '__all__'    

# TO DO    
# from geography.models import ZipCode
#zip_code = models.ForeignKey(
#    ZipCode,
#    on_delete=models.SET_NULL,
#    blank=True,
#    null=True,
#)