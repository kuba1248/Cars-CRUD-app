# Generated by Django 4.0.6 on 2022-07-20 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_alter_cars_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
