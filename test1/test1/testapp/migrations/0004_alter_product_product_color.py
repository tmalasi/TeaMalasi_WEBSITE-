# Generated by Django 4.1.1 on 2022-10-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_category_color_product_product_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_color',
            field=models.ManyToManyField(blank=True, to='testapp.color'),
        ),
    ]
