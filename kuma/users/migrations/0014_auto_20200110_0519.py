# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-01-10 05:19
from __future__ import unicode_literals

from django.db import migrations


def create_subscription_waffle_flag(apps, schema_editor):
    Flag = apps.get_model("waffle", "Flag")
    Flag.objects.get_or_create(
        name="subscription", staff=True, note="Show stripe subscription form"
    )


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0014_user_is_newsletter_subscribed"),
    ]

    operations = [migrations.RunPython(create_subscription_waffle_flag)]
