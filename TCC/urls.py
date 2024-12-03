# Importa a função 'path' do módulo 'django.urls' para definir URLs
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Importa as views que serão utilizadas nas URLs
from .views import (
    bem_vindo,  # View para a página de boas-vindas
    remover_produto_tabela,  # View para remover produto da tabela
    remover_produto,  # View para remover um produto
    login_admin,  # View para login do administrador
    home,  # View para a página inicial
    lista_produtos,  # View para listar produtos
    adicionar_produto,
    relatorio,
    USER,
    cadastro_funcionario,
    login_funcionario,
    cadastrar_fornecedor,
    forn,
reposicao_estoque,

homefunc,
lista_produtosFUNC,
editar_produto,
perfilFUNC,
perfilADM,
logout,recusar_pedido, retirar_quantidade,
editar_perfil_funcionario, excluir_funcionario,editar_funcionario,relatorioFUNC,pedir_produto,confirmar_pedido,lista_pedidos, lista_pedidosFUNC

)

# Define as URLs do aplicativo
urlpatterns = [
                  path('', bem_vindo, name='index'),  # URL raiz que redireciona para a página de boas-vindas
                  path('login_adm/', login_admin, name='login_admin'),  # URL para login do administrador
                  path('RELATORIO/', relatorio, name='relatorio'),  # URL para login do administrador
                  path('RELATORIOFUNC/', relatorioFUNC, name='relatorioFUNC'),  # URL para login do administrador

                  path('USER/', USER, name='USER'),  # URL para login do administrador

                  path('HOME/', home, name='home'),  # URL para a página inicial
                  path('HOMEFUNC/', homefunc, name='homefunc'),  # URL para a página inicial
                  # URL para login do funcionário (duplicada)
                  # URL para cadastro de funcionários
                  path('adicionar_produto/', adicionar_produto, name='adicionar_produto'),
                  # URL para adicionar um novo produto
                  path('lista_produtos/', lista_produtos, name='lista_produtos'),  # URL para listar todos os produtos
                  path('lista_produtosFUNC/', lista_produtosFUNC, name='lista_produtosFUNC'),  # URL para listar todos os produtos

                  path('remover_produto/', remover_produto, name='remover_produto'),
                  path('editar_produto/<int:produto_id>/', editar_produto, name='editar_produto'),
                  # Verifique se está assim

                  # URL para remover um produto (não especificado)
                  path('produtos/remover/<int:id>/', remover_produto_tabela, name='remover_produto_tabela'),
                  path('cadastro_funcionario/', cadastro_funcionario, name='cadastro_funcionario'),
                  path('login_funcionario/', login_funcionario, name='login_funcionario'),
                  path('cadastrar/', cadastrar_fornecedor, name='cadastrar_fornecedor'),
                  path('forn/', forn, name='forn'),
                  path('perfilFUNC/', perfilFUNC, name='perfilFUNC'),
                  path('perfilADM/', perfilADM, name='perfilADM'),
                  path('logout/', logout, name='logout'),
                  path('editar_perfil/', editar_perfil_funcionario, name='editar_perfil_funcionario'),
                  path('funcionarios/<int:pk>/excluir/', excluir_funcionario, name='excluir_funcionario'),
                  path('funcionarios/<int:pk>/editar/', editar_funcionario, name='editar_funcionario'),

                  path('reposicao/<int:produto_id>/', reposicao_estoque, name='reposicao_estoque'),
                  path('pedir_produto/', pedir_produto, name='pedir_produto'),
                  path('confirmar_pedido/<int:pedido_id>/', confirmar_pedido, name='confirmar_pedido'),
                  path('lista_pedidos/', lista_pedidos, name='lista_pedidos'),
                  path('recusar_pedido/<int:pedido_id>/', recusar_pedido, name='recusar_pedido'),
                  path('pedidos/retirar/<int:pedido_id>/', retirar_quantidade, name='retirar_quantidade'),
                  path('lista_pedidosFUNC/', lista_pedidosFUNC, name='lista_pedidosFUNC'),

                  # Nova URL

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
