from django.db import models

class Task(models.Model):
    title = models.TextField('Имя_Фамилия', max_length=500)
    task = models.TextField('Что такое HTML?', max_length=500)
    tagcss = models.TextField('Что такое CSS?', max_length=500)
    tagulol = models.TextField('Как сделать Ненумерованный список в нумерованном?Написать тегами', max_length=500)
    tagmarginmargin = models.TextField('Какая разница между значениями margin 10px и margin 10px 10px в свойстве margin?',max_length=500)
    tagssilka = models.TextField('Ссылки. Как задать адрес документа, на который следует перейти? Написать тегом',max_length=500)
    tagbackground = models.TextField('Какое свойство задает цвет заднего фона?', max_length=500)
    tagregistr = models.TextField('В каком регистре лучше писать HTML-код?', max_length=500)
    tagclassred = models.TextField('Как задать красный цвет для всех элементов, имеющих класс red?', max_length=500)
    tagtr = models.TextField('Зачем нужнeн тег tr', max_length=500)
    tagmarginpadding = models.TextField('В чем разница между margin и padding?', max_length=500)
    tagdivspan = models.TextField('В чем разница между div и span?', max_length=500)
    tagimage = models.TextField('Как добавить картинку на страницу?написать тегом', max_length=500)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

