from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "tagcss","tagulol","tagmarginmargin","tagssilka","tagbackground","tagregistr","tagclassred","tagtr","tagmarginpadding","tagdivspan","tagimage"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagcss": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagulol": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagmarginmargin": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagssilka": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagbackground": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagregistr": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagclassred": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagtr": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagmarginpadding": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagdivspan": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            }),
            "tagimage": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите Текст'
            })

        }
