# Generated by Django 2.2.1 on 2019-05-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.TextField(max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]