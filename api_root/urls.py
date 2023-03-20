
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api_rest.urls'), name='api_rest_urls')                                            #Vai buscar as funções do nosso aplicativo no caso as url do app api_rest.
]
