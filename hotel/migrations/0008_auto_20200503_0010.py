# Generated by Django 3.0.5 on 2020-05-02 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0007_auto_20200502_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='room',
        ),
        migrations.AddField(
            model_name='booking',
            name='room_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hotel.Room'),
        ),
    ]
