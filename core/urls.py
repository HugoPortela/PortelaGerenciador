from django.conf.urls import url

from portelaGerenciador.core.views import home, cadastro_usuario, sucesso_usuario,cadastro_produtos,sucesso_produto

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^cadastro-usuario/$', cadastro_usuario, name='cadastrousuario'),
    url(r'^sucesso-usuario/$', sucesso_usuario, name='usuariosucesso'),
    url(r'^cadastro-produto/$',cadastro_produtos, name='cadastroproduto'),
    url(r'^sucesso-produto/$',sucesso_produto, name='sucessoproduto'),
]