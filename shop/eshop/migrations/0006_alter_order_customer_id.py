# Generated by Django 4.0.4 on 2022-04-11 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0005_alter_status_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='eshop.customer'),
        ),
    ]