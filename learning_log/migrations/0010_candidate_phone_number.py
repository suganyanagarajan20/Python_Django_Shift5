# Generated by Django 4.2.6 on 2023-10-21 16:37

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0009_candidate_self_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, default='+41', max_length=128, null=True, region=None),
        ),
    ]
