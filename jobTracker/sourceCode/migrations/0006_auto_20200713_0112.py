# Generated by Django 3.0.7 on 2020-07-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourceCode', '0005_auto_20200702_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, choices=[('pending', 'Pending'), ('success', 'Success'), ('not-selected', 'Not-Selected'), ('interviewing', 'Interviewing')], default='', max_length=20, null=True, verbose_name='status'),
        ),
    ]
