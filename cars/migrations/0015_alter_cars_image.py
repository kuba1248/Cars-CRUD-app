# Generated by Django 4.0.6 on 2022-07-20 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0014_cars_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='image',
            field=models.ImageField(default='static/images/bentley.jpg', upload_to='media/'),
        ),
    ]