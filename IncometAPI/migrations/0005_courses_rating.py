# Generated by Django 3.2.7 on 2022-06-23 18:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IncometAPI', '0004_alter_file_source_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_name', models.CharField(max_length=200, null=True)),
                ('courses_discriptions', models.CharField(max_length=800, null=True)),
                ('courses_start_date', models.CharField(max_length=200, null=True)),
                ('courses_end_date', models.CharField(max_length=200, null=True)),
                ('courses_pdf', models.FileField(blank=True, null=True, upload_to='images/')),
                ('courses_price', models.FloatField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('update_date', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_verify', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courses_rating', models.IntegerField(null=True)),
                ('review', models.CharField(max_length=200, null=True)),
                ('courses', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IncometAPI.courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]