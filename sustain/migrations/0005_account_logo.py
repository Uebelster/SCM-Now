# Generated by Django 2.2.19 on 2021-03-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sustain', '0004_auto_20210305_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
