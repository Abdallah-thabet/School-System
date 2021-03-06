# Generated by Django 3.1.1 on 2020-09-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0003_auto_20200926_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=18),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='age',
            field=models.IntegerField(default=32),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='experience',
            field=models.IntegerField(default=2),
        ),
    ]
