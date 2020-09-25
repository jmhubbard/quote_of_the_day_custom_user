from django.core.management.base import BaseCommand
from shows.models import Character, Show 
from quotes.quotelist import quotelistdict

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Loads characters from quotes.quotelist.quotedictlist'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save characters to database')

    def handle(self, *args, **options):
        savedCount = 0
        duplicateCount = 0
        totalattempteditems = 0
        show_does_not_exist = []
        for item in quotelistdict:
            totalattempteditems += 1
            try:
                show_name=Show.objects.get(name=item["show"])
            except ObjectDoesNotExist:
                show_does_not_exist.append(item)
            else:
                character = Character(
                    first_name=item["first_name"],
                    last_name=item["last_name"],
                    show=show_name
                )
                if options["save"]:
                    try:
                        character.save()
                    except IntegrityError:
                        duplicateCount += 1
                        continue
                    else:
                        savedCount += 1
                    
        print(f'Show does not exist in database for the following: {show_does_not_exist}')
        print(f'Total attempted characters: {totalattempteditems}')
        print(f"Skipped {duplicateCount} duplicate characters.")
        print(f"Saved: {savedCount} characters.")
        print(f"Total: {Character.objects.count()} episodes in database.")