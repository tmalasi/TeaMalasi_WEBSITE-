# Generated by Django 4.1.1 on 2022-10-05 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=50, null=True)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('product_review', models.TextField(blank=True, max_length=100, null=True)),
                ('product_image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
