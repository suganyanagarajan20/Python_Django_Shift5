# Generated by Django 4.2.6 on 2023-10-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0005_candidate_first_name_candidate_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='sex',
            field=models.CharField(default=' ', max_length=15),
        ),
    ]
