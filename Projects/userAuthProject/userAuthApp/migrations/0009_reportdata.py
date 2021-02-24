# Generated by Django 3.1.3 on 2020-12-07 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userAuthApp', '0008_auto_20201207_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('dealerName', models.CharField(max_length=128)),
                ('location', models.CharField(max_length=64)),
                ('spn', models.CharField(max_length=64)),
                ('spcn', models.IntegerField()),
                ('standName', models.CharField(max_length=64)),
                ('ncife', models.IntegerField()),
                ('tnov', models.IntegerField()),
                ('tataAce', models.CharField(max_length=64)),
                ('boleroPickup', models.CharField(max_length=64)),
                ('alfaLoad', models.CharField(max_length=64)),
                ('ashok', models.CharField(max_length=64)),
                ('piagioApe', models.CharField(max_length=64)),
                ('atul', models.CharField(max_length=64)),
                ('otherVehicles', models.CharField(max_length=64)),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAuthApp.report')),
            ],
        ),
    ]
