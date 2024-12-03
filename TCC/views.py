from django.contrib import messages
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Produto, Fornecedor, Funcionario, Pedido
from .forms import ProdutoForm, FornecedorForm, CadastroFuncionarioForm, LoginForm, FuncionarioForm, FuncionarioForm2


def bem_vindo(request):
    return render(request, 'TCC/index.html')


def USER(request):
    query = request.GET.get('q', '')
    if query:
        funcionarios = Funcionario.objects.filter(firstname__icontains=query) | Funcionario.objects.filter(lastname__icontains=query)
    else:
        funcionarios = Funcionario.objects.all()
    return render(request, 'TCC/CONFIG/index.html', {'funcionarios': funcionarios, 'query': query})


def perfilADM(request):
    user = request.user
    last_logout_date = request.session.get('last_logout_date', 'N/A')
    return render(request, 'TCC/PERFIL/index.html', {'user': user, 'last_logout_date': last_logout_date})


def perfilFUNC(request):
    if request.method == 'GET':
        funcionario_id = request.session.get('funcionario_id')
        if funcionario_id:
            funcionario = get_object_or_404(Funcionario, id=funcionario_id)
            return render(request, 'TCC/PERFIL/FUNC/index.html', {'funcionario': funcionario})
        else:
            return redirect('login_funcionario')


def login_admin(request):
    return render(request, 'TCC/LOGIN/index.html')


def home(request):
    return render(request, 'TCC/HOME/index.html')


def homefunc(request):
    return render(request, 'TCC/HOME/HOMEFUNC/index.html')


def lista_produtos(request):
    produtos = Produto.objects.all()
    return render(request, 'TCC/ESTOQUE/index.html', {'produtos': produtos})


def lista_produtosFUNC(request):
    produtos = Produto.objects.all()

    if request.method == 'GET':
        funcionario_id = request.session.get('funcionario_id')
        if funcionario_id:
            funcionario = get_object_or_404(Funcionario, id=funcionario_id)
            return render(request, 'TCC/ESTOQUEFUNC/index.html', {'produtos': produtos, 'funcionario': funcionario})
        else:
            return redirect('login_funcionario')

    return render(request, 'TCC/ESTOQUEFUNC/index.html', {'produtos': produtos})

def adicionar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adicionado com sucesso!')
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    fornecedores = Fornecedor.objects.all()
    return render(request, 'TCC/ESTOQUE/add/index.html', {'form': form, 'fornecedores': fornecedores})


def remover_produto(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade_remover = int(request.POST.get('quantidade', 0))
        produto = get_object_or_404(Produto, id=produto_id)
        if 0 < quantidade_remover <= produto.quantidade:
            produto.quantidade -= quantidade_remover
            produto.save()
            if produto.quantidade == 0:
                messages.warning(request, f'{produto.nome} está indisponível!')
            else:
                messages.success(request, f'{quantidade_remover} unidade(s) de {produto.nome} removida(s) com sucesso!')
        else:
            messages.error(request, 'Quantidade inválida!')
        return redirect('lista_produtos')
    else:
        produtos = Produto.objects.all()
        return render(request, 'TCC/ESTOQUE/rm/index.html', {'produtos': produtos})


def editar_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'TCC/ESTOQUE/edit/index.html', {'form': form})


@require_http_methods(["POST"])
def remover_produto_tabela(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    messages.success(request, f'{produto.nome} foi removido da tabela com sucesso!')
    return redirect('lista_produtos')


def relatorio(request):
    produtos = Produto.objects.all()
    return render(request, 'TCC/RELATORIO/index.html', {'produtos': produtos})


def relatorioFUNC(request):
    produtos = Produto.objects.all()
    return render(request, 'TCC/RELATORIO/RELATORIOFUNC/index.html', {'produtos': produtos})


def cadastrar_fornecedor(request):
    if request.method == 'POST':
        form = FornecedorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('forn')
    else:
        form = FornecedorForm()
    return render(request, 'TCC/FORN/CADASTRARFORN/index.html', {'form': form})


def forn(request):
    fornecedores = Fornecedor.objects.all()
    return render(request, 'TCC/FORN/index.html', {'fornecedores': fornecedores})


def reposicao_estoque(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    if request.method == 'POST':
        quantidade_adicionada = int(request.POST.get('quantidade'))
        produto.quantidade += quantidade_adicionada
        produto.save()
        return redirect('lista_produtos')
    return render(request, 'TCC/ESTOQUE/repor/index.html', {'produto': produto})


def cadastro_funcionario(request):
    if request.method == 'POST':
        form = CadastroFuncionarioForm(request.POST)
        if form.is_valid():
            funcionario = form.save(commit=False)
            funcionario.password = form.cleaned_data['password']
            funcionario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login_funcionario')
    else:
        form = CadastroFuncionarioForm()
    return render(request, 'TCC/CADASTRO/index.html', {'form': form})


def login_funcionario(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            funcionario = Funcionario.objects.filter(username=username, password=password).first()
            if funcionario:
                request.session['funcionario_id'] = funcionario.id
                return redirect('homefunc')
            else:
                messages.error(request, 'Usuário ou Senha incorretos.')
    else:
        form = LoginForm()
    return render(request, 'TCC/LOGINFUNC/index.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect('index')


def editar_perfil_funcionario(request):
    funcionario = get_object_or_404(Funcionario, id=request.session['funcionario_id'])
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil atualizado com sucesso!')
            return redirect('perfilFUNC')
    else:
        form = FuncionarioForm(instance=funcionario)
    return render(request, 'TCC/PERFIL/edit/index.html', {'form': form, 'funcionario': funcionario})


def excluir_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('USER')
    return render(request, 'TCC/CONFIG/excluir/index.html', {'funcionario': funcionario})


def editar_funcionario(request, pk):
    funcionario = get_object_or_404(Funcionario, pk=pk)
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, request.FILES, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('USER')
    else:
        form = FuncionarioForm2(instance=funcionario)
    return render(request, 'TCC/CONFIG/editar/index.html', {'form': form, 'funcionario': funcionario})


def pedir_produto(request):
    if request.method == 'POST':
        produto_id = request.POST.get('produto_id')
        quantidade_pedida = int(request.POST.get('quantidade', 0))
        solicitante_nome = request.POST.get('solicitante')  # Recebe o nome do solicitante digitado pelo usuário
        produto = get_object_or_404(Produto, id=produto_id)

        if quantidade_pedida > 0:
            pedido = Pedido.objects.create(
                produto=produto,
                quantidade_pedida=quantidade_pedida,
                solicitante_nome=solicitante_nome,  # Salva o nome do solicitante
                status='Pendente'
            )
            messages.info(request, f'Pedido de {quantidade_pedida} unidade(s) de {produto.nome} criado por {solicitante_nome}!')
        else:
            messages.error(request, 'Quantidade inválida!')
        return redirect('lista_produtosFUNC')

    produtos = Produto.objects.all()
    return render(request, 'TCC/ESTOQUE/pedir/index.html', {'produtos': produtos})


def lista_pedidos(request):
    pedidos = Pedido.objects.all()
    return render(request, 'TCC/pedidos/index.html', {'pedidos': pedidos})

def lista_pedidosFUNC(request):
    pedidos = Pedido.objects.all()
    return render(request, 'TCC/pedidos/PEDIDOSFUNC/index.html', {'pedidos': pedidos})


def confirmar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.status = 'Confirmado'
    pedido.save()
    messages.success(request, f'Pedido de {pedido.quantidade_pedida} unidade(s) de {pedido.produto.nome} confirmado!')
    return redirect('lista_pedidos')


def recusar_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    pedido.status = 'Recusado'
    pedido.save()
    messages.warning(request, f'O pedido de {pedido.produto.nome} foi recusado.')
    return redirect('lista_pedidos')


def retirar_quantidade(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    produto = pedido.produto
    if pedido.status == 'Confirmado':
        if pedido.quantidade_pedida <= produto.quantidade:
            produto.quantidade -= pedido.quantidade_pedida
            produto.save()
            pedido.status = 'Quantidade Retirada'
            pedido.save()
            messages.success(request,
                             f'Estoque atualizado! {pedido.quantidade_pedida} unidade(s) de {produto.nome} foram retiradas.')
        else:
            messages.error(request, f'Estoque insuficiente para retirar a quantidade solicitada de {produto.nome}.')
    else:
        messages.error(request, 'O pedido já teve a quantidade retirada ou não está no status "Confirmado".')

    return redirect('lista_pedidos')


from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def enviar_email_estoque(produto):
    assunto = f"Estoque baixo: {produto.nome}"
    contexto = {
        'produto': produto,
    }

    mensagem_html = render_to_string('TCC/emails/index.html', contexto)
    mensagem_texto = strip_tags(mensagem_html)

    send_mail(
        assunto,
        mensagem_texto,
        'estoquestockstore@gmail.com',  # Remetente
        ['estoquestockstore@gmail.com'],  # Destinatário
        html_message=mensagem_html,
    )