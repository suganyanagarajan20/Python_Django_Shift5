# Generated by Django 4.2.6 on 2023-10-22 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning_log', '0016_candidate_certification_expiry_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate_certification',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='candidate_certification',
            name='issuing_date',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='Candidate_exp',
            fields=[
                ('exp_id', models.IntegerField(primary_key=True, serialize=False)),
                ('curr_comp', models.CharField(default=' ', max_length=50)),
                ('job_title', models.CharField(default=' ', max_length=50)),
                ('skills', models.CharField(default=' ', max_length=50)),
                ('work_desc', models.TextField(max_length=100)),
                ('date_of_joining', models.DateField(null=True)),
                ('date_of_termination', models.DateTimeField(null=True)),
                ('permit', models.CharField(default=' ', max_length=50)),
                ('language', models.CharField(default=' ', max_length=50)),
                ('level', models.CharField(default=' ', max_length=50)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning_log.candidate')),
            ],
        ),
    ]
