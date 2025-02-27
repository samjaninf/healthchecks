# Generated by Django 1.11.6 on 2017-12-27 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0033_auto_20170714_1715")]

    operations = [
        migrations.AlterField(
            model_name="channel",
            name="kind",
            field=models.CharField(
                choices=[
                    ("email", "Email"),
                    ("webhook", "Webhook"),
                    ("hipchat", "HipChat"),
                    ("slack", "Slack"),
                    ("pd", "PagerDuty"),
                    ("pagertree", "PagerTree"),
                    ("po", "Pushover"),
                    ("pushbullet", "Pushbullet"),
                    ("opsgenie", "OpsGenie"),
                    ("victorops", "VictorOps"),
                    ("discord", "Discord"),
                    ("telegram", "Telegram"),
                    ("sms", "SMS"),
                ],
                max_length=20,
            ),
        )
    ]
