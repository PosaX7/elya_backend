import csv
from django.core.management.base import BaseCommand
from programmes.models import Programme

class Command(BaseCommand):
    help = 'Importe les programmes depuis un fichier CSV'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Chemin du fichier CSV')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Programme.objects.create(
                    classe=row['classe'],
                    matiere=row['matiere'],
                    chapitre=row['chapitre'],
                    periode=row['periode'],
                    num_chapitre=int(row['num_chapitre'])
                )
        self.stdout.write(self.style.SUCCESS('✅ Importation terminée avec succès !'))
