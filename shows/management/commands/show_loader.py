from django.core.management.base import BaseCommand
from quotes.models import Episode, Show
from quotes.quotelist import quotelistdict

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Loads shows from quotes.quotelist.quotedictlist'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save shows to database')

    def handle(self, *args, **options):
        savedCount = 0
        duplicateCount = 0
        totalattempteditems = 0
        for item in quotelistdict:
            totalattempteditems += 1
            show = Show(
                name=item["show"],
                is_active=False
            )
            if options["save"]:
                try:
                    show.save()
                except IntegrityError:
                    duplicateCount += 1
                    continue
                else:
                    savedCount += 1
                    
        print(f'Total attempted shows: {totalattempteditems}')
        print(f"Skipped {duplicateCount} duplicate shows.")
        print(f"Saved: {savedCount} shows.")
        print(f"Total: {Show.objects.count()} shows in database.")
