# Generated by Django 5.0.4 on 2024-04-23 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0010_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Degree or certification title.', max_length=100)),
                ('degree_institution', models.CharField(help_text='Name of the degree and institution.', max_length=100)),
                ('start_year', models.IntegerField(help_text='Start year of the education period.')),
                ('end_year', models.IntegerField(help_text='End year of the education period.')),
            ],
        ),
    ]