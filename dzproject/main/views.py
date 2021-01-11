from django.shortcuts import render, redirect
from .models import Fold, Item
from .forms import WareHouseCreateForm, ItemCreateTestForm
from django.views.generic import DetailView,UpdateView, DeleteView
from django.db.models import F
from django.http import HttpResponse,HttpResponseRedirect


def index(request):
    return render(request, 'main/master.html')


def first(request):
    get_items = Item.objects.all()
    get_folds = Fold.objects.all()


    return render(request, 'main/first.html', {'title':"Примерный сводный отчет",
                                               'get_item': get_items,'get_fold': get_folds})


def second(request):
    items = Item.objects.all()
    return render(request, 'main/second.html', {'title':"Вторая страница сайта", 'item': items})


def third(request):
    #warehouses = WareHouse.objects.find() - найти объект по его айди order - сортировка
    warehouses = Fold.objects.all()
    return render(request, 'main/third.html', {'title':"Третья страница сайта", 'warehouses': warehouses})


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


def folds_home(request):
    items = Fold.objects.all()
    return render(request, 'main/folds_home.html', {'title': "Складыю. Главная", 'items': items})


class FoldDetailView(DetailView):
    model = Fold
    template_name = 'main/fold_detail.html'
    context_object_name = 'folds'


class FoldUpdateView(UpdateView):
    model = Fold
    template_name = 'main/update_fold.html'

    form_class = WareHouseCreateForm


class FoldDeleteView(DeleteView):
    model = Fold
    success_url = '/third'
    template_name = 'main/delete_fold.html'

    form_class = WareHouseCreateForm

