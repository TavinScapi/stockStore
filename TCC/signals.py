from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Produto
from django.conf import settings

@receiver(post_save, sender=Produto)
def verificar_quantidade_produto(sender, instance, **kwargs):
    if instance.quantidade < 10:
        # Enviar e-mail se a quantidade for menor que 10
        send_mail(
            'Estoque Baixo - Ação Necessária',
            f'O produto {instance.nome} está com a quantidade baixa ({instance.quantidade} unidades). Considere reabastecer o estoque.',
            settings.EMAIL_HOST_USER,
            ['estoquestockstore@gmail.com'],  # Enviar o e-mail para este endereço
            fail_silently=False,
        )
