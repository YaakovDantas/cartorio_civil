# Generated by Django 2.2 on 2019-04-18 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_casamento_divorcio_natimorto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='nascimento',
            name='livro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='home.Livro'),
        ),
    ]