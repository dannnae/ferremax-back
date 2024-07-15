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

        for categoria in categoria_objetos:
            categoria.save()

        productos_datos = [
            # Categoria herramientas manuales
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
                'codigo': 'DWC6-MR31',
                'marca': 'BAUKER',
                'nombre': 'Sierra circular eléctrica 7 1/4" 1300W',
                'stock': '6',
                'categoria_id': categoria_objetos[0].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '39990',
                'imagen': './sierra.avif'
            },

            # Categoria herramientas basicas
        
            {
                'codigo': '7ZC1-ZTA7',
                'marca': 'POLPAICO',
                'nombre': 'Cemento Polpaico 25 kilos',
                'stock': '7',
                'categoria_id': categoria_objetos[1].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '3690',
                'imagen': './cemento.avif'
            },

            {
                'codigo': 'K2Z3-4RRT',
                'marca': 'CERAMICAS SANTIAGO',
                'nombre': '29x14x9.4 cm Ladrillo 9 Súper',
                'stock': '100',
                'categoria_id': categoria_objetos[1].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '890',
                'imagen': './ladrillo.avif'
            },

            {
                'codigo': 'N22M-UA90',
                'marca': 'KOLOR',
                'nombre': 'Esmalte al agua standard interior semibrillo blanco 1 galón',
                'stock': '10',
                'categoria_id': categoria_objetos[1].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '29990',
                'imagen': './pintura.avif'
            },

            {
                'codigo': '4F6N-P2BA',
                'marca': 'CORDILLERA',
                'nombre': 'Cerámica 45x45 cm Alicante Beige 2.05 m2',
                'stock': '100',
                'categoria_id': categoria_objetos[1].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '7990',
                'imagen': './ceramica.avif'
            },

            {
                'codigo': '1LQ8-0J00',
                'marca': 'CERESITA',
                'nombre': 'Barniz marino brillante 1/4 gl roble oscuro',
                'stock': '10',
                'categoria_id': categoria_objetos[1].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '8747',
                'imagen': './barniz.avif'
            },

            # Categoria equipos de seguridad

            {
                'codigo': '9R9K-CN9P',
                'marca': 'LIBUS',
                'nombre': 'Casco de seguridad con roller blanco',
                'stock': '10',
                'categoria_id': categoria_objetos[2].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '8570',
                'imagen': './casco.avif'
            },

            {
                'codigo': 'D99O-MSRW',
                'marca': 'REDLINE',
                'nombre': 'Pack 20 pares de guantes forte basic',
                'stock': '10',
                'categoria_id': categoria_objetos[2].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '16990',
                'imagen': './guante.avif'
            },

            {
                'codigo': 'T7B4-8I8X',
                'marca': 'REDLINE',
                'nombre': 'Lente de seguridad Spy Claro',
                'stock': '10',
                'categoria_id': categoria_objetos[2].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '2190',
                'imagen': './lentes.avif'
            },

            {
                'codigo': 'YQB3-S2KA',
                'marca': '3M',
                'nombre': 'Respirador Reutilizable 3M 6200 medio rostro',
                'stock': '15',
                'categoria_id': categoria_objetos[2].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '20990',
                'imagen': './mascarilla.avif'
            },

            {
                'codigo': 'KWBZ-3MC1',
                'marca': 'KARSON',
                'nombre': 'Mascara soldar fotosensible',
                'stock': '20',
                'categoria_id': categoria_objetos[2].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '8747',
                'imagen': './soldar.avif'
            },

            # Categoria tornillos y anclaje

            {
                'codigo': '7NXD-FUQV',
                'marca': 'INCHALAM',
                'nombre': 'Clavo corriente 3" bolsa 1kg',
                'stock': '50',
                'categoria_id': categoria_objetos[3].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '1890',
                'imagen': './clavo-1.avif'
            },

            {
                'codigo': '10DA-SVO0',
                'marca': 'FIXSER',
                'nombre': 'Clavo para techo 2 1/2" bolsa 100 unidades',
                'stock': '20',
                'categoria_id': categoria_objetos[3].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '5890',
                'imagen': './clavo-2.avif'
            },

            {
                'codigo': 'ZPVL-83SB',
                'marca': 'FIXSER',
                'nombre': 'Kit fijaciones para carpinteria 600 unidades',
                'stock': '25',
                'categoria_id': categoria_objetos[3].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '4570',
                'imagen': './fijacion.avif'
            },

            {
                'codigo': 'DBMW-25TU',
                'marca': 'FIXSER',
                'nombre': 'Anclaje tipo mariposa 3/16"x2" 2 unidades',
                'stock': '100',
                'categoria_id': categoria_objetos[3].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '2190',
                'imagen': './anclaje.avif'
            },

            {
                'codigo': 'MZZ8-LAB7',
                'marca': 'MAMUT',
                'nombre': 'Tornillo Volcanita CRS ZRB 6 x 1 1/4" 250 unidades',
                'stock': '50',
                'categoria_id': categoria_objetos[3].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '4990',
                'imagen': './tornillo.avif'
            },

            # Categoria fijaciones y adhesivos

            {
                'codigo': '3ODB-D3V6',
                'marca': 'COMMAND',
                'nombre': 'Gancho ovalado blanco 3 unidades',
                'stock': '50',
                'categoria_id': categoria_objetos[4].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '4390',
                'imagen': './gancho.avif'
            },

            {
                'codigo': 'UTGR-AQ27',
                'marca': 'HENKEL',
                'nombre': 'Adhesivo de montaje Agorex 370 gr',
                'stock': '60',
                'categoria_id': categoria_objetos[4].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '8790',
                'imagen': './adhesivo.avif'
            },

            {
                'codigo': 'BZ3U-FEE5',
                'marca': 'WEBER',
                'nombre': 'Adhesivo Porcelanato Muro Superficie Flexible 24,5 Kg',
                'stock': '30',
                'categoria_id': categoria_objetos[4].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '16640',
                'imagen': './porcelato.avif'
            },

            {
                'codigo': 'ILOC-05Y2',
                'marca': 'COMMAND',
                'nombre': 'Pack 6 Ganchos small blanco',
                'stock': '70',
                'categoria_id': categoria_objetos[4].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '6490',
                'imagen': './gancho-2.avif'
            },

            {
                'codigo': '5PJ2-7119',
                'marca': 'LANCO',
                'nombre': 'Adhesivo de Montaje Súper Nail 300 ml',
                'stock': '30',
                'categoria_id': categoria_objetos[4].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '8080',
                'imagen': './adhesivo-2.avif'
            },

            # Categoria equipos de medicion

             {
                'codigo': 'ZFV1-V4XE',
                'marca': 'DEWALT',
                'nombre': 'Huincha de medir 8 metros plástico',
                'stock': '50',
                'categoria_id': categoria_objetos[5].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '12147',
                'imagen': './huincha.avif'
            },

             {
                'codigo': 'LJM5-DBFL',
                'marca': 'UBERMANN',
                'nombre': 'Escuadra 7" multiple',
                'stock': '20',
                'categoria_id': categoria_objetos[5].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '6291',
                'imagen': './escuadra.avif'
            },

             {
                'codigo': 'LO6Q-0CSM',
                'marca': 'KWB',
                'nombre': 'Regla Guía Universal Para Carpintería Line Master 10pzs Kwb',
                'stock': '29',
                'categoria_id': categoria_objetos[5].id,
                'tienda_id': tienda_objetos[1].id,
                'valor': '42290',
                'imagen': './regla.avif'
            },

             {
                'codigo': 'URQ6-BNJ1',
                'marca': 'UBERMANN',
                'nombre': 'Pie de metro 6" plástico negro',
                'stock': '15',
                'categoria_id': categoria_objetos[5].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '20990',
                'imagen': './pie.avif'
            },

             {
                'codigo': 'A6UL-D0HV',
                'marca': 'BOSCH',
                'nombre': 'Nivel láser 15 m + trípode',
                'stock': '5',
                'categoria_id': categoria_objetos[5].id,
                'tienda_id': tienda_objetos[0].id,
                'valor': '129000',
                'imagen': './laser.avif'
            },
        ]
        producto_objetos = [Producto(**datos) for datos in productos_datos]
        Producto.objects.bulk_create(producto_objetos)