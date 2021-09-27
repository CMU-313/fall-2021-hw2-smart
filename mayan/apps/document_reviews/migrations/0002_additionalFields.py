from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('document_reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Review',
            name='firstName',
            field=models.CharField(
                max_length=48, verbose_name='First Name', default="fname"
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='lastName',
            field=models.CharField(
                max_length=48, verbose_name='Last Name', default="lname"
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='gradYear',
            field=models.CharField(
                max_length=48, verbose_name='Graduation Year', default="gyear"
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='fieldOfStudy',
            field=models.CharField(
                max_length=48, verbose_name='Field of Study', default="None"
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='gpaScale',
            field=models.IntegerField(
                verbose_name='GPA: Rate 1-10', default=0
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='technicalScale',
            field=models.IntegerField(
                verbose_name='Technical Skills: Rate 1-10', default=0
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='communicationScale',
            field=models.IntegerField(
                verbose_name='Communication Skills: Rate 1-10', default=0
            ),
        ),
        migrations.AddField(
            model_name='Review',
            name='experienceScale',
            field=models.IntegerField(
                verbose_name='Experience: Rate 1-10', default=0
            ),
        ),
    ]
