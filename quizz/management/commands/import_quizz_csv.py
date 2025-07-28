import csv
from django.core.management.base import BaseCommand
from quizz.models import (
    QuizCategory,
    QuizSubGroup,
    DifficultyLevel,
    Quiz,
    QuizQuestion,
    QuizAnswer
)

class Command(BaseCommand):
    help = 'Importe les questions à partir d’un fichier CSV structuré'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        csv_file = options['csv_file']

        try:
            with open(csv_file, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                for row in reader:
                    # Récupération ou création de la catégorie
                    category, _ = QuizCategory.objects.get_or_create(name=row['categorie'])

                    # Récupération ou création du sous-groupe
                    subgroup, _ = QuizSubGroup.objects.get_or_create(name=row['sous_groupe'], category=category)

                    # Récupération ou création du niveau de difficulté
                    difficulty, _ = DifficultyLevel.objects.get_or_create(level=int(row['niveau']))

                    # Création ou récupération du quiz
                    quiz, _ = Quiz.objects.get_or_create(
                        title=row['quizz'],
                        category=category,
                        subgroup=subgroup,
                        difficulty=difficulty
                    )

                    # Création de la question
                    question = QuizQuestion.objects.create(
                        quiz=quiz,
                        text=row['question'],
                        correct_answer_number=int(row['bonne_reponse'])
                    )

                    # Création des réponses (1 à 4)
                    for i in range(1, 5):
                        QuizAnswer.objects.create(
                            question=question,
                            text=row[f'reponse_{i}'],
                            number=i
                        )

                    self.stdout.write(self.style.SUCCESS(f"✔ Question importée : {question.text}"))

        except Exception as e:
            self.stderr.write(self.style.ERROR(f"❌ Erreur inattendue : {e}"))
