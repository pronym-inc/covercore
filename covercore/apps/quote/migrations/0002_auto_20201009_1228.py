# Generated by Django 3.0.7 on 2020-10-09 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pronym_api', '0010_auto'),
        ('quote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workerscompensationquoterequest',
            name='api_account',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers_compensation_quote_requests', to='pronym_api.ApiAccount'),
        ),
    ]
