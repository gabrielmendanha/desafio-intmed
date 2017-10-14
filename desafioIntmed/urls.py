"""desafioIntmed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from intmed import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^itens/', views.ItemList.as_view(), name='itemList'),
    url(r'^item/(?P<item_pk>\d+)/$', views.ItemList.as_view(), name='itemDel'),
    url(r'^mercados/', views.MercadoList.as_view(), name='mercadoList'),
    url(r'^mercado/(?P<mercado_pk>\d+)/$', views.MercadoView.as_view(), name='mercadoPrincipal'),
    url(r'^mercado/(?P<mercado_pk>\d+)/(?P<item_pk>\d+)/$', views.MercadoView.as_view()),
    url(r'^entrega/$', views.EntregaView.as_view(), name='entregaView'),
    url(r'^entrega/(?P<entrega_pk>\d+)/$', views.EntregaView.as_view(), name='entregaViewDel')
]

urlpatterns = format_suffix_patterns(urlpatterns)
