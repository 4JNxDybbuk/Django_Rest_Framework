# Generated by Django 4.0.1 on 2022-02-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('author', models.CharField(max_length=40)),
                ('discouunt', models.IntegerField()),
                ('duration', models.FloatField()),
            ],
        ),
    ]