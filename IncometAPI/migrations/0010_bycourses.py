# Generated by Django 3.2.7 on 2022-06-29 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IncometAPI', '0009_rename_file_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='ByCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_verify', models.BooleanField(default=False)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IncometAPI.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
