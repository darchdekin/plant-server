# Generated by Django 5.0.7 on 2024-07-14 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0005_alter_plant_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='name',
            field=models.CharField(blank=True, default='', max_length=128),
        ),
    ]
