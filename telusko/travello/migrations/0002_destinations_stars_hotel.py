# Generated by Django 4.0 on 2021-12-16 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='destinations',
            name='Stars_Hotel',
            field=models.CharField(choices=[('Five Star', '5 Star'), ('Four Star', '4 Star'), ('Three Star', '3 Star'), ('Two Star', '2 Star'), ('One Star', '1 Star'), ('zero Star', '0 Star')], default='Five Star', max_length=32),
        ),
    ]
