# Generated by Django 4.0.2 on 2022-02-15 16:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('social_network_app', '0003_remove_post_num_likes_post_num_likes_delete_postlike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='num_likes',
            field=models.ManyToManyField(blank=True, related_name='num_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
