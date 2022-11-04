# Generated by Django 3.2.15 on 2022-11-01 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0023_auto_20221027_1303'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coach',
            options={'verbose_name': 'Тренера', 'verbose_name_plural': 'Тренеры'},
        ),
        migrations.RenameField(
            model_name='video',
            old_name='video_url',
            new_name='video_url_1',
        ),
        migrations.AddField(
            model_name='video',
            name='video_url_2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='video_url_3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='is_agreed',
            field=models.BooleanField(default=False, verbose_name='Согласие на обработку'),
        ),
    ]
