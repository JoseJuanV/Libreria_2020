from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username, nombre, apellido, password = None):
        if not email: 
            raise ValueError('El usuario debe tener un correo Electrónico')
        
        user = self.model(
            username = username,
            email = email,
            nombre = nombre,
            apellido = apellido
        )

        user.set_password(password)
        user.save()

        return user 
    
    def create_superuser(self, username, email, nombre, apellido, password):
        
        user = self.create_user(
            email,
            username = username,
            nombre = nombre,
            apellido = apellido,
            password = password 
        )
        
        user.usuario_administrador = True 
        user.save()
        
        return user 


class Usuario(AbstractBaseUser):
    nombre = models.CharField(max_length = 150)
    apellido = models.CharField(max_length = 150)
    email = models.EmailField(max_length=150, unique = True)
    username = models.CharField(max_length = 150, unique = True)
    imagen = models.ImageField(upload_to = 'perfil/', max_length=100, default = 'perfil/avatar.png')
    usuario_activo = models.BooleanField(default = True)
    usuario_administrador = models.BooleanField(default = False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'username' 
    REQUIRED_FIELDS = ['email', 'nombre', 'apellido'] 

    def __str__(self):
        return f'{self.nombre} {self.apellido}' 
    
    def has_perm(self, perm, obj = None):
        """Este metodo es llamado por el administrador de Django, 
        para otorgar el permiso de entrar al administrador de Django"""
        return True 
    
    def has_module_perms(self, app_label): 
        """Tambien es para el administrador de Django, recibe app_label
        que basicamente dice en que aplicacion esta situado nuestro modelo Usuario"""
        return True 
    

    @property
    def is_staff(self):
        return self.usuario_administrador 
    
    
    
    
    