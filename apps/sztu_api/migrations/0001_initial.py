# Generated by Django 2.1.7 on 2019-03-08 08:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Click',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ip', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, max_length=800, null=True)),
                ('access_time', models.DateTimeField(blank=True, null=True)),
                ('create_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='最后修改时间')),
            ],
        ),
    ]