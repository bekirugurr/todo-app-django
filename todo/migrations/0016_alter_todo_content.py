# Generated by Django 4.0.4 on 2022-05-27 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0015_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='content',
            field=models.TextField(max_length=120),
        ),
    ]