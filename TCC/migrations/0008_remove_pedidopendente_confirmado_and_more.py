# Generated by Django 5.1.2 on 2024-10-22 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0007_pedidopendente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidopendente',
            name='confirmado',
        ),
        migrations.AlterField(
            model_name='pedidopendente',
            name='categoria',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='pedidopendente',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
