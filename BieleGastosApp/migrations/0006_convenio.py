# Generated by Django 2.2.12 on 2021-02-19 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BieleGastosApp', '0005_gastos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Convenio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'convenio',
            },
        ),
    ]
