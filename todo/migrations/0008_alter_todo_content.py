# Generated by Django 4.0.4 on 2022-05-27 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_delete_done_todo_is_done'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(max_length=100),
        ),
    ]
