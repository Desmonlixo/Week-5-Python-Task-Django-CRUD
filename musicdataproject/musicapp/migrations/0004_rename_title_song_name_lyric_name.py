# Generated by Django 4.1.2 on 2022-10-27 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0003_alter_lyric_song_id_alter_song_artiste_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='lyric',
            name='name',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
