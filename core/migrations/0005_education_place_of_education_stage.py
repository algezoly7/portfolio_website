# Generated by Django 4.0.2 on 2022-02-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='place_of_education_stage',
            field=models.CharField(default="don't have", max_length=50),
            preserve_default=False,
        ),
    ]