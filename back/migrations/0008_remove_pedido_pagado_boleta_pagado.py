# Generated by Django 4.1.7 on 2024-05-14 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0007_pedido_pagado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='pagado',
        ),
        migrations.AddField(
            model_name='boleta',
            name='pagado',
            field=models.BooleanField(default=False),
        ),
    ]
