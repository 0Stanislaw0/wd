# Generated by Django 2.2.1 on 2019-10-09 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='default.jpg', upload_to='user_images', verbose_name='Аватар'),
        ),
    ]
