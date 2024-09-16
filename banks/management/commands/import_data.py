import os
from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Import bank and branch data from SQL file'

    def add_arguments(self, parser):
        parser.add_argument('sql_file', type=str, help='Path to the SQL file')

    def handle(self, *args, **options):
        sql_file = options['sql_file']
        
        if not os.path.exists(sql_file):
            self.stdout.write(self.style.ERROR(f'File not found: {sql_file}'))
            return

        with connection.cursor() as cursor:
            with open(sql_file, 'r') as f:
                sql_content = f.read()
                cursor.execute(sql_content)
        
        self.stdout.write(self.style.SUCCESS('Successfully imported data'))