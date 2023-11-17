# Generated by Django 4.2.7 on 2023-11-17 08:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('korean_name', models.TextField(blank=True)),
                ('profile_path', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('korean_name', models.TextField(blank=True)),
                ('profile_path', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('original_title', models.TextField()),
                ('certification', models.TextField(blank=True)),
                ('overview', models.TextField(blank=True)),
                ('release_date', models.DateField()),
                ('runtime', models.IntegerField()),
                ('tagline', models.TextField(blank=True)),
                ('poster_path', models.TextField(blank=True)),
                ('backdrop_path', models.TextField(blank=True)),
                ('trailer', models.TextField(blank=True)),
                ('rating_avg', models.FloatField(default=0)),
                ('rating_cnt', models.IntegerField(default=0)),
                ('actors', models.ManyToManyField(to='movies.actor')),
                ('directors', models.ManyToManyField(to='movies.director')),
                ('genres', models.ManyToManyField(to='movies.genre')),
            ],
        ),
        migrations.CreateModel(
            name='WatchProvider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('log_img', models.ImageField(blank=True, upload_to='')),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500)),
                ('rating', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='watch_providers',
            field=models.ManyToManyField(to='movies.watchprovider'),
        ),
    ]
