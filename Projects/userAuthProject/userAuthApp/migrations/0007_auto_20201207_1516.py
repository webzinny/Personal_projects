# Generated by Django 3.1.3 on 2020-12-07 09:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthApp', '0006_auto_20201207_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='reports',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAuthApp.report'),
        ),
    ]
