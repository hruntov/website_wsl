# Generated by Django 5.0.2 on 2024-02-07 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='youtuber',
            options={'ordering': ['id'], 'verbose_name_plural': 'Youtubers'},
        ),
    ]
