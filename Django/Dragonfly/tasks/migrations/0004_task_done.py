# Generated by Django 3.1.7 on 2021-04-12 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20210412_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='Done',
            field=models.CharField(choices=[('Yes', 'YES'), ('NO', 'NO')], default='NO', max_length=3),
        ),
    ]
