# Generated by Django 2.2 on 2019-04-29 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='title',
            new_name='post',
        ),
    ]
