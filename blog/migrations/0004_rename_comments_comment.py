# Generated by Django 4.1.3 on 2022-12-26 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_comments"),
    ]

    operations = [
        migrations.RenameModel(old_name="comments", new_name="Comment",),
    ]
