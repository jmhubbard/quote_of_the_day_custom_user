from django.core.management.base import BaseCommand
from quotes.models import Episode, Show
from quotes.quotelist import quotelistdict

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Loads episodes from quotes.quotelist.quotedictlist'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save episodes to database')

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
                print('hello')
            else:
                episode = Episode(
                    name=item["episode"],
                    season=item["season"],
                    show=show_name
                )
                if options["save"]:
                    try:
                        episode.save()
                    except IntegrityError:
                        duplicateCount += 1
                        continue
                    else:
                        savedCount += 1
                    
        print(f'Show does not exist in database for the follow: {show_does_not_exist}')
        print(f'Total attempted quotes: {totalattempteditems}')
        print(f"Skipped {duplicateCount} duplicate episodes.")
        print(f"Saved: {savedCount} episodes.")
        print(f"Total: {Episode.objects.count()} episodes.")
