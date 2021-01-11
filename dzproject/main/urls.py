from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='home'),
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