# Generated by Django 3.2 on 2021-05-04 13:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Job Category name', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cname', models.CharField(help_text='Company name', max_length=30)),
                ('contact', models.CharField(help_text='Contact information', max_length=200)),
                ('caddress', models.TextField(help_text='Company Address', max_length=1000)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True)),
            ],
            options={
                'ordering': ['cname'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of countries.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Level of Education e.g. Graduation.', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular book across whole library', primary_key=True, serialize=False)),
                ('location', models.CharField(help_text='Country name', max_length=200)),
                ('designation', models.CharField(help_text='Designation eg Developer, Full Stack', max_length=200)),
                ('date_loggedin', models.DateField(blank=True, null=True)),
                ('job_description', models.TextField(help_text='Add Job Description', max_length=2000)),
                ('job_type', models.CharField(blank=True, choices=[('FT', 'Full time'), ('PT', 'Part time'), ('IT', 'Internship')], default='FT', help_text='Type of job - Full Time/Part Time/Internship', max_length=2)),
                ('exp_required', models.CharField(choices=[('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 year'), ('6', '6 years'), ('7', '7 years'), ('8', '8 years')], max_length=1)),
                ('salary', models.CharField(blank=True, max_length=30)),
                ('url', models.URLField(blank=True, null=True)),
                ('last_date', models.DateField(blank=True, null=True)),
                ('is_published', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('a', 'Available'), ('c', 'Closed')], default='a', help_text='position availability', max_length=1)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_created', to='profiles.company')),
            ],
            options={
                'ordering': ['date_loggedin'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Select your Skills e.g. IT, Machine Learning', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='JobSeeker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(help_text='Enter your First Name', max_length=30)),
                ('mname', models.CharField(help_text='Enter your Middle Name', max_length=30)),
                ('lname', models.CharField(help_text='Enter your Last Name', max_length=30)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('address', models.TextField(help_text='Enter your Street Address', max_length=1000)),
                ('email', models.EmailField(error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True)),
                ('mobile', models.CharField(help_text='Enter your Mobile Number', max_length=10)),
                ('experience', models.CharField(choices=[('1', '1 year'), ('2', '2 years'), ('3', '3 years'), ('4', '4 years'), ('5', '5 year'), ('6', '6 years'), ('7', '7 years'), ('8', '8 years')], max_length=1)),
                ('status', models.CharField(choices=[('A', 'Applied'), ('V', 'Visting'), ('C', 'Confirm'), ('R', 'Rejected')], max_length=1)),
                ('date_registration', models.DateField(blank=True, null=True)),
                ('country', models.ManyToManyField(help_text='Select your Country', to='profiles.Country')),
                ('education', models.ManyToManyField(help_text='Select your education', to='profiles.Education')),
                ('skills', models.ManyToManyField(help_text='Select your skills', to='profiles.Skill')),
            ],
            options={
                'ordering': ['fname', 'lname'],
            },
        ),
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='job_applied', to='profiles.job')),
                ('jobSeeker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person_applied', to='profiles.jobseeker')),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ManyToManyField(help_text='Select your Country', to='profiles.Country'),
        ),
        migrations.CreateModel(
            name='BookmarkJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.job')),
                ('jobSeeker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.jobseeker')),
            ],
        ),
    ]
