# Generated by Django 4.2.6 on 2023-10-16 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0006_tag_human_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('human_name', models.CharField(max_length=50)),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo.tag')),
            ],
        ),
    ]
