# Generated by Django 5.0 on 2023-12-12 12:06

from django.db import migrations


def add_test_data(apps, schema_editor):
    TestModel = apps.get_model('youtubers', 'TestModel')
    TestModel.objects.create(test_text="Test 1")
    TestModel.objects.create(test_text="Test 2")


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_test_data)
    ]
