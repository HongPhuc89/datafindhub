# Generated by Django 3.0.3 on 2020-04-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_field', models.FileField(upload_to='uploaded/')),
                ('cred_file_field', models.FileField(upload_to='uploaded/')),
            ],
        ),
        migrations.CreateModel(
            name='InterSavedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_address', models.CharField(max_length=100)),
                ('original_text', models.CharField(max_length=10000)),
                ('translated_text', models.CharField(max_length=10000)),
                ('link_name', models.CharField(default='.png', max_length=1000)),
                ('image', models.URLField()),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SavedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('web_address', models.CharField(max_length=100)),
                ('original_text', models.CharField(max_length=10000)),
                ('translated_text', models.CharField(max_length=10000)),
                ('link_name', models.CharField(default='.png', max_length=1000)),
                ('link', models.URLField()),
            ],
        ),
    ]
