# Generated by Django 2.1.2 on 2018-11-19 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Github',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=150)),
                ('url', models.CharField(max_length=150)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar_media')),
            ],
        ),
    ]
