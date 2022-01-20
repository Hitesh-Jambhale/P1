# Generated by Django 4.0.1 on 2022-01-18 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrevLoan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=50)),
                ('branch_name', models.CharField(max_length=50)),
                ('account_no', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=11)),
                ('micr_code', models.CharField(max_length=9)),
                ('loan_amount', models.FloatField()),
                ('loan_type', models.CharField(choices=[('PERSONAL', 'Personal'), ('VEHICLE', 'Vehicle'), ('HOME', 'Home')], max_length=10)),
                ('loan_tenure', models.FloatField()),
                ('amount_paid', models.FloatField()),
                ('amount_remaining', models.FloatField()),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Customer.customer')),
            ],
        ),
    ]
