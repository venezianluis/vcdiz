# Generated by Django 3.0.8 on 2020-07-18 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20200718_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='pic',
            field=models.ImageField(default='static/blog/pic_folder/None/no-img.jpg', upload_to='static/blog/pic_folder/'),
        ),
    ]
