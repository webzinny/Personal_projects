# Generated by Django 3.1.3 on 2020-12-24 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BJPdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True)),
                ('Designation', models.CharField(blank=True, max_length=64)),
                ('Name', models.CharField(blank=True, max_length=64)),
                ('Place', models.CharField(blank=True, max_length=64)),
                ('Contact', models.CharField(blank=True, max_length=64)),
                ('Session', models.CharField(max_length=20)),
            ],
        ),
    ]