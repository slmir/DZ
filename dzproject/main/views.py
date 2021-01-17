from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import DetailView,UpdateView, DeleteView, View
from django.http import Http404, HttpResponse,HttpResponseRedirect




def index(request):
    return render(request, 'main/master.html')


def instruction(request):
    return render(request, 'main/instruction.html')


def first(request):
    get_items = ItemNewOne.objects.all()
    get_folds = FoldNewOne.objects.all()


    return render(request, 'main/first.html', {'title':"Сводный отчет",
                                               'get_item': get_items,'get_fold': get_folds})


def second(request):
    items = ItemNewOne.objects.all()
    return render(request, 'main/second.html', {'title':"Вторая страница сайта", 'item': items})


def item_list(request):
    items = ItemNewOne.objects.all()
    return render(request, 'main/item_full_list.html', {'title':"Информация о товарах", 'item': items})


def fold_list(request):
    folds = FoldNewOne.objects.all()
    return render(request, 'main/fold_full_list.html', {'title':"Информация о складах", 'fold': folds})


def third(request):
    #warehouses = WareHouse.objects.find() - найти объект по его айди order - сортировка
    warehouses = FoldNewOne.objects.all()
    return render(request, 'main/third.html', {'title':"Третья страница сайта", 'warehouses': warehouses})


class FoldCreate(View):
    def get(self,request):
        form = NewFoldCreateForm()
        return render(request, 'main/new_fold_create.html',{'form' : form})

    def post(self, request):
        post_form = NewFoldCreateForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('/folds')
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
            return redirect('/items')
        else:
            return render(request, 'main/new_item_create.html',{'form' : post_form})


def folds_home(request):
    warehouses = FoldNewOne.objects.all()
    return render(request, 'main/folds_home.html', {'title': "Склады", 'warehouses': warehouses})


def items_home(request):
    items = ItemNewOne.objects.all()
    return render(request, 'main/items_home.html', {'title': "Товары", 'item': items})

"""def createitem(request):
    error = ''
    if request.method == 'POST':
        form = ItemCreateTestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/items')
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
            return redirect('/folds')
        else:
            error = 'Данные на форме неверны!'

    form = WareHouseCreateForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create_fold.html', context)

"""
"""class FoldUpdate(View):
    def get(self,request):
        fold = FoldNew.objects.get(id__iexact=self.id)
        bound_form=NewFoldCreateForm(instance=fold)
        return render(request, 'main/update_new_fold.html', context={'form': bound_form, 'folds': fold})
"""

class FoldDetailView(DetailView):
    model = FoldNewOne
    template_name = 'main/fold_detail.html'
    context_object_name = 'folds'


class FoldUpdateView(UpdateView):
    model = FoldNewOne
    template_name = 'main/update_new_fold.html'

#    form_class = NewFoldCreateForm
    form_class = NewFoldUpdateForm


class FoldDeleteView(DeleteView):
    model = FoldNewOne
    #form_class = NewFoldUpdateForm
    success_url = '/folds'
    template_name = 'main/delete_fold.html'


class ItemDetailView(DetailView):
    model = ItemNewOne
    template_name = 'main/item_detail.html'
    context_object_name = 'items'


class ItemUpdateView(UpdateView):
    model = ItemNewOne
    template_name = 'main/update_new_item.html'

    form_class = NewItemUpdateForm


class ItemDeleteView(DeleteView):
    model = ItemNewOne
    success_url = '/items'
    template_name = 'main/delete_new_item.html'

#    form_class = WareHouseCreateForm



