from django import forms
from .models import *
from django.forms import ModelForm, TextInput, Textarea, Select
from django.core.exceptions import ValidationError
import datetime

class NewFoldCreateForm(forms.ModelForm):
    class Meta:
        model = FoldNewOne
        fields = ["name", "parknumber", "responsible", "adress", "square"]
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
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес склада (необязательно)'
            }),
            "square": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите площадь склада'
            }),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name']

        if new_name == 'create':
            raise ValidationError('Запись о складе с таким именем не может быть создана!')
        if FoldNewOne.objects.filter(name__iexact=new_name).count():
            raise ValidationError(
                'Название склада должно быть уникальным. В записях уже существует склад "{}"'.format(new_name))

        return new_name

    def clean_parknumber(self):
        new_parknumber = self.cleaned_data['parknumber']

        if new_parknumber <= 0:
            raise ValidationError('Запись о номере платформы разгрузки должна быть целым неотрицательным числом!')

        return new_parknumber

    def clean_square(self):
        new_square = self.cleaned_data['square']

        if new_square <= 0:
            raise ValidationError('Запись о площади склада должна быть целым неотрицательным числом!')

        return new_square


class NewFoldUpdateForm(forms.ModelForm):
    class Meta:
        model = FoldNewOne
        fields = ["name", "parknumber", "responsible", "adress", "square"]
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
            "adress": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите адрес склада (необязательно)'
            }),
            "square": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите площадь склада'
            }),
        }

    def clean_name(self):
        new_name = self.cleaned_data['name']

        if new_name == 'create':
            raise ValidationError('Запись о складе с таким именем не может быть создана!')

        return new_name

    def clean_parknumber(self):
        new_parknumber = self.cleaned_data['parknumber']

        if new_parknumber <= 0:
            raise ValidationError('Запись о номере платформы разгрузки должна быть целым неотрицательным числом!')

        return new_parknumber

    def clean_square(self):
        new_square = self.cleaned_data['square']

        if new_square <= 0:
            raise ValidationError('Запись о площади склада должна быть целым неотрицательным числом!')

        return new_square



class NewItemCreateForm(forms.ModelForm):
    class Meta:
        model = ItemNewOne
        folds = FoldNewOne.objects.all()
        category = (
            ('Мебель'),
            ('Стройматериалы'),
            ('Инструменты'),
            ('Техника'),
        )

        moduls = (
            ('А'),
            ('Б'),
            ('В'),
            ('Г'),
            ('Д'),
            ('Е'),
            ('Ж'),
            ('З'),
        )

        sections = (
            ('S-1'),
            ('S-2'),
            ('S-3'),
            ('S-4'),
            ('S-5'),
            ('S-6'),
            ('S-7'),
            ('S-8'),
            ('S-9'),
            ('S-10'),
            ('S-11'),
            ('S-12'),
            ('S-13'),
            ('S-14'),
            ('S-15'),
            ('S-16'),
        )

        rows = (
            ('1'),
            ('2'),
            ('3'),
            ('4'),
            ('5'),
            ('6'),
            ('7'),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16'),
            ('17'),
            ('18'),
            ('19'),
            ('20'),
            ('21'),
            ('22'),
            ('23'),
            ('24'),
            ('25'),
            ('26'),
            ('27'),
            ('28'),
            ('29'),
            ('30'),
            ('31'),
            ('32'),
        )

        places = (
            ('М0'),
            ('М1'),
            ('М2'),
            ('М3'),
            ('М4'),
            ('М5'),
            ('М6'),
            ('М7'),
            ('М8'),
            ('М9'),
            ('М10'),
            ('М11'),
            ('М12'),
            ('М13'),
            ('М14'),
            ('М15'),
            ('М16'),
            ('М17'),
            ('М18'),
            ('М19'),
            ('М20'),
            ('М21'),
            ('М22'),
            ('М23'),
            ('М24'),
            ('М25'),
            ('М26'),
            ('М27'),
            ('М28'),
            ('М29'),
            ('М30'),
            ('М31'),
            ('М32'),
            ('М33'),
            ('М34'),
            ('М35'),
            ('М36'),
            ('М37'),
            ('М38'),
            ('М39'),
            ('М40'),
            ('М41'),
            ('М42'),
            ('М43'),
            ('М44'),
            ('М45'),
            ('М46'),
            ('М47'),
            ('М48'),
            ('М49'),
            ('М50'),
            ('М51'),
            ('М52'),
            ('М53'),
            ('М54'),
            ('М55'),
            ('М56'),
            ('М57'),
            ('М58'),
            ('М59'),
            ('М60'),
            ('М61'),
            ('М62'),
            ('М63'),
            ('М64'),
            ('М65'),
            ('М66'),
            ('М67'),
            ('М68'),
            ('М69'),
            ('М70'),
            ('М71'),
            ('М72'),
            ('М73'),
            ('М74'),
            ('М75'),
            ('М76'),
            ('М77'),
            ('М78'),
            ('М79'),
            ('М80'),
            ('М81'),
            ('М82'),
            ('М83'),
            ('М84'),
            ('М85'),
            ('М86'),
            ('М87'),
            ('М88'),
            ('М89'),
            ('М90'),
            ('М91'),
            ('М92'),
            ('М93'),
            ('М94'),
            ('М95'),
            ('М96'),
            ('М97'),
            ('М98'),
            ('М99'),
            ('М100'),
            ('М101'),
            ('М102'),
            ('М103'),
            ('М104'),
            ('М105'),
            ('М106'),
            ('М107'),
            ('М108'),
            ('М109'),
            ('М110'),
            ('М111'),
            ('М112'),
            ('М113'),
            ('М114'),
            ('М115'),
            ('М116'),
            ('М117'),
            ('М118'),
            ('М119'),
            ('М120'),
            ('М121'),
            ('М122'),
            ('М123'),
            ('М124'),
            ('М125'),
            ('М126'),
            ('М127'),
            ('М128'),
        )

        fields = ['name', 'category', 'amount', 'shelflifeday', 'option', 'foldid', 'module', 'section', 'row', 'place']
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
            "module": Select(attrs={
            'class': 'form-control',
            'placeholder': 'Выбирете модуль склада'
            }, choices=moduls),
            "section": Select(attrs={
            'class': 'form-control',
            'placeholder': 'Выбирете модуль склада'
            }, choices=sections),
            "row": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете модуль склада'
            }, choices=rows),
            "place": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете модуль склада'
            }, choices=places),
        }


    def clean_name(self):
        new_name = self.cleaned_data['name']

        if new_name == 'create':
            raise ValidationError('Запись о складе с таким именем не может быть создана!')
        if ItemNewOne.objects.filter(name__iexact=new_name).count():
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




class NewItemUpdateForm(forms.ModelForm):

    class Meta:
        model = ItemNewOne
        folds = FoldNewOne.objects.all()
        category = (
            ('Мебель'),
            ('Стройматериалы'),
            ('Инструменты'),
            ('Техника'),
        )

        moduls = (
            ('А'),
            ('Б'),
            ('В'),
            ('Г'),
            ('Д'),
            ('Е'),
            ('Ж'),
            ('З'),
        )

        sections = (
            ('S-1'),
            ('S-2'),
            ('S-3'),
            ('S-4'),
            ('S-5'),
            ('S-6'),
            ('S-7'),
            ('S-8'),
            ('S-9'),
            ('S-10'),
            ('S-11'),
            ('S-12'),
            ('S-13'),
            ('S-14'),
            ('S-15'),
            ('S-16'),
        )

        rows = (
            ('1'),
            ('2'),
            ('3'),
            ('4'),
            ('5'),
            ('6'),
            ('7'),
            ('8'),
            ('9'),
            ('10'),
            ('11'),
            ('12'),
            ('13'),
            ('14'),
            ('15'),
            ('16'),
            ('17'),
            ('18'),
            ('19'),
            ('20'),
            ('21'),
            ('22'),
            ('23'),
            ('24'),
            ('25'),
            ('26'),
            ('27'),
            ('28'),
            ('29'),
            ('30'),
            ('31'),
            ('32'),
        )

        places = (
            ('М0'),
            ('М1'),
            ('М2'),
            ('М3'),
            ('М4'),
            ('М5'),
            ('М6'),
            ('М7'),
            ('М8'),
            ('М9'),
            ('М10'),
            ('М11'),
            ('М12'),
            ('М13'),
            ('М14'),
            ('М15'),
            ('М16'),
            ('М17'),
            ('М18'),
            ('М19'),
            ('М20'),
            ('М21'),
            ('М22'),
            ('М23'),
            ('М24'),
            ('М25'),
            ('М26'),
            ('М27'),
            ('М28'),
            ('М29'),
            ('М30'),
            ('М31'),
            ('М32'),
            ('М33'),
            ('М34'),
            ('М35'),
            ('М36'),
            ('М37'),
            ('М38'),
            ('М39'),
            ('М40'),
            ('М41'),
            ('М42'),
            ('М43'),
            ('М44'),
            ('М45'),
            ('М46'),
            ('М47'),
            ('М48'),
            ('М49'),
            ('М50'),
            ('М51'),
            ('М52'),
            ('М53'),
            ('М54'),
            ('М55'),
            ('М56'),
            ('М57'),
            ('М58'),
            ('М59'),
            ('М60'),
            ('М61'),
            ('М62'),
            ('М63'),
            ('М64'),
            ('М65'),
            ('М66'),
            ('М67'),
            ('М68'),
            ('М69'),
            ('М70'),
            ('М71'),
            ('М72'),
            ('М73'),
            ('М74'),
            ('М75'),
            ('М76'),
            ('М77'),
            ('М78'),
            ('М79'),
            ('М80'),
            ('М81'),
            ('М82'),
            ('М83'),
            ('М84'),
            ('М85'),
            ('М86'),
            ('М87'),
            ('М88'),
            ('М89'),
            ('М90'),
            ('М91'),
            ('М92'),
            ('М93'),
            ('М94'),
            ('М95'),
            ('М96'),
            ('М97'),
            ('М98'),
            ('М99'),
            ('М100'),
            ('М101'),
            ('М102'),
            ('М103'),
            ('М104'),
            ('М105'),
            ('М106'),
            ('М107'),
            ('М108'),
            ('М109'),
            ('М110'),
            ('М111'),
            ('М112'),
            ('М113'),
            ('М114'),
            ('М115'),
            ('М116'),
            ('М117'),
            ('М118'),
            ('М119'),
            ('М120'),
            ('М121'),
            ('М122'),
            ('М123'),
            ('М124'),
            ('М125'),
            ('М126'),
            ('М127'),
            ('М128'),
        )

        fields = ['name', 'category', 'amount', 'shelflifeday', 'option', 'foldid', 'module', 'section',
                  'row', 'place']
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
            "module": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете модуль склада'
            }, choices=moduls),
            "section": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете модуль склада'
            }, choices=sections),
            "row": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете модуль склада'
            }, choices=rows),
            "place": Select(attrs={
                'class': 'form-control',
                'placeholder': 'Выбирете модуль склада'
            }, choices=places),
        }


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

