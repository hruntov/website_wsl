# Generated by Django 5.0.2 on 2024-02-24 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_alter_category_options_alter_youtuber_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('youtuber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='youtubers.youtuber')),
            ],
            options={
                'ordering': ['created_at'],
                'indexes': [models.Index(fields=['created_at'], name='youtubers_c_created_f475ae_idx')],
            },
        ),
    ]
