# Generated by Django 3.2.7 on 2022-07-01 09:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IncometAPI', '0010_bycourses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bycourses',
            name='courses',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses1', to='IncometAPI.courses'),
        ),
    ]