from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
path('',views.index, name='home'),

    path('create-fold', views.FoldCreate.as_view(), name='fold_create_url'),
    path('create-item', views.ItemCreate.as_view(), name='item_create_url'),
    #path('folds/<int:pk>/update', views.FoldUpdate.as_view(), name='fold_update_url'),

    path('first',views.first, name='fir'),
    path('instruction', views.instruction, name='instruction'),
    path('second',views.second, name='sec'),
    path('third',views.third, name='thi'),
    path('folds',views.folds_home, name='folds_home'),
    path('items',views.items_home, name='items_home'),
    path('items/full_list', views.item_list, name='items_list'),
    path('items/full_list_f', views.fold_list, name='folds_list'),

    path('folds/<int:pk>', views.FoldDetailView.as_view(), name='fold-detail'),
    path('folds/<int:pk>/update', views.FoldUpdateView.as_view(), name='fold-update'),
    path('folds/<int:pk>/delete', views.FoldDeleteView.as_view(), name='fold-delete'),
    path('items/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
    path('items/<int:pk>/update', views.ItemUpdateView.as_view(), name='item-update'),
    path('items/<int:pk>/delete', views.ItemDeleteView.as_view(), name='item-delete'),


]