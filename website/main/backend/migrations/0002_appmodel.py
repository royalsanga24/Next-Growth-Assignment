# Generated by Django 4.2.11 on 2024-04-29 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('entertaiment', 'Entertainment')], max_length=20)),
                ('sub_category', models.CharField(choices=[('social media', 'Social Media'), ('games', 'Games'), ('finance', 'Finance'), ('education', 'Education'), ('other', 'Other')], max_length=20)),
            ],
        ),
    ]
