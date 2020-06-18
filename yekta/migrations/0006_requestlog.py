# Generated by Django 3.0.7 on 2020-06-18 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yekta', '0005_auto_20200617_1907'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=16)),
                ('time', models.DateTimeField()),
                ('browser', models.CharField(max_length=7)),
                ('device', models.CharField(max_length=7)),
            ],
        ),
    ]
