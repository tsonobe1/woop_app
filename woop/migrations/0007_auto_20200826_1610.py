# Generated by Django 3.0.5 on 2020-08-26 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('woop', '0006_board_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_title',
            field=models.CharField(max_length=200, verbose_name='やること'),
        ),
    ]