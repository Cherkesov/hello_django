# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-03 21:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hello_django_app', '0002_auto_20160304_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proportion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_django_app.Ingredient')),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hello_django_app.Measure')),
            ],
        ),
    ]
