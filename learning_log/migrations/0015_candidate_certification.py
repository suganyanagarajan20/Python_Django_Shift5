# Generated by Django 4.2.6 on 2023-10-21 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0014_candidate_account'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate_certification',
            fields=[
                ('certification_id', models.IntegerField(primary_key=True, serialize=False)),
                ('org_name', models.TextField(default=' ', max_length=200)),
                ('credential_id', models.CharField(default=' ', max_length=100)),
                ('credential_url', models.TextField(default=' ', max_length=200)),
                ('skillset', models.TextField(default=' ', max_length=255)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_log.candidate')),
            ],
        ),
    ]