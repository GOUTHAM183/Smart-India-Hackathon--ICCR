# Generated by Django 3.1.3 on 2022-08-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
