# Generated by Django 4.1.3 on 2022-12-01 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_bk', '0005_alter_usersinfo_enrollment_no_alter_usersinfo_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersinfo',
            name='email',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='usersinfo',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]