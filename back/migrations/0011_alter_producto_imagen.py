# Generated by Django 4.1.7 on 2024-05-23 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0010_remove_pedido_en_carrito_boleta_es_carrito_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=None, null=True, upload_to='./media'),
        ),
    ]
