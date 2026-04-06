from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from .models import Page

class CustomLoginView(LoginView):
    template_name = 'core/login.html'
    redirect_authenticated_user = True

class HomeView(TemplateView):
    template_name = 'home.html'

class PainelListView(LoginRequiredMixin, ListView):
    model = Page
    template_name = 'core/painel_list.html'
    context_object_name = 'pages'

class PainelCreateView(LoginRequiredMixin, CreateView):
    model = Page
    template_name = 'core/painel_form.html'
    fields = ['titulo', 'slug', 'conteudo']
    success_url = reverse_lazy('core:painel_list')

class PainelUpdateView(LoginRequiredMixin, UpdateView):
    model = Page
    template_name = 'core/painel_form.html'
    fields = ['titulo', 'slug', 'conteudo']
    success_url = reverse_lazy('core:painel_list')

class PainelDeleteView(LoginRequiredMixin, DeleteView):
    model = Page
    template_name = 'core/painel_confirm_delete.html'
    success_url = reverse_lazy('core:painel_list')

class PageDetailPublicView(DetailView):
    model = Page
    template_name = 'core/page_detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Buscar até 3 posts mais recentes que não sejam o atual
        context['recent_pages'] = Page.objects.exclude(id=self.object.id).order_by('-criado_em')[:3]
        return context