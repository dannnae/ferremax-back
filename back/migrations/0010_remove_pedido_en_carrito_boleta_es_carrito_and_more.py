# Generated by Django 4.1.7 on 2024-05-20 18:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0009_boleta_buy_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='en_carrito',
        ),
        migrations.AddField(
            model_name='boleta',
            name='es_carrito',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='boleta',
            name='tienda_entrega',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='back.tienda'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='boleta',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='back.boleta'),
        ),
    ]