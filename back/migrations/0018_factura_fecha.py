# Generated by Django 4.1.7 on 2024-07-15 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0017_factura_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
    ]