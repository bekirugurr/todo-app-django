# Generated by Django 4.0.4 on 2022-05-25 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_alter_todo_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='done',
            name='priority',
            field=models.CharField(choices=[('High Priority', 'High Priority'), ('Middle Priority', 'Middle Priority'), ('Low Priority', 'Lox Priority')], default='Middle Priority', max_length=50),
        ),
        migrations.AlterField(
            model_name='todo',
            name='priority',
            field=models.CharField(choices=[('High Priority', 'High Priority'), ('Middle Priority', 'Middle Priority'), ('Low Priority', 'Lox Priority')], default='Middle Priority', max_length=50),
        ),
    ]