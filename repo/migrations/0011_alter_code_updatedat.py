# Generated by Django 4.2.6 on 2023-11-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0010_delete_variant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
    ]