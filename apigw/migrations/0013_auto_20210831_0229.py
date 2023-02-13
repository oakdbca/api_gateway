# Generated by Django 3.2.6 on 2021-08-31 02:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('apigw', '0012_auto_20210831_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='apiservice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='APIServiceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_slug_url', models.CharField(max_length=1024)),
                ('client_ip', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('api_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='api_service_id', to='apigw.apiservice')),
            ],
        ),
    ]