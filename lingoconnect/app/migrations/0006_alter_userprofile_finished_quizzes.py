# Generated by Django 4.2.7 on 2023-12-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_userprofile_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='finished_quizzes',
            field=models.ManyToManyField(blank=True, default=set(), to='app.quiz'),
        ),
    ]
