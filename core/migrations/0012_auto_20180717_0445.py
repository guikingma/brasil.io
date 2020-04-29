# Generated by Django 2.0.3 on 2018-07-17 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0011_field_last_update"),
    ]

    operations = [
        migrations.AddField(
            model_name="field", name="description", field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="field",
            name="type",
            field=models.CharField(
                choices=[
                    ("binary", "binary"),
                    ("bool", "bool"),
                    ("date", "date"),
                    ("datetime", "datetime"),
                    ("decimal", "decimal"),
                    ("email", "email"),
                    ("float", "float"),
                    ("integer", "integer"),
                    ("json", "json"),
                    ("string", "string"),
                    ("text", "text"),
                ],
                max_length=15,
            ),
        ),
    ]
