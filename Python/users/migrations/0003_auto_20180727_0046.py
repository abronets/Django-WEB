# Generated by Django 2.0.6 on 2018-07-26 21:46

from django.db import migrations
import users.managers


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180721_1324'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
