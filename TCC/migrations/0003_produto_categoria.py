# Generated by Django 5.1.1 on 2024-10-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0002_produto_preco_alter_produto_quantidade'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='categoria',
            field=models.CharField(choices=[('escritorio', 'Escritório'), ('limpeza', 'Limpeza'), ('eletronicos', 'Eletrônicos')], default='escritorio', max_length=20),
        ),
    ]
