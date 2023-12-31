# Generated by Django 4.1 on 2023-09-06 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0012_contra_voucher_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='contra_particulars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('particular_id', models.IntegerField(null=True)),
                ('particular', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.companies')),
                ('contra_voucher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.payment_voucher')),
            ],
        ),
    ]
