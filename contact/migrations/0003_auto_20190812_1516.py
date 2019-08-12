# Generated by Django 2.2.4 on 2019-08-12 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_asked_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='asked_date',
        ),
        migrations.AddField(
            model_name='contact',
            name='posted_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
