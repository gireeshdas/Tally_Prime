# Generated by Django 4.1 on 2023-09-20 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_bank_transactions_contra_particular_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal_particulars',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies'),
        ),
    ]
