# Generated by Django 4.1.7 on 2024-04-27 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0003_pedido_en_carrito'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]
