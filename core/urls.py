# Em core/urls.py (NOVO ARQUIVO)

from django.urls import path
from . import views # Importa as views do app 'core'

# Este 'app_name' ajuda a organizar as URLs
app_name = 'core'

urlpatterns = [
    # path(URL_DESEJADA, VIEW_ASSOCIADA, NOME_DA_URL)
    path('', views.HomeView.as_view(), name='home'),
]