# Generated by Django 3.1 on 2020-09-11 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='created_by',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
