# Generated by Django 2.2.23 on 2021-09-27 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_reviews', '0002_auto_20210927_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='fieldOfStudy',
            field=models.CharField(default='se', max_length=48, verbose_name='Field of Study'),
            preserve_default=False,
        ),
    ]
