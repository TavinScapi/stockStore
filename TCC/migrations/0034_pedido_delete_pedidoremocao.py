# Generated by Django 5.1.2 on 2024-11-06 23:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TCC', '0033_pedidoremocao_delete_pedido'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade_pedida', models.IntegerField()),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Confirmado', 'Confirmado'), ('Recusado', 'Recusado')], default='Pendente', max_length=10)),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TCC.produto')),
            ],
        ),
        migrations.DeleteModel(
            name='PedidoRemocao',
        ),
    ]
