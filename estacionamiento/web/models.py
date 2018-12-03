from django.db import models
from django.urls import reverse

# Create your models here.

class Administrador(models.Model):
    admin = models.AutoField(primary_key=True)
    usuario = models.CharField('nombre de usuario', max_length=30)
    nombres = models.CharField(max_length=30)
    a_paterno = models.CharField('apellido paterno', max_length=30)
    a_materno = models.CharField('apellido materno', max_length=30, blank = True)
    password = models.CharField('contraseña', max_length=30)

class Usuario(models.Model):
    TIPOS_USUARIO = (
        (1, 'Docente'),
        (2, 'Administrativo'),
        (3, 'Alumno'),
        (4, 'Directivo'),
    )
    user = models.AutoField(primary_key=True)
    num_id = models.CharField('número identificador', max_length=30,unique=True)
    usuario = models.CharField('nombre de usuario', max_length=30)
    nombres = models.CharField('nombres', max_length=30)
    a_paterno = models.CharField('apellido paterno', max_length=30)
    a_materno = models.CharField('apellido materno', max_length=30, blank = True)
    password = models.CharField('contraseña', max_length=30)
    telefono = models.CharField(max_length=30)
    tipo_usuario = models.IntegerField(choices=TIPOS_USUARIO)
    discapacitado = models.BooleanField(default=False)
    activo = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('user-detail', kwargs={'pk': self.user})

class Cajon(models.Model):
    ESTACIONAMIENTOS = (
        (1, 'PRINCIPAL'),
        (2, 'TRASERO'),
        (3, 'DISCAPACITADOS PRINCIPAL'),
        (4, 'DISCAPACITADOS TRASERO'),
    )
    cajon = models.AutoField(primary_key=True)
    num_cajon = models.IntegerField('numero de cajón')
    horario_entrada = models.DateTimeField()
    horario_salida = models.DateTimeField()
    disponible = models.BooleanField(default=True)
    num_estacionamiento = models.IntegerField(choices=ESTACIONAMIENTOS)

class Automovil(models.Model):
    VEHICULOS = (
        ('MT', 'Motocicleta'),
        ('AU', 'Automovil'),
        ('CM', 'Camioneta'),
        ('VN', 'Van'),
        ('OT', 'Otros'),
    )
    placa = models.CharField(primary_key=True, max_length=8)
    modelo = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    tipo_vehiculo = models.CharField('tipo de vehiculo', max_length=2, choices=VEHICULOS)
    marca = models.CharField(max_length=15)

class LugarAsignado(models.Model):
    lugar = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    id_cajon = models.ForeignKey('Cajon',on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField('horario de entrada')
    horario_salida = models.DateTimeField('horario de salida')
    id_vehiculo_1 = models.ForeignKey('Automovil',on_delete=models.CASCADE, related_name='fk_vehiculo1_lugar')
    id_vehiculo_2 = models.ForeignKey('Automovil',on_delete=models.SET_NULL, null=True, blank=True, related_name='fk_vehiculo2_lugar')

class Solicitud(models.Model):
    solicitud = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    horario_entrada = models.DateTimeField('horario de entrada')
    horario_salida = models.DateTimeField('horario de salida')
    id_vehiculo_1 = models.ForeignKey('Automovil',on_delete=models.CASCADE, related_name='fk_vehiculo1_sol')
    id_vehiculo_2 = models.ForeignKey('Automovil',on_delete=models.SET_NULL, null=True, blank=True, related_name='fk_vehiculo2_sol')
    aprovada = models.BooleanField(default=False)

class Sancion(models.Model):
    sancion = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey('Administrador', null=True, on_delete=models.SET_NULL)
    id_usuario = models.ForeignKey('Usuario',on_delete=models.CASCADE)
    razon = models.TextField()
    fecha = models.DateTimeField('fecha de la sanción')
    fecha_inicio = models.DateTimeField('fecha de inicio')
    fecha_termino = models.DateTimeField('fecha de termino')