# Generated by Django 5.1.3 on 2024-12-10 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discover', '0002_game_thumbnail_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='game',
            name='platform',
        ),
        migrations.AddField(
            model_name='game',
            name='platforms',
            field=models.ManyToManyField(blank=True, to='discover.platform'),
        ),
    ]
