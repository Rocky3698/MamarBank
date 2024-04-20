from django import forms
from .models import Transaction
from accounts.models import UserBankAccount
class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'amount',
            'transaction_type'
        ]

    def __init__(self, *args, **kwargs):
        self.account = kwargs.pop('account') # account value ke pop kore anlam
        super().__init__(*args, **kwargs)
        self.fields['transaction_type'].disabled = True # ei field disable thakbe
        self.fields['transaction_type'].widget = forms.HiddenInput() # user er theke hide kora thakbe

    def save(self, commit=True):
        self.instance.account = self.account
        self.instance.balance_after_transaction = self.account.balance
        return super().save()


class DepositForm(TransactionForm):
    def clean_amount(self): # amount field ke filter korbo
        min_deposit_amount = 100
        amount = self.cleaned_data.get('amount') # user er fill up kora form theke amra amount field er value ke niye aslam, 50
        if amount < min_deposit_amount:
            raise forms.ValidationError(
                f'You need to deposit at least {min_deposit_amount} $'
            )

        return amount


class WithdrawForm(TransactionForm):

    def clean_amount(self):
        account = self.account
        min_withdraw_amount = 500
        max_withdraw_amount = 20000
        balance = account.balance # 1000
        amount = self.cleaned_data.get('amount')
        if amount < min_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at least {min_withdraw_amount} $'
            )

        if amount > max_withdraw_amount:
            raise forms.ValidationError(
                f'You can withdraw at most {max_withdraw_amount} $'
            )

        if amount > balance: # amount = 5000, tar balance ache 200
            raise forms.ValidationError(
                f'You have {balance} $ in your account. '
                'You can not withdraw more than your account balance'
            )

        return amount


class LoanRequestForm(TransactionForm):
    def clean_amount(self):
        amount = self.cleaned_data.get('amount')

        return amount

class SendMoneyForm(TransactionForm):
    class Meta:
        model = Transaction
        fields = ['receiver_account','amount','transaction_type']
    
    def clean_receiver_account(self):
        receiver_account_no = self.cleaned_data.get('receiver_account')
        try:
            receiver_account = UserBankAccount.objects.get(account_no=receiver_account_no)
        except UserBankAccount.DoesNotExist:
            raise forms.ValidationError("Receiver account does not exist.")
        return receiver_account.account_no

    def clean_amount(self):
        account = self.account
        min_send_money = 500
        max_send_money = 20000
        balance = account.balance
        amount = self.cleaned_data.get('amount')

        if amount < min_send_money:
            raise forms.ValidationError(f'You can send at least {min_send_money} $')

        if amount > max_send_money:
            raise forms.ValidationError(f'You can send at most {max_send_money} $')

        if amount > balance:
            raise forms.ValidationError(f'You have {balance} $ in your account. '
                                        'You cannot send more than your account balance')
        return amount
