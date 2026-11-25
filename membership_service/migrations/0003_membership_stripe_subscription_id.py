from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('membership_service', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='stripe_subscription_id',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
