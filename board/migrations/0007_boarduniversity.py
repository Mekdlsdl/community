# Generated by Django 4.2.3 on 2023-07-09 03:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0006_commentsdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoardUniversity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField(default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='board_universities', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]