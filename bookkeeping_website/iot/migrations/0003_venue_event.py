# Generated by Django 3.2.3 on 2021-07-06 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iot', '0002_alter_event_light'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venue_Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Venue', models.CharField(max_length=10)),
                ('Date', models.DateField()),
                ('Time_st', models.TimeField()),
                ('Time_ed', models.TimeField()),
                ('Event', models.CharField(max_length=10)),
                ('Instructor', models.CharField(max_length=20)),
            ],
        ),
    ]
