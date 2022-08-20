from django.forms import ModelForm
from ToDo_App.models import ToDo


class ToDoforms(ModelForm):
    class Meta:
      model = ToDo
      fields = [ 'title','status','priority']