# Generated by Django 4.0.6 on 2022-07-22 01:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0025_alter_brand_options_alter_cars_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-id', 'Brand']},
        ),
        migrations.AlterModelOptions(
            name='cars',
            options={'ordering': ['-id', 'brand']},
        ),
    ]
