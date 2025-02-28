# Generated by Django 4.2.2 on 2023-06-23 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("artistas", "0001_initial"),
        ("playlist", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("name", models.CharField(default="", max_length=250)),
                ("date", models.DateField(auto_now=True)),
                ("description", models.CharField(max_length=300, null=True)),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="artistas.artist",
                    ),
                ),
                (
                    "playlist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="playlist.playlist",
                    ),
                ),
            ],
        ),
    ]
