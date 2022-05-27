# Generated by Django 4.0.4 on 2022-05-27 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('High Priority', '😱 High Priority'), ('Middle Priority', '😨 Middle Priority'), ('Low Priority', '😧 Low Priority')], max_length=50),
        ),
    ]
