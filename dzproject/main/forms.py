from django import forms
from .models import FoldNew, ItemNew
from django.forms import ModelForm, TextInput, Textarea, Select
from django.core.exceptions import ValidationError


class WareHouseCreateForm(ModelForm):
    class Meta:
        model = FoldNew
        fields = ["name", "parknumber", "responsible"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название склада'
            }),
            "parknumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер платформы'
            }),
            "responsible": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО ответственного (необязательно)'
            }),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name']

        if new_name == 'создать':
            raise ValidationError('Запись о складе с таким именем не может быть создана!')
        if FoldNew.objects.filter(name__iexact=new_name).count():
            raise ValidationError(
                'Название склада должно быть уникальным. В записях уже существует склад "{}"'.format(new_name))

        return new_name


class ItemCreateTestForm(ModelForm):
    class Meta:
        model = ItemNew
        folds = FoldNew.objects.all()
        category = (
            ('Мебель'),
            ('Стройматериалы'),
            ('Инструменты'),
            ('Техника'),
        )
        fields = ['name', 'category', 'amount', 'shelflifeday', 'option', 'foldid']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование товара'
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите категорию'
            }, choices=category),
            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество (шт.)'
            }),
            "shelflifeday": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите срок хранения (дней)'
            }),
            "option": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание (необязательно)'
            }),
            "foldid": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете склад'
            }, choices=folds),

        }


class NewFoldCreateForm(forms.ModelForm):
    class Meta:
        model = FoldNew
        fields = ["name", "parknumber", "responsible"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название склада'
            }),
            "parknumber": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер платформы'
            }),
            "responsible": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ФИО ответственного (необязательно)'
            }),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name']

        if new_name == 'create':
            raise ValidationError('Запись о складе с таким именем не может быть создана!')
        if FoldNew.objects.filter(name__iexact=new_name).count():
            raise ValidationError(
                'Название склада должно быть уникальным. В записях уже существует склад "{}"'.format(new_name))

        return new_name

    def clean_parknumber(self):
        new_parknumber = self.cleaned_data['parknumber']

        if new_parknumber <= 0:
            raise ValidationError('Запись о номере платформы разгрузки должна быть целым неотрицательным числом!')

        return new_parknumber


"""
class NewItemCreateForm(forms.Form):
    folds = FoldNew.objects.all()
    new_fold_list = [(1, '--------')]
    for i in folds:
        new_fold_list.append((i.id, i.name))

    category = (
        ('1', '--------'),
        ('2','Мебель'),
        ('3','Стройматериалы'),
        ('4','Инструменты'),
        ('5','Техника'),
    )
    name = forms.CharField(max_length=50)
    cat = forms.ChoiceField(choices=category)
    amount = forms.IntegerField()
    days = forms.IntegerField()
    option = forms.CharField()
    foldid = forms.ChoiceField(choices=new_fold_list)

    name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите наименование товара'})
    cat.widget.attrs.update({'class': 'form-control', 'placeholder': 'Выберите категорию'})
    amount.widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите количество'})
    days.widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите количество дней хранения'})
    option.widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите описание (необязательно)'})
    foldid.widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите склад'})
    class Meta:
        model = FoldNew
        fields = ['name', 'parknumber', 'responsible']

        widgets = {
            'name': forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название склада',
            }),
            'parknumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер платформы разгрузки'}),
            'responsible': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите ФИО управляющего (неообязательно)'}),
        }
"""
class NewItemCreateForm(forms.ModelForm):
    class Meta:
        model = ItemNew
        folds = FoldNew.objects.all()
        category = (
            ('Мебель'),
            ('Стройматериалы'),
            ('Инструменты'),
            ('Техника'),
        )
        fields = ['name', 'category', 'amount', 'shelflifeday', 'option', 'foldid']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование товара'
            }),
            "category": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выберите категорию'
            }, choices=category),
            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество (шт.)'
            }),
            "shelflifeday": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите срок хранения (дней)'
            }),
            "option": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание (необязательно)'
            }),
            "foldid": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете склад'
            }, choices=folds),

        }


    def clean_name(self):
        new_name = self.cleaned_data['name']

        if new_name == 'create':
            raise ValidationError('Запись о складе с таким именем не может быть создана!')
        if ItemNew.objects.filter(name__iexact=new_name).count():
            raise ValidationError(
                'Наименование товара должно быть уникальным. В записях уже существует товар "{}"'.format(
                    new_name))

        return new_name


    def clean_amount(self):
        new_amount = self.cleaned_data['amount']

        if new_amount <= 0:
            raise ValidationError('Запись о количестве товара должна быть целым неотрицательным числом!')

        return new_amount

    def clean_shelflifeday(self):
        new_days = self.cleaned_data['shelflifeday']

        if new_days <= 0:
            raise ValidationError('Запись о количестве дней хранения должна быть целым неотрицательным числом!')

        return new_days




