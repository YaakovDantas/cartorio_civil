# Generated by Django 2.2 on 2019-04-18 00:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20190418_0006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nascimento',
            name='livro',
        ),
    ]
