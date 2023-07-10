# Generated by Django 4.2.3 on 2023-07-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_pages', '0002_delete_teamforcompany'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamOfCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(max_length=256)),
                ('designation', models.CharField(max_length=256)),
                ('photo', models.ImageField(upload_to='Photo_For_Company_teams/%y/%m/%d')),
                ('facebook_url', models.URLField(max_length=120)),
                ('google_plus', models.URLField(max_length=120)),
                ('linkedn_url', models.URLField(max_length=120)),
                ('twitter_url', models.URLField(max_length=120)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
    ]
