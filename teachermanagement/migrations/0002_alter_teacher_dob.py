# Generated by Django 5.0.1 on 2024-02-06 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='dob',
            field=models.CharField(max_length=100),
        ),
    ]
