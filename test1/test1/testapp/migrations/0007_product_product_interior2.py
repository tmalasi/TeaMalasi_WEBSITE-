# Generated by Django 4.1.1 on 2022-10-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0006_product_product_interior1'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_interior2',
            field=models.ImageField(blank=True, null=True, upload_to='interior/'),
        ),
    ]
