# Generated by Django 4.0.3 on 2022-05-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0017_issue_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pc',
            name='pcStatus',
            field=models.CharField(max_length=24),
        ),
    ]
