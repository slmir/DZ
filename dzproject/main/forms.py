from .models import Fold, Item
from django.forms import ModelForm, TextInput, Textarea, Select
from django.core.exceptions import ValidationError


class WareHouseCreateForm(ModelForm):
    class Meta:
        model = Fold
        fields = ["name", "parknumber", "responsible"]
        widgets = {
            "name": TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите название склада'
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
        if Fold.objects.filter(FoldName__iexact=new_name).count():
            raise ValidationError('Название склада должно быть уникальным. В записях уже существует склад "{}"'.format(new_name))

        return new_name


class ItemCreateTestForm(ModelForm):
    class Meta:
        model = Item
        folds = Fold.objects.all()
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