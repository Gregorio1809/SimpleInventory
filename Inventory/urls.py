from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'Inventory'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^home/$', views.HomeView.as_view(), name='home'),
    url(r'^(?P<item_id>[0-9]+)/detail/$', views.details, name='details'),
    # url(r'^(?P<item_id>[0-9]+)/detail/transfer/$', views.returnitm, name='transferitm'),
    # url(r'^(?P<item_id>[0-9]+)/detail/return/$', views.returnitm(), name='returnitm'),
    # url(r'^create_item/$', views.create_item, name='create_item'),
    url(r'^item/add/$', views.ItemCreate.as_view(), name='item_form'),
    url(r'^item/(?P<pk>[0-9]+)/delete/$', views.ItemDelete.as_view(), name='item-delete'),
    url(r'^client/add/$', views.ClientCreate.as_view(), name='client_form'),
    url(r'^category/add/$', views.CategoryCreate.as_view(), name='category_form'),
    url(r'^value/add/$', views.ValueCreate.as_view(), name='value_form'),
    url(r'^client/(?P<pk>[0-9]+)/delete/$', views.ValueDelete.as_view(), name='client-delete'),
    url(r'^category/(?P<pk>[0-9]+)/delete/$', views.CategoryDelete.as_view(), name='category-delete'),
    url(r'^value/(?P<pk>[0-9]+)/delete/$', views.ValueDelete.as_view(), name='value-delete'),


    # path('', views.index, name='index'),
    # path('<int:item_id>/', views.details, name='details'),
    # path('item/add', views.create_item, name='item_form'),
    path('<int:item_id>/detail/transfer', views.transferitm, name='transferitm'),
    path('<int:item_id>/detail/return', views.returnitm, name='returnitm'),
]
