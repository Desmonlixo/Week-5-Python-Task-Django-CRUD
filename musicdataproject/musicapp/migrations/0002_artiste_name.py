# Generated by Django 4.1.2 on 2022-10-27 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='name',
            field=models.CharField(default=1, max_length=400),
            preserve_default=False,
        ),
    ]