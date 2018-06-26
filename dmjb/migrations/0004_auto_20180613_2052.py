# Generated by Django 2.0.5 on 2018-06-13 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dmjb', '0003_job_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='company_name',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='job',
            name='contact_email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
