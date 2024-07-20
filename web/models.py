from django.db import models

# Create your models here.
class firm(models.Model):
  Ine_files = models.FileField(max_length=100, upload_to="files/", null=False, blank=False)
  Curp_files = models.FileField(max_length=100, upload_to="files/", null=False, blank=False)
  Acta_files = models.FileField(max_length=100, upload_to="files/", null=False, blank=False)
  Comp_files = models.FileField(max_length=100, upload_to="files/", null=False, blank=False)

# Firma_files = models.FileField(max_length=100, default='default_files/placeholder.pdf')
  #def __str__():
    