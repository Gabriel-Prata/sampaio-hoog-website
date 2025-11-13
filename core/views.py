from django.views.generic import TemplateView

# Create your views here.

class HomeView(TemplateView):
    """
    View para a página inicial (Home), baseada em classe.
    """
    
    # Define qual arquivo de template esta view deve renderizar.
    # (Equivalente ao 'return render(request, "home.html", {})')
    template_name = 'home.html'

    # (Opcional) Podemos adicionar dados ao contexto (o dict {}) assim:
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['minha_variavel'] = 'Valor'
    #     return context