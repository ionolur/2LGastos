# Generated by Django 2.2.12 on 2021-02-26 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('BieleGastosApp', '0007_resultado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('irpf', models.DecimalField(decimal_places=2, max_digits=4)),
                ('reduccion', models.DecimalField(decimal_places=2, max_digits=4)),
                ('guardar_normal', models.BooleanField()),
                ('guardar_ertain', models.BooleanField()),
                ('guardar_berezi', models.BooleanField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]