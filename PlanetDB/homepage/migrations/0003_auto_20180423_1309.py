# Generated by Django 2.0.4 on 2018-04-23 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20180419_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='distance',
            field=models.FloatField(help_text='Enter distance from Sun in AU'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='name',
            field=models.CharField(help_text='Enter planet name', max_length=20, unique='TRUE'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='ordinality',
            field=models.IntegerField(help_text='Enter ordinality of planet', unique='TRUE'),
        ),
        migrations.AlterField(
            model_name='planet',
            name='size',
            field=models.FloatField(help_text='Enter size of planet in Earth Masses'),
        ),
    ]