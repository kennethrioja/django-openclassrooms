# Generated by Django 5.0.4 on 2024-05-09 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0010_remove_game_creator"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="creator",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="listings.player",
            ),
        ),
    ]
