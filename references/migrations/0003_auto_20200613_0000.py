# Generated by Django 3.0.7 on 2020-06-12 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0002_post_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created',)},
        ),
    ]
