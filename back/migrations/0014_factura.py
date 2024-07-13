# Generated by Django 4.1.7 on 2024-07-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0013_alter_customuser_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('rut', models.CharField(max_length=20)),
                ('telefono', models.CharField(max_length=20)),
                ('comuna', models.CharField(max_length=100)),
                ('ciudad', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=200)),
                ('direccion2', models.CharField(max_length=200)),
                ('envio', models.IntegerField()),
            ],
        ),
    ]
