# Generated by Django 3.2.6 on 2021-08-30 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0009_alter_apiservice_cache_limit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiservice',
            name='basic_auth_enabled',
            field=models.BooleanField(default=False),
        ),
    ]