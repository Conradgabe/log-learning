# Generated by Django 4.0.2 on 2022-05-23 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_topic_public'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='public',
            field=models.CharField(choices=[('Y', 'yes'), ('N', 'no')], max_length=2),
        ),
    ]
