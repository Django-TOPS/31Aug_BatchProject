# Generated by Django 2.0 on 2021-01-08 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20210101_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='notes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('myfile', models.FileField(upload_to='upload')),
                ('comment', models.CharField(max_length=500)),
            ],
        ),
    ]