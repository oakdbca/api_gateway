# Generated by Django 3.2.6 on 2021-08-27 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0003_auto_20210827_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiservice',
            name='aws_access_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_host',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_region',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_secret_access_key',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_service',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='aws_token',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='cache_limit',
            field=models.IntegerField(default=0, help_text='Cache expiry limit in seconds'),
        ),
        migrations.AlterField(
            model_name='apiservice',
            name='service_type',
            field=models.IntegerField(choices=[(1, 'AWS (AWSRequestsAuth)'), (2, 'HTTP/s Request (GET)'), (3, 'HTTP/s Request (POST)')], default=0),
        ),
    ]