from django.db import models

# Create your models here.
class Autores(models.Model):
    id_autor = models.AutoField(primary_key = True)
    apellidos = models.CharField(max_length = 25, blank = False, null = False)
    nombres = models.CharField(max_length = 25, blank = False, null = False)

    class Meta: 
        ordering = ['id_autor']
    
    def __str__(self):
        return self.nombres + " " + self.apellidos
     

class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key =True)
    categoria = models.CharField(max_length = 50, blank = False, null = False)

    class Meta:
        ordering = ['id_categoria']
    
    def __str__(self):
        return '{} - {}'.format(
            self.id_categoria,
            self.categoria
        )

class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key = True)
    identificacion = models.CharField(max_length = 12, blank = False, null = False)
    nombres = models.CharField(max_length = 25, blank = False, null = False)
    apellidos = models.CharField(max_length = 25, blank = False, null = False)
    telefono = models.CharField(max_length = 12, blank = False, null = False)
    direccion = models.CharField(max_length = 128, blank = False, null = False)
    correo_electronico = models.EmailField(max_length = 128, blank = False, null = False)

    class Meta:
        ordering = ['id_cliente']
    
    def __str__(self):
        return '{} - {} - {} - {} - {} - {}'.format(
            self.id_cliente,
            self.identificacion,
            self.nombres,
            self.apellidos,
            self.telefono,
            self.correo_electronico
        )
    
    
class Libros(models.Model):
    isbn = models.IntegerField(primary_key = True)
    titulo = models.CharField(max_length = 128, blank = False, null = False)
    fecha_pub = models.DateField( blank = False, null = False)
    fecha_creacion = models.DateField(auto_now=True, auto_now_add=False)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    precio = models.IntegerField(blank = False, null = False)
    portada = models.ImageField(upload_to='portada/', blank = True, null = True, default = '')
    id_autor = models.ManyToManyField(Autores)

    class Meta:
        ordering = ['fecha_creacion']
    
    def __str__(self):
        return '{} - {} - {}'.format(
            self.isbn,
            self.titulo,
            self.precio
        )


class PedidosCliente(models.Model):
    id_pedido = models.AutoField(primary_key = True)
    nro_pedido = models.CharField(max_length = 255, unique = True, blank = False, null = False)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    isbn = models.ForeignKey(Libros, on_delete=models.CASCADE)
    fecha_pedido = models.DateField(auto_now=True, auto_now_add=False)
    cantidad = models.IntegerField()
    valor = models.IntegerField()
    
    class Meta:
        ordering = ['id_pedido']
    

    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(
            self.nro_pedido,
            self.id_cliente,
            self.isbn,
            self.cantidad,
            self.valor
        )

    
    
    
    
    
    
     
    
    
    
    
     