# Generated by Django 2.2.5 on 2019-09-15 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebook', '0004_visitorinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitorinfo',
            name='city',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='visitorinfo',
            name='district',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='visitorinfo',
            name='isp',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
