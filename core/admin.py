from django.contrib import admin
from .models import Page

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'criado_em', 'atualizado_em')
    search_fields = ('titulo', 'slug')
    prepopulated_fields = {'slug': ('titulo',)}
