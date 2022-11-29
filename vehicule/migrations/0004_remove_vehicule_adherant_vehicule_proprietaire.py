# Generated by Django 4.1.2 on 2022-11-19 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adherant', '0001_initial'),
        ('vehicule', '0003_remove_vehicule_client_vehicule_adherant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='adherant',
        ),
        migrations.AddField(
            model_name='vehicule',
            name='proprietaire',
            field=models.ForeignKey(db_column='proprietaire_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='adherant.adherant'),
        ),
    ]