from django.core.management.base import BaseCommand, CommandError
from back.models import Producto, Categoria, Tienda, Boleta, Contacto, Pedido


class Command(BaseCommand):
    help = "Crear productos de ejemplo"

    def handle(self, *args, **options):
        Tienda.objects.all().delete()
        Categoria.objects.all().delete()
        Producto.objects.all().delete()
        Boleta.objects.all().delete()
        Contacto.objects.all().delete()
        Pedido.objects.all().delete()
        
        tiendas_datos = [
            {
                'nombre': 'Ferremas Las Condes',
                'direccion': 'Av. Las Condes 12422, 7710162 Santiago, Lo Barnechea, Región Metropolitana',
            },
            {
                'nombre': 'Ferremas Estacion Central',
                'direccion': 'San Francisco de Borja 402, 9160005 Santiago, Estación Central, Región Metropolitana',
            }
        ]

        tienda_objetos = [Tienda(**datos) for datos in tiendas_datos]
        Tienda.objects.bulk_create(tienda_objetos)

        for tienda in tienda_objetos:
            tienda.save()

        categoria_datos = [
            {
                'nombre': 'Herramientas Manuales'
            },
            {
                'nombre': 'Materiales Basicos'
            },
            {
                'nombre': 'Equipos de Seguridad'
            },
            {
                'nombre': 'Tornillos y Anclajes'
            },
            {
                'nombre': 'Fijaciones y Adhesivos'
            },
            {
                'nombre': 'Equipos de Medición'
            }
        ]

        categoria_objetos = [Categoria(**datos) for datos in categoria_datos]
        categoria_objetos = Categoria.objects.bulk_create(categoria_objetos)

        for categoria in categoria_objetos:
            categoria.save()

        productos_datos = [
            {
                'codigo': '0QMB-73NV',
                'marca': 'REDLINE',
                'nombre': 'Martillo carpintero 24 Oz acero',
                'stock': '5',
                'categoria_id': categoria_objetos[0].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '13480',
                'imagen': './martillo.avif'
            },
            {
                'codigo': '9SE9-BJRA',
                'marca': 'STANLEY',
                'nombre': 'Set de destornilladores acero 6 unidades',
                'stock': '7',
                'categoria_id': categoria_objetos[0].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '10990',
                'imagen': './destornillador.avif'
            },
            {
                'codigo': 'O680-8MDQ',
                'marca': 'TOTAL TOOLS',
                'nombre': 'Llave Francesa Ajustable 12 Pulgadas',
                'stock': '5',
                'categoria_id': categoria_objetos[0].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '10500',
                'imagen': './llave.webp'
            },
            {
                'codigo': '9BZN-5GR5',
                'marca': 'BAUKER',
                'nombre': 'Taladro inalámbrico percutor 10 mm 12V',
                'stock': '9',
                'categoria_id': categoria_objetos[0].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '42990',
                'imagen': './taladro.avif'
            },
            {
                'codigo': 'DKC6-MRMT',
                'marca': 'BAUKER',
                'nombre': 'Sierra circular eléctrica 7 1/4" 1300W',
                'stock': '4',
                'categoria_id': categoria_objetos[0].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '39990',
                'imagen': './sierra.avif'
            }
        ]
        producto_objetos = [Producto(**datos) for datos in productos_datos]
        Producto.objects.bulk_create(producto_objetos)