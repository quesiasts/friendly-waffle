# Generated by Django 3.1.6 on 2021-02-16 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionario',
            name='idade',
            field=models.IntegerField(),
        ),
    ]