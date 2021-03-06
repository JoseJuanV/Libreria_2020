# Generated by Django 3.0.7 on 2020-06-07 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UsuarioApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='apellido',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nombre',
            field=models.CharField(max_length=150),
        ),
    ]
