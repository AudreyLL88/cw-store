# Generated by Django 3.1.7 on 2021-03-14 20:32

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20210314_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productstock',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productstock',
            name='sizes',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('XS', 'X-Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'X-Large')], max_length=11, null=True),
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
        migrations.DeleteModel(
            name='ProductStock',
        ),
    ]
