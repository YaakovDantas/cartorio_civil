# Generated by Django 2.1.2 on 2019-01-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20190128_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nascimento',
            name='imagem',
            field=models.ImageField(upload_to='fotos'),
        ),
    ]
