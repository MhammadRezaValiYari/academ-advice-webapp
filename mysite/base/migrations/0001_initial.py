# Generated by Django 3.2.8 on 2022-01-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_title', models.CharField(max_length=50)),
                ('about_article', models.CharField(max_length=1000)),
                ('phone_nummbers', models.IntegerField()),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
