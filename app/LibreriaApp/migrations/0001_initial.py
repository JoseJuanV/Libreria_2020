# Generated by Django 3.0.7 on 2020-06-07 23:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('apellidos', models.CharField(max_length=25)),
                ('nombres', models.CharField(max_length=25)),
            ],
            options={
                'ordering': ['id_autor'],
            },
        ),
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id_categoria', models.AutoField(primary_key=True, serialize=False)),
                ('categoria', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['id_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('identificacion', models.CharField(max_length=12)),
                ('nombres', models.CharField(max_length=25)),
                ('apellidos', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=128)),
                ('correo_electronico', models.EmailField(max_length=128)),
            ],
            options={
                'ordering': ['id_cliente'],
            },
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=128)),
                ('fecha_pub', models.DateField()),
                ('fecha_creacion', models.DateField(auto_now=True)),
                ('precio', models.IntegerField()),
                ('portada', models.ImageField(blank=True, default='', null=True, upload_to='portada/')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibreriaApp.Categorias')),
                ('id_autor', models.ManyToManyField(to='LibreriaApp.Autores')),
            ],
            options={
                'ordering': ['fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='PedidosCliente',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
                ('nro_pedido', models.CharField(max_length=255, unique=True)),
                ('fecha_pedido', models.DateField(auto_now=True)),
                ('cantidad', models.IntegerField()),
                ('valor', models.IntegerField()),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibreriaApp.Cliente')),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibreriaApp.Libros')),
            ],
            options={
                'ordering': ['id_pedido'],
            },
        ),
    ]
