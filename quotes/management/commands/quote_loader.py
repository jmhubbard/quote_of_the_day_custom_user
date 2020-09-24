from django.core.management.base import BaseCommand
from quotes.models import Character, Episode, Quote
from quotes.quotelist import quotelistdict

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Loads quotes from quotes.quotelist.quotedictlist'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save quotes to the database')

    def handle(self, *args, **options):
        savedCount = 0
        duplicateCount = 0
        totalattempteditems = 0
        character_does_not_exist = []
        episode_does_not_exist = []
        for item in quotelistdict:
            totalattempteditems += 1
            try:
                character = Character.objects.get(first_name=item["first_name"], last_name=item["last_name"])
            except ObjectDoesNotExist:
                character_does_not_exist.append(item)
            else:
                try:
                    episode = Episode.objects.get(name=item["episode"])
                except ObjectDoesNotExist:
                    episode_does_not_exist.append(item)
                else:
                    quote = Quote(
                        text=item["quote"],
                        speaker=character,
                        episode=episode
                    )
                    if options["save"]:
                        try:
                            quote.save()
                        except IntegrityError:
                            duplicateCount += 1
                            continue
                        else:
                            savedCount += 1
                    
        print(f'Character does not exist in database for the following: {character_does_not_exist}')
        print(f'Episdoe does not exist in database for the following: {episode_does_not_exist}')
        print(f'Total attempted quotes: {totalattempteditems}')
        print(f"Skipped {duplicateCount} duplicate quotes.")
        print(f"Saved: {savedCount} quotes.")
        print(f"Total: {Quote.objects.count()} quotes in database.")