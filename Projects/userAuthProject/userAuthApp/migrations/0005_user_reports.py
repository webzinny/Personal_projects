# Generated by Django 3.1.3 on 2020-12-07 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthApp', '0004_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reports',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='userAuthApp.report'),
        ),
    ]