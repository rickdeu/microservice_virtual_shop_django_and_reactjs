# Generated by Django 4.2.3 on 2023-08-28 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_alter_orderitem_options_order_paidinfo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paidInfo',
            field=models.JSONField(default=dict, null=True),
        ),
    ]
