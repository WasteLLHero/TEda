# Generated by Django 4.1.4 on 2023-04-29 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dishes',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
