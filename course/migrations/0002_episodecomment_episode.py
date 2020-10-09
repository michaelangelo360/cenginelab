# Generated by Django 3.1.2 on 2020-10-09 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodecomment',
            name='episode',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='course.episode'),
            preserve_default=False,
        ),
    ]
