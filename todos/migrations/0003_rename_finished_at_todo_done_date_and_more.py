# Generated by Django 5.0.4 on 2024-04-17 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0002_alter_todo_deadline_alter_todo_finished_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todo",
            old_name="finished_at",
            new_name="done_date",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="todo",
            name="deadline",
        ),
    ]
