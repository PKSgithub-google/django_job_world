# Generated by Django 3.2 on 2021-05-07 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_job_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='job',
            options={'ordering': ['date_loggedin']},
        ),
        migrations.RenameField(
            model_name='job',
            old_name='job_id',
            new_name='id',
        ),
    ]
