from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('documents', '0075_delete_duplicateddocumentold'),
        ('sites', '0001_initial'),
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                (
                    'id', models.AutoField(
                        verbose_name='ID', serialize=False, auto_created=True,
                        primary_key=True
                    )
                ),
                (
                    'firstName', models.CharField(
                        verbose_name='First Name'
                    )
                ),
                (
                    'lastName', models.CharField(
                        verbose_name='Last Name'
                    )
                ),
                (
                    'gradYear', models.CharField(
                        verbose_name='Graduation Year'
                    )
                ),
                (
                    'fieldOfStudy', models.CharField(
                        verbose_name='Field of Study'
                    )
                ),
                (
                    'gpaScale', models.IntegerField(
                        verbose_name='GPA: Rate 1-10'
                    )
                ),
                (
                    'technicalScale', models.IntegerField(
                        verbose_name='Technical Skills: Rate 1-10'
                    )
                ),
                (
                    'communicationScale', models.IntegerField(
                        verbose_name='Communication Skills: Rate 1-10'
                    )
                ),
                (
                    'experienceScale', models.IntegerField(
                        verbose_name='Experience: Rate 1-10'
                    )
                ),
                (
                    'addlcomments', models.TextField(
                        verbose_name='Additional Comments'
                    )
                ),
                (
                    'submit_date', models.DateTimeField(
                        auto_now_add=True,
                        verbose_name='Date time submitted', db_index=True
                    )
                ),
                (
                    'document', models.ForeignKey(
                        on_delete=models.CASCADE, related_name='reviews',
                        to='documents.Document', verbose_name='Document'
                    )
                ),
                (
                    'user', models.ForeignKey(
                        editable=False, on_delete=models.CASCADE,
                        related_name='reviews', to=settings.AUTH_USER_MODEL,
                        verbose_name='User'
                    )
                ),
            ],
            options={
                'ordering': ('-submit_date',),
                'get_latest_by': 'submit_date',
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
            bases=(models.Model,),
        ),
    ]
