# Generated by Django 2.2.28 on 2023-02-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security_system', '0003_auto_20230207_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smokerecord',
            name='hydrogen',
        ),
        migrations.RemoveField(
            model_name='smokerecord',
            name='lpg',
        ),
        migrations.RemoveField(
            model_name='smokerecord',
            name='methan',
        ),
        migrations.RemoveField(
            model_name='smokerecord',
            name='smoke',
        ),
        migrations.AlterField(
            model_name='smokerecord',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
