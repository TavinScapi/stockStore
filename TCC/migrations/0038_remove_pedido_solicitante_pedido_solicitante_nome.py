# Generated by Django 5.1.2 on 2024-11-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0037_alter_pedido_solicitante'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='solicitante',
        ),
        migrations.AddField(
            model_name='pedido',
            name='solicitante_nome',
            field=models.CharField(default='Desconhecido', max_length=255),
        ),
    ]