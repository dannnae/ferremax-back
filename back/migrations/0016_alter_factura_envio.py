# Generated by Django 4.1.7 on 2024-07-07 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0015_remove_factura_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='factura',
            name='envio',
            field=models.IntegerField(null=True),
        ),
    ]