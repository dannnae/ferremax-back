# Generated by Django 4.1.7 on 2024-04-27 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0004_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default=None, upload_to=''),
        ),
    ]
