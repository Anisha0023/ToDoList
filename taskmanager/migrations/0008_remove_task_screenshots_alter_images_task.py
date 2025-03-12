# Generated by Django 5.1.3 on 2025-01-15 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0007_task_screenshots_images_delete_taskimages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='screenshots',
        ),
        migrations.AlterField(
            model_name='images',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='screenshots', to='taskmanager.task'),
        ),
    ]
