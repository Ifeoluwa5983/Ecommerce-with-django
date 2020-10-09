# Generated by Django 3.1 on 2020-10-01 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_item',
            new_name='Order_item',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='detail_text',
        ),
        migrations.RemoveField(
            model_name='product',
            name='mainImage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='preview_text',
        ),
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AddField(
            model_name='product',
            name='digital',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
