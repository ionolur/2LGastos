# Generated by Django 2.2.12 on 2021-02-04 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Horas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField()),
                ('slug', models.SlugField()),
                ('horas_trabajo', models.DecimalField(decimal_places=1, max_digits=3)),
                ('viaje_ida', models.DecimalField(decimal_places=1, max_digits=3)),
                ('viaje_vuelta', models.DecimalField(decimal_places=1, max_digits=3)),
                ('pernocta', models.BooleanField()),
                ('semana_3', models.BooleanField()),
                ('notas', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'hora',
                'verbose_name_plural': 'horas',
                'ordering': ('autor', 'dia'),
            },
        ),
    ]
