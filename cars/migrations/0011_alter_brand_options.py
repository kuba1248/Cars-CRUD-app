# Generated by Django 4.0.6 on 2022-07-17 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_cars_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'ordering': ['-id']},
        ),
    ]