# Generated by Django 2.2.12 on 2021-02-05 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BieleGastosApp', '0002_calendario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendario',
            name='codigo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='dia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='dia_sem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='mes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='calendario',
            name='semana',
            field=models.IntegerField(),
        ),
    ]