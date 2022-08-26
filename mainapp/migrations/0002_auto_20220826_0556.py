# Generated by Django 3.2.15 on 2022-08-26 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='preambule',
            field=models.CharField(max_length=256, verbose_name='Вступление'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Заголовок'),
        ),
        migrations.CreateModel(
            name='NewsImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='news/%Y/%m/%d')),
                ('news', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainapp.news')),
            ],
        ),
    ]
