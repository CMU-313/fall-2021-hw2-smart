# Generated by Django 2.2.23 on 2021-09-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='fieldOfStudy',
            field=models.CharField(max_length=48, verbose_name='Field of Study', null=True),
            
        ),
        migrations.AlterField(
            model_name='review',
            name='firstName',
            field=models.CharField(max_length=48, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='review',
            name='gradYear',
            field=models.CharField(max_length=48, verbose_name='Graduation Year'),
        ),
        migrations.AlterField(
            model_name='review',
            name='lastName',
            field=models.CharField(max_length=48, verbose_name='Last Name'),
        ),
    ]
