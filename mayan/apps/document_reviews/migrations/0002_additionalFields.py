from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('documennt_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Review',
            name='firstName',
            field=models.CharField(
                verbose_name='First Name'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='lastName',
            field=models.CharField(
                verbose_name='lastName'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='gradYear',
            field=models.CharField(
                verbose_name='Graduation Year'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='fieldOfStudy',
            field=models.CharField(
                verbose_name='Field of Study'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='gpaScale',
            field=models.IntegerField(
                verbose_name='GPA: Rate 1-10'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='techinicalScale',
            field=models.IntegerField(
                verbose_name='Technical Skills: Rate 1-10'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='communicationScale',
            field=models.IntegerField(
                verbose_name='Communication Skills: Rate 1-10'
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='experienceScale',
            field=models.IntegerField(
                verbose_name='Experience: Rate 1-10'
            ),
        ),
    ]
