# Generated by Django 5.0.7 on 2024-07-15 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0006_alter_plant_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
