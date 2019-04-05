# Generated by Django 2.1.7 on 2019-04-04 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=1000)),
                ('company_id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('skills_required', models.CharField(max_length=1000)),
                ('ctc', models.CharField(max_length=1000)),
                ('date_of_visit', models.CharField(max_length=1000)),
                ('openings', models.CharField(max_length=1000)),
                ('rounds', models.CharField(max_length=1000)),
                ('company_id', models.CharField(max_length=1000)),
                ('job_id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
            ],
        ),
    ]