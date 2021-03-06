# Generated by Django 3.1.6 on 2021-02-16 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20210216_0017'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=255)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8)),
                ('produto', models.ManyToManyField(to='website.Clientes')),
            ],
        ),
    ]
