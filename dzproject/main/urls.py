from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='home'),

    path('create-fold', views.FoldCreate.as_view(), name='fold_create_url'),
    path('create-item', views.ItemCreate.as_view(), name='item_create_url'),
   # path('folds/<int:pk>/update/', views.FoldUpdate.as_view(), name='fold_update_url'),

    path('first',views.first, name='fir'),
    path('second',views.second, name='sec'),
    path('third',views.third, name='thi'),
    path('folds',views.folds_home, name='folds_home'),
    path('CreateFold', views.createfold, name='createFold'),
    path('folds/<int:pk>', views.FoldDetailView.as_view(), name='fold-detail'),
    path('folds/<int:pk>/update', views.FoldUpdateView.as_view(), name='fold-update'),
    path('folds/<int:pk>/delete', views.FoldDeleteView.as_view(), name='fold-delete'),
    path('CreateItem', views.createitem, name='createItem'),

]
