# Generated by Django 2.1.7 on 2019-02-13 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12, verbose_name='Preço'),
            preserve_default=False,
        ),
    ]