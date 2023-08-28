# Generated by Django 4.2.3 on 2023-08-28 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'ordering': ['product_name'], 'verbose_name': 'Item', 'verbose_name_plural': 'Itens'},
        ),
        migrations.AddField(
            model_name='order',
            name='paidInfo',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterUniqueTogether(
            name='orderitem',
            unique_together={('product_id', 'order')},
        ),
    ]