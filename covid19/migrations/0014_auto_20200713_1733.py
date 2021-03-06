# Generated by Django 3.0.5 on 2020-07-13 20:33

from django.db import migrations
from django.conf import settings


def create_covid19_auto_import_user(apps, schema_editor):
    User = apps.get_model("auth", "User")
    StateSpreadsheet = apps.get_model("covid19", "StateSpreadsheet")

    auto_user = User.objects.create(username=settings.COVID19_AUTO_IMPORT_USER)
    for sp in StateSpreadsheet.objects.filter(automatically_created=True).select_related("user"):
        warnings = sp.data["warnings"]
        warnings.insert(0, f"Importação automática disparada por {sp.user.username}")
        sp.data["warnings"] = warnings
        sp.user = auto_user
        sp.save()


class Migration(migrations.Migration):

    dependencies = [
        ("covid19", "0013_auto_20200713_1721"),
        ("auth", "0011_update_proxy_permissions"),
    ]

    operations = [
        migrations.RunPython(create_covid19_auto_import_user),
    ]
