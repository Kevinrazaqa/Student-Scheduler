# Generated by Django 4.0 on 2022-12-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('focus_session', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chek',
            name='date',
        ),
        migrations.AddField(
            model_name='chek',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
