# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-24 17:10
from __future__ import unicode_literals

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
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('armorValue', models.PositiveIntegerField()),
                ('pathIcon', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Caterpillar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('moveValue', models.PositiveIntegerField()),
                ('pathIcon', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Ia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='NavSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('actionValue', models.PositiveIntegerField()),
                ('pathIcon', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Tank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('armor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Armor')),
                ('caterpillar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Caterpillar')),
                ('ia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Ia')),
                ('navSystem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.NavSystem')),
            ],
        ),
        migrations.CreateModel(
            name='TypeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.PositiveIntegerField(default=0)),
                ('avatar', models.ImageField(blank=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('attackValue', models.PositiveIntegerField()),
                ('range', models.PositiveIntegerField()),
                ('pathIcon', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tank',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.UserProfile'),
        ),
        migrations.AddField(
            model_name='tank',
            name='weapon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Weapon'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.UserProfile'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='typeItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TypeItem'),
        ),
        migrations.AddField(
            model_name='ia',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.UserProfile'),
        ),
    ]
