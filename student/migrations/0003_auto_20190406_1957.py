# Generated by Django 2.1.7 on 2019-04-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_cse_studentgen'),
    ]

    operations = [
        migrations.AddField(
            model_name='cse',
            name='compiler',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='Computer_Networks',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='communication',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='cp',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='dbms',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='dsa',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='jee_mains',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='oops',
            field=models.FloatField(default=50),
        ),
        migrations.AlterField(
            model_name='cse',
            name='os',
            field=models.FloatField(default=50),
        ),
    ]