# Generated by Django 4.2.6 on 2023-10-25 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0025_alter_candidate_photo_candidate_docs'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='job',
            name='job_sal_expect',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]