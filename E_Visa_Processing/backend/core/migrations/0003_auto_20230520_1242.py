# Generated by Django 3.0.5 on 2023-05-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230520_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visa',
            name='aadhar',
            field=models.FileField(max_length=255, upload_to='visa/'),
        ),
        migrations.AlterField(
            model_name='visa',
            name='pancard',
            field=models.FileField(max_length=255, upload_to='visa/'),
        ),
        migrations.AlterField(
            model_name='visa_details',
            name='photo',
            field=models.FileField(max_length=255, upload_to='visa_details/'),
        ),
        migrations.AlterField(
            model_name='visa_details',
            name='sign',
            field=models.FileField(max_length=255, upload_to='visa_details/'),
        ),
    ]