# Generated by Django 5.1.2 on 2024-11-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0039_alter_fornecedor_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fornecedor',
            name='telefone',
            field=models.CharField(max_length=50),
        ),
    ]