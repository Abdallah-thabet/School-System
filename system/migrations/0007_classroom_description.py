# Generated by Django 3.1.1 on 2020-09-26 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_auto_20200926_0606'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='description',
            field=models.TextField(default='No Description', max_length=300),
        ),
    ]
