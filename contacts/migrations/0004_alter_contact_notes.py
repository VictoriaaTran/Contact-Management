# Generated by Django 4.2.7 on 2023-11-15 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0003_alter_contact_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="notes",
            field=models.TextField(blank="True", default="", max_length=200),
        ),
    ]