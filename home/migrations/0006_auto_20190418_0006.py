# Generated by Django 2.2 on 2019-04-18 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190418_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nascimento',
            name='livro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Livro'),
        ),
    ]