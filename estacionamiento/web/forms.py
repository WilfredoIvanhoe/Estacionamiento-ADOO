from django.forms import ModelForm
from django.forms import modelformset_factory
from models import Usuario

class NewUserForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ('num_id','usuario','nombres','a_paterno','a_materno','password','telefono','tipo_usuario', 'discapacitado')

NewUserFormSet = modelformset_factory(Usuario, form=NewUserForm)
