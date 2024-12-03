from django.db import models
from django.contrib.auth.models import User  # Importa o modelo User para referência futura, se necessário

from django.db import models

class Fornecedor(models.Model):
    """
    Modelo para representar um fornecedor.
    """
    nome = models.CharField(max_length=100)  # Nome do fornecedor
    endereco = models.CharField(max_length=255)  # Endereço do fornecedor
    telefone = models.CharField(max_length=50)  # Telefone do fornecedor
    email = models.EmailField()  # Email do fornecedor
    servicos = models.TextField()  # Serviços oferecidos pelo fornecedor
    foto = models.ImageField(upload_to='fornecedores/', blank=True, null=True)  # Foto local
    foto_url = models.URLField(blank=True, null=True)  # URL da foto externa

    def __str__(self):
        return self.nome  # Representação em string do fornecedor




from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class Produto(models.Model):
    """
    Modelo para representar um produto.
    """
    CATEGORIAS_CHOICES = [
        ('escritorio', 'Escritório'),
        ('limpeza', 'Limpeza'),
        ('eletronicos', 'Eletrônicos'),
        ('materiais', 'Materiais'),
    ]

    nome = models.CharField(max_length=100)  # Nome do produto
    descricao = models.TextField()  # Descrição do produto
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Preço do produto
    quantidade = models.IntegerField()  # Quantidade disponível
    categoria = models.CharField(max_length=20, choices=CATEGORIAS_CHOICES,
                                 default='escritorio')  # Categoria do produto
    estoque_minimo = models.IntegerField(default=10)  # Estoque mínimo para o produto
    estoque_maximo = models.IntegerField(default=100)  # Estoque máximo para o produto
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE, null=True,
                                   blank=True)  # Relação com o fornecedor

    def __str__(self):
        return self.nome  # Representação em string do produto

    def save(self, *args, **kwargs):
        # Verificar estoque antes de salvar
        if self.quantidade <= self.estoque_minimo:
            self.enviar_email_estoque_baixo()
        super().save(*args, **kwargs)

    def enviar_email_estoque_baixo(self):
        """
        Envia um e-mail de alerta quando o estoque está baixo.
        """
        assunto = f"Estoque Baixo: {self.nome}"
        contexto = {
            'produto': self,
        }

        # Carregar o conteúdo do e-mail com um template HTML
        mensagem_html = render_to_string('TCC/emails/index.html', contexto)
        mensagem_texto = strip_tags(mensagem_html)

        send_mail(
            assunto,
            mensagem_texto,
            'estoquestockstore@gmail.com',  # Remetente
            ['estoquestockstore@gmail.com'],  # Destinatário
            html_message=mensagem_html,
        )


class Funcionario(models.Model):
    """
    Modelo para representar um funcionário.
    """
    firstname = models.CharField(max_length=100)  # Primeiro nome do funcionário
    lastname = models.CharField(max_length=100)  # Sobrenome do funcionário
    email = models.EmailField(unique=True)  # Email único do funcionário
    phone = models.CharField(max_length=15)  # Telefone do funcionário
    username = models.CharField(max_length=50, unique=True)  # Nome de usuário único
    password = models.CharField(max_length=50)  # Senha do funcionário
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)  # Campo para a foto do funcionário
    last_login = models.DateTimeField(auto_now=True)  # Data e hora da última vez que o funcionário fez login

    def __str__(self):
        return self.username  # Representação em string do funcionário

from django.db import models

class Pedido(models.Model):
    STATUS_CHOICES = [
        ('Pendente', 'Pendente'),
        ('Confirmado', 'Confirmado'),
        ('Recusado', 'Recusado'),
    ]

    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade_pedida = models.IntegerField()
    solicitante_nome = models.CharField(max_length=255, default='Desconhecido')  # Default value here
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pendente')
    data_pedido = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantidade_pedida} unidade(s) de {self.produto.nome} - {self.status} por {self.solicitante_nome}"
