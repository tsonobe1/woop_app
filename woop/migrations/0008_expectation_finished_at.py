# Generated by Django 3.0.5 on 2020-09-08 12:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('woop', '0007_auto_20200826_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='expectation',
            name='finished_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了日時'),
        ),
    ]