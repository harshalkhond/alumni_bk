# Generated by Django 4.1.3 on 2022-12-01 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_bk', '0004_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersinfo',
            name='enrollment_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usersinfo',
            name='role',
            field=models.CharField(max_length=120),
        ),
    ]
