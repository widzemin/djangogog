# Generated by Django 3.1.7 on 2021-02-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_doctor_available_animal_race'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='grade',
            field=models.CharField(choices=[('DR', 'Doctor'), ('SDR', 'Super-doctor'), ('MDR', 'Mega-doctor')], default='DR', max_length=100),
        ),
    ]
