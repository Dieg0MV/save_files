# Generated by Django 5.0.6 on 2024-07-22 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_firm_acta_files_alter_firm_comp_files_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='firm',
            name='Firma_files',
            field=models.FileField(null=True, upload_to='files/'),
        ),
    ]