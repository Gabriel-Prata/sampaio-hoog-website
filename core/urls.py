from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    # Autenticação
    path('shlogin/', views.CustomLoginView.as_view(), name='login'),
    path('shlogout/', LogoutView.as_view(next_page='core:home'), name='logout'),

    # Painel de Administração Customizado
    path('painel/', views.PainelListView.as_view(), name='painel_list'),
    path('painel/novo/', views.PainelCreateView.as_view(), name='painel_create'),
    path('painel/<int:pk>/editar/', views.PainelUpdateView.as_view(), name='painel_update'),
    path('painel/<int:pk>/excluir/', views.PainelDeleteView.as_view(), name='painel_delete'),

    # Renderização da Página (deve ficar por último para não dar match em rotas fixas)
    path('<slug:slug>/', views.PageDetailPublicView.as_view(), name='page_detail'),
]