# Generated by Django 3.1.5 on 2021-01-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='question',
            field=models.TextField(),
        ),
    ]
