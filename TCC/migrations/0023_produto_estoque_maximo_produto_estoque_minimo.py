# Generated by Django 5.1.2 on 2024-10-29 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0022_rename_email_funcionario_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='estoque_maximo',
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name='produto',
            name='estoque_minimo',
            field=models.IntegerField(default=10),
        ),
    ]