# Generated by Django 5.1.2 on 2024-10-31 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0024_funcionario_last_login_funcionario_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='password',
            field=models.CharField(max_length=128),
        ),
    ]
