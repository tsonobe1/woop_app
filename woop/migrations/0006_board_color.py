# Generated by Django 3.0.5 on 2020-07-05 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woop', '0005_auto_20200702_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='色'),
        ),
    ]
