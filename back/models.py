from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime   

class CustomUser(AbstractUser):
    class Types(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        VENDEDOR = "VENDEDOR", "Vendedor"
        BODEGUERO = "BODEGUERO", "Bodeguero"
        CONTADOR = "CONTADOR", "Contador"
        CLIENTE = "CLIENTE", "Cliente"

    type = models.CharField(
        max_length=20, choices=Types.choices, default=Types.ADMIN
    )

    email = models.EmailField(unique=True, max_length=50)
    username = models.CharField(max_length=20)

    note = models.TextField(max_length=200, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    

# Para el retiro en tienda
class Tienda(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
    

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    marca = models.CharField(max_length=100)
    nombre = models.CharField(max_length=200)
    stock = models.IntegerField(default=0)
    imagen = models.ImageField(null=True, default=None)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE)
    valor = models.FloatField()

    def __str__(self):
        return self.nombre
    

class Boleta(models.Model):
    buy_order = models.CharField(max_length=10, unique=True, null=True, default=None)
    fecha = models.DateTimeField(auto_now_add=True)
    valor_total = models.FloatField()
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    direccion_entrega = models.CharField(max_length=200)
    tienda_entrega = models.ForeignKey(Tienda, on_delete=models.CASCADE, null=True, default=None)
    es_carrito = models.BooleanField(default=True)
    pagado = models.BooleanField(default=False)

    def __str__(self):
        return self.id
    

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre
    

class Pedido(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, null=True, default=None, related_name='pedidos')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    valor_total = models.FloatField()

    def __str__(self):
        return str(self.id)
    
class Factura(models.Model):
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE, null=True, default=None, related_name='factura')
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    rut = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    direccion2 = models.CharField(max_length=200, null=True, blank=True)
    envio = models.IntegerField(null=True)
    fecha = models.DateField(auto_now=True, blank=True)

    def __str__(self):
        return self.nombre