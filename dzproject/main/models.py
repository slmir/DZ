from django.db import models
from django.shortcuts import reverse


class FoldNew(models.Model):
    name = models.CharField('Название склада', max_length=50)
    parknumber = models.IntegerField('Номер платформы')
    responsible = models.CharField('Ответственный', max_length=50, blank=True)

    def __str__(self):
        return str(self.name)

    def get_item_count(self):
        count = 0
        items = ItemNew.objects.all()
        for i in items:
            if i.foldid.id == self.id:
                count += 1
        return count

    def get_id(self):
        return self.id

    def get_absolute_url(self):
        return f'/folds/{self.id}'

    """def get_update_url(self):
        return reverse('fold_update_url',kwargs={'id': self.id})
"""
    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'


class ItemNew(models.Model):
    __original_name = None
    ITEM_CATEGORY = (
        ('Мебель', 'Мебель'),
        ('Стройматериалы', 'Строительные материалы'),
        ('Инструменты', 'Инструменты для выполнения строительных,отделочных работ'),
        ('Техника', 'Технические средства, машины для строительных, отделочных работ'),
    )
    name = models.CharField('Наименование товара', max_length=100)
    category = models.CharField('Категория', max_length=50, choices=ITEM_CATEGORY)
    amount = models.IntegerField('Количество')
    shelflifeday = models.IntegerField('Дней хранения')
    option = models.TextField('Описание', blank=True)
    foldid = models.ForeignKey(FoldNew, on_delete=models.CASCADE, verbose_name="Склад", blank="True")

    def __init__(self, *args,**kwargs):
        super(ItemNew,self).__init__(*args,**kwargs)
        self.__original_name = self.name

    def __str__(self):
        return 'Наименование товара: ' + str(self.name) + '; Категория: ' + str(self.category)

    def get_id(self):
        return self.foldid.id

    def get_name(self):
        return self.name

    def get_absolute_url(self):
        return f'/items/{self.id}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
