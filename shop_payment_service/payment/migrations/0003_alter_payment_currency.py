# Generated by Django 4.2.3 on 2023-08-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_card_number_payment_cvc_payment_expiry_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='currency',
            field=models.CharField(default='USD', max_length=200),
        ),
    ]