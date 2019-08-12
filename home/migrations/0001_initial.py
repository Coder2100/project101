# Generated by Django 2.2.4 on 2019-08-10 20:24

from django.db import migrations, models
import university.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='university/carousel/', validators=[university.validators.image_validation_extension])),
                ('buttonMessage', models.CharField(max_length=255)),
            ],
        ),
    ]