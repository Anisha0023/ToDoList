# Generated by Django 5.1.3 on 2025-01-15 17:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0005_remove_task_edit_remove_task_trash_task_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='screenshots/')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='taskmanager.task')),
            ],
        ),
    ]
