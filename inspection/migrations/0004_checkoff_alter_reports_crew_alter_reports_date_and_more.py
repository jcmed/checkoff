# Generated by Django 4.1.7 on 2023-06-25 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0003_alter_reports_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkoff',
            fields=[
                ('unit', models.IntegerField(primary_key=True, serialize=False)),
                ('miles', models.IntegerField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('assignment', models.CharField(max_length=100, null=True)),
                ('unit_raw', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='reports',
            name='crew',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='date',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='status',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reports',
            name='unit',
            field=models.IntegerField(null=True),
        ),
    ]