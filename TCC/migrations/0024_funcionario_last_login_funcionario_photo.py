# Generated by Django 5.1.2 on 2024-10-29 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0023_produto_estoque_maximo_produto_estoque_minimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
