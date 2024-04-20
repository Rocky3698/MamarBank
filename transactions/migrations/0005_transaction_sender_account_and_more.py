# Generated by Django 5.0.4 on 2024-04-12 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_bank_balance'),
        ('transactions', '0004_transaction_receiver_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='sender_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='accounts.userbankaccount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='receiver_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='accounts.userbankaccount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.IntegerField(choices=[(1, 'Deposite'), (2, 'Withdrawal'), (3, 'Loan'), (4, 'Loan Paid'), (5, 'Send Money')], null=True),
        ),
    ]