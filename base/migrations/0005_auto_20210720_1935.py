# Generated by Django 3.2.5 on 2021-07-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_enquiry_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enquiry',
            name='documents',
        ),
        migrations.AlterField(
            model_name='enquiry',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]