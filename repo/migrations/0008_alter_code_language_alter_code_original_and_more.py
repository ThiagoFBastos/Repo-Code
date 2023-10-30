# Generated by Django 4.2.6 on 2023-10-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0007_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='language',
            field=models.CharField(choices=[('c++', 'c++'), ('py', 'python'), ('c', 'c'), ('java', 'java'), ('c#', 'c#'), ('js', 'javascript')], max_length=10),
        ),
        migrations.AlterField(
            model_name='code',
            name='original',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='code',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
