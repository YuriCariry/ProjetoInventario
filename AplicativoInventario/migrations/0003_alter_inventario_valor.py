# Generated by Django 4.0.4 on 2022-05-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AplicativoInventario', '0002_alter_inventario_valor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='valor',
            field=models.CharField(blank=True, max_length=255, verbose_name='Valor'),
        ),
    ]
