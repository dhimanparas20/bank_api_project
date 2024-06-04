from rest_framework import serializers
from .models import Bank, Branch

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ['name']

class BranchSerializer(serializers.ModelSerializer):
    bank_name = serializers.CharField(source='bank.name', read_only=True)

    class Meta:
        model = Branch
        fields = ['bank_name', 'branch', 'ifsc']
