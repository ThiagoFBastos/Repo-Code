# Generated by Django 4.2.6 on 2023-10-25 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0008_alter_code_language_alter_code_original_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='human_name',
            field=models.CharField(max_length=50),
        ),
    ]