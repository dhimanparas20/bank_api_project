# banks/management/commands/import_banks.py

import csv
from django.core.management.base import BaseCommand
from bank.models import Bank, Branch

class Command(BaseCommand):
    help = 'Import bank data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row)  # Debugging: print each row to verify column names
                bank_name = row['bank_name']
                bank, created = Bank.objects.get_or_create(name=bank_name)
                
                Branch.objects.create(
                    ifsc=row['ifsc'],
                    bank_id=bank,
                    branch=row['branch'],
                    address=row['address'],
                    city=row['city'],
                    district=row['district'],
                    state=row['state'],
                    bank_name=bank_name
                )
            self.stdout.write(self.style.SUCCESS('Data imported successfully'))
