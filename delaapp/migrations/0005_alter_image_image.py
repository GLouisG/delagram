# Generated by Django 3.2.8 on 2021-10-17 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delaapp', '0004_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
