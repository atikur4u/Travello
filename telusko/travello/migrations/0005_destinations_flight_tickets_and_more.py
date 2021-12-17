# Generated by Django 4.0 on 2021-12-16 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_alter_destinations_stars_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='Flight_tickets',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destinations',
            name='Guided_visits',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='destinations',
            name='Inclusive',
            field=models.CharField(choices=[('Partially Subsidized', 'Partially Subsidized'), ('All Inclusive', 'All Inclusive')], default='Partially Subsidized', max_length=20),
        ),
    ]
