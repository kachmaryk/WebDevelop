# Generated by Django 3.0.6 on 2020-06-07 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Japan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guests', models.IntegerField()),
                ('acomodation', models.CharField(max_length=100)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('optional', models.CharField(max_length=100)),
            ],
        ),
    ]
