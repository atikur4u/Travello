# Generated by Django 4.0 on 2021-12-11 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_image', models.ImageField(upload_to='pics')),
                ('spec_offer_text_center', models.BooleanField(default=False)),
                ('destination_title', models.CharField(max_length=30)),
                ('destination_subtitle', models.TextField()),
                ('destination_price', models.IntegerField()),
            ],
        ),
    ]
