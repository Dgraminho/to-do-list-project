# Generated by Django 3.1.4 on 2020-12-14 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projeto_lista', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='finished',
            new_name='completed',
        ),
    ]
