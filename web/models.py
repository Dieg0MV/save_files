from django.db import models

# Create your models here.
class firm(models.Model):
  Ine_files = models.FileField(max_length=100, default=None)
""" 
  Curp_files = models.FileField()
  Acta_files = models.FileField()
  Comp_files = models.FileField()
  Firma_files = models.FileField() """