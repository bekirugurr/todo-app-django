# Generated by Django 4.0.4 on 2022-05-27 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_alter_todo_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='tag',
            field=models.CharField(max_length=20),
        ),
    ]