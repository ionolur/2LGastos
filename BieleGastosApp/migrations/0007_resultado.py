# Generated by Django 2.2.12 on 2021-02-20 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BieleGastosApp', '0006_convenio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resultado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'resultado',
                'verbose_name_plural': 'resultados',
            },
        ),
    ]
