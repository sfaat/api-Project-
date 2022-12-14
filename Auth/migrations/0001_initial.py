# Generated by Django 3.2.7 on 2022-04-09 18:22

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=200, unique=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('city_name', models.CharField(max_length=200)),
                ('city_code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Interests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('salutation', models.CharField(max_length=30, null=True)),
                ('first_name', models.CharField(max_length=150, null=True)),
                ('last_name', models.CharField(max_length=150, null=True)),
                ('about', models.TextField(null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatar/')),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='coverPicture/')),
                ('posts_count', models.IntegerField(blank=True, null=True)),
                ('followers_count', models.IntegerField(blank=True, null=True)),
                ('following_count', models.IntegerField(blank=True, null=True)),
                ('skills', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('enlarge_url', models.URLField(null=True)),
                ('date_of_birth', models.DateTimeField(null=True)),
                ('birth_place', models.CharField(max_length=500, null=True)),
                ('gender', models.CharField(max_length=20, null=True)),
                ('is_mail_verified', models.BooleanField(default=False)),
                ('verify_mail_code', models.TextField(blank=True, max_length=30, null=True)),
                ('is_public', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('working_from', models.DateTimeField()),
                ('working_till', models.DateTimeField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Auth.city')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Work Places',
                'db_table': 'work_place',
            },
        ),
        migrations.CreateModel(
            name='SocialLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Social Links',
                'db_table': 'social_links',
            },
        ),
        migrations.CreateModel(
            name='MySkills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('skill', models.CharField(max_length=250)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MyProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('project_title', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('skills', models.TextField(null=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('team_size', models.IntegerField(null=True)),
                ('client_name', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'My Projects',
            },
        ),
        migrations.CreateModel(
            name='MyPlaces',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('place_name', models.CharField(max_length=200)),
                ('lat_long', models.CharField(max_length=200, null=True)),
                ('from_date', models.DateTimeField(null=True)),
                ('to_date', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'My Places',
                'db_table': 'place',
            },
        ),
        migrations.CreateModel(
            name='MyLanguage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('name', models.CharField(max_length=200)),
                ('read', models.CharField(max_length=200, null=True)),
                ('write', models.CharField(max_length=200, null=True)),
                ('speak', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Languages',
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='MyInterest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('interest_code', models.CharField(max_length=200)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'My Interest',
                'db_table': 'interest',
            },
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.batch')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Followers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('following', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='following', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('school_college_name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('session_from', models.DateTimeField(null=True)),
                ('session_to', models.DateTimeField(null=True)),
                ('attended_for', models.CharField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField(null=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('modified_by', models.IntegerField(blank=True, default=None, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('deleted_by', models.IntegerField(blank=True, default=None, null=True)),
                ('deleted_on', models.DateTimeField(blank=True, default=None, null=True)),
                ('message', models.TextField()),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Auth.batch')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
