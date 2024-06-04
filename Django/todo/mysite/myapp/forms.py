from .models import Task
from django import forms

# Create your models here.
class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name','priority','date']