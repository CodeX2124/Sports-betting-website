# Generated by Django 4.2.8 on 2024-02-24 08:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("api", "0006_comment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Bet",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("score1", models.IntegerField(blank=True, null=True)),
                ("score2", models.IntegerField(blank=True, null=True)),
                ("points", models.IntegerField(blank=True, default=None, null=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="bets",
                        to="api.event",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_bets",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "unique_together": {("user", "event")},
                "index_together": {("user", "event")},
            },
        ),
    ]
