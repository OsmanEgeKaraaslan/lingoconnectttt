# Generated by Django 4.2.7 on 2023-12-16 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_question_correct_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='question',
            name='correct_answer',
            field=models.CharField(max_length=10000),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option2',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option3',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='option4',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=10000),
        ),
    ]
