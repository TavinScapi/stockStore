# Generated by Django 5.1.2 on 2024-10-23 18:59

import django.contrib.auth.models
import django.contrib.auth.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0012_remove_funcionario_data_criacao_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'verbose_name': 'user', 'verbose_name_plural': 'users'},
        ),
        migrations.AlterModelManagers(
            name='funcionario',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='funcionario',
            name='is_admin',
        ),
        migrations.AddField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(default='000.000.000-00', max_length=14, unique=True),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='groups',
            field=models.ManyToManyField(blank=True, related_name='funcionario_set', to='auth.group'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='is_superuser',
            field=models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='last name'),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='nome_completo',
            field=models.CharField(default='Funcionario', max_length=255),
        ),
        migrations.AddField(
            model_name='funcionario',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='funcionario_user_set', to='auth.permission'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
