# Generated by Django 4.2.5 on 2023-10-03 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('celery_id', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(choices=[('RUNNING', 'Running'), ('SUCCESS', 'Success'), ('FAILURE', 'Failure')], default='RUNNING', max_length=10)),
            ],
        ),
    ]
