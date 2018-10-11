from django.urls import path
from django.contrib import admin
from django.conf.urls import url, include

from django.contrib.auth import views

from . import views

app_name = 'Inventory'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^item/$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<item_id>[0-9]+)/detail/$', views.details, name='details'),

    url(r'^item/add/$', views.ItemCreate.as_view(), name='item_form'),
    url(r'^item/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name='item-delete'),
    url(r'^client/add/$', views.ClientCreate.as_view(), name='client_form'),
    url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_form'),
    url(r'^value/add/$', views.ValueCreate.as_view(), name='value_form'),
    url(r'^client/(?P<pk>[0-9]+)/delete/$', views.ClientDelete.as_view(), name='client-delete'),
    url(r'^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='category-delete'),
    url(r'^value/(?P<pk>[0-9]+)/delete/$', views.ValueDelete.as_view(), name='value-delete'),

    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('<int:item_id>/detail/transfer', views.transferitm, name='transferitm'),
    path('<int:item_id>/detail/return', views.returnitm, name='returnitm'),


]

handler404 = 'Inventory.views.handler404'
handler500 = 'Inventory.views.handler500'
