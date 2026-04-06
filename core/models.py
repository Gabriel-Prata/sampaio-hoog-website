from django.db import models

# Create your models here.

class Page(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    slug = models.SlugField(unique=True, max_length=200, help_text="A URL da página. Ex: 'meu-post-novo'")
    conteudo = models.TextField(verbose_name="Conteúdo", help_text="Insira o HTML e os estilos Tailwind aqui.")
    criado_em = models.DateTimeField(auto_now_add=True, verbose_name="Criado Em")
    atualizado_em = models.DateTimeField(auto_now=True, verbose_name="Atualizado Em")

    class Meta:
        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ['-criado_em']

    def __str__(self):
        return self.titulo
