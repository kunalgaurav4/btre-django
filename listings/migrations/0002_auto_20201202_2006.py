# Generated by Django 3.1.3 on 2020-12-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='city',
            field=models.CharField(max_length=20),
        ),
    ]
