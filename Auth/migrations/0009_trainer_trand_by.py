# Generated by Django 3.2.7 on 2022-04-28 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0008_trainer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='trand_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.languages'),
        ),
    ]
