from django.forms import ModelForm
from django.forms import modelformset_factory
from django import forms
from models import Usuario

class NewUserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Usuario
        fields = ('num_id','usuario','nombres','a_paterno','a_materno','password','telefono','tipo_usuario', 'discapacitado')

NewUserFormSet = modelformset_factory(Usuario, form=NewUserForm)
