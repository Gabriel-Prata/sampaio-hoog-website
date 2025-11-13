
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # URLs dos meus APPs
    path('', include('core.urls', namespace='core')),
]
