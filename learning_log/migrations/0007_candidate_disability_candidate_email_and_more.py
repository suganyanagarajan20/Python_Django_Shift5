# Generated by Django 4.2.6 on 2023-10-21 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0006_candidate_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='disability',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='candidate',
            name='email',
            field=models.EmailField(default=False, max_length=254, unique=True),
        ),
        migrations.AddField(
            model_name='candidate',
            name='marital_status',
            field=models.CharField(default=False, max_length=25),
        ),
    ]
