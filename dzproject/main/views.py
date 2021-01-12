from django.shortcuts import render, redirect
from .models import FoldNew, ItemNew
from .forms import *
from django.views.generic import DetailView,UpdateView, DeleteView, View
from django.db.models import F
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages




def index(request):
    return render(request, 'main/master.html')


def first(request):
    get_items = ItemNew.objects.all()
    get_folds = FoldNew.objects.all()


    return render(request, 'main/first.html', {'title':"Примерный сводный отчет",
                                               'get_item': get_items,'get_fold': get_folds})


def second(request):
    items = ItemNew.objects.all()
    return render(request, 'main/second.html', {'title':"Вторая страница сайта", 'item': items})


def third(request):
    #warehouses = WareHouse.objects.find() - найти объект по его айди order - сортировка
    warehouses = FoldNew.objects.all()
    return render(request, 'main/third.html', {'title':"Третья страница сайта", 'warehouses': warehouses})


class FoldCreate(View):
    def get(self,request):
        form = NewFoldCreateForm()
        return render(request, 'main/new_fold_create.html',{'form' : form})

    def post(self, request):
        post_form = NewFoldCreateForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('/third')
        else:
            return render(request, 'main/new_fold_create.html',{'form' : post_form})


class ItemCreate(View):
    def get(self,request):
        form = NewItemCreateForm()
        return render(request, 'main/new_item_create.html',{'form' : form})

    def post(self, request):
        post_form = NewItemCreateForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('/second')
        else:
            return render(request, 'main/new_item_create.html',{'form' : post_form})


def folds_home(request):
    items = FoldNew.objects.all()
    return render(request, 'main/folds_home.html', {'title': "Складыю. Главная", 'items': items})

def createitem(request):
    error = ''
    if request.method == 'POST':
        form = ItemCreateTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/second')
        else:
            error = 'Данные на форме неверны!'

    form = ItemCreateTestForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_item.html', context)


def createfold(request):
    error = ''
    if request.method == 'POST':
        form = WareHouseCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/third')
        else:
            error = 'Данные на форме неверны!'

    form = WareHouseCreateForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_fold.html', context)


"""class FoldUpdate(View):
    def get(self,request):
        fold = FoldNew.objects.get(id__iexact=self.id)
        bound_form=NewFoldCreateForm(instance=fold)
        return render(request, 'main/update_new_fold.html', context={'form': bound_form, 'folds': fold})
"""

class FoldDetailView(DetailView):
    model = FoldNew
    template_name = 'main/fold_detail.html'
    context_object_name = 'folds'


class FoldUpdateView(UpdateView):
    model = FoldNew
    template_name = 'main/update_new_fold.html'

#    form_class = NewFoldCreateForm
    form_class = NewFoldUpdateForm


class FoldDeleteView(DeleteView):
    model = FoldNew
    success_url = '/third'
    template_name = 'main/delete_fold.html'

    form_class = WareHouseCreateForm