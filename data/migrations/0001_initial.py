# Generated by Django 2.1.1 on 2018-09-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_field', models.CharField(max_length=200)),
                ('second_field', models.CharField(max_length=200)),
                ('third_field', models.CharField(max_length=200)),
                ('fourth_field', models.CharField(max_length=200)),
            ],
        ),
    ]
