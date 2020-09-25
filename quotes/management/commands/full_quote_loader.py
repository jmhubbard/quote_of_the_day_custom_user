from django.core.management.base import BaseCommand
from quotes.models import Quote
from shows.models import Character, Episode, Show
from quotes.quotelist import quotelistdict

from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Creates quotes, shows, characters, and episodes from quotes.quotelist.quotedictlist'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save quotes, shows, characters, and episodes to the database')

    def handle(self, *args, **options):
        totalAttemptedItems = 0

        savedShowCount = 0
        duplicateShows = 0

        savedCharacterCount = 0
        duplicateCharacters = 0

        savedEpisodeCount = 0
        duplicateEpisodes = 0

        savedQuoteCount = 0
        duplicateQuotes = 0

        for item in quotelistdict:
            totalAttemptedItems += 1
            show = Show(
                name = item["show"],
                is_active = False,
            )
            if options["save"]:
                try:
                    show.save()
                except IntegrityError:
                    duplicateShows += 1
                    show = Show.objects.get(name=item["show"])
                else:
                    savedShowCount += 1
                finally:
                    episode = Episode(
                        name = item["episode"],
                        season = item["season"],
                        show = show
                    )
                    if options["save"]:
                        try:
                            episode.save()
                        except IntegrityError:
                            duplicateEpisodes += 1
                            episode = Episode.objects.get(
                                name=item["episode"],
                                season=item["season"],
                                show=show
                                )
                        else:
                            savedEpisodeCount += 1
                        finally:    
                            character = Character(
                                first_name = item["first_name"],
                                last_name = item["last_name"],
                                show = show
                            )
                            if options["save"]:
                                try:
                                    character.save()
                                except IntegrityError:
                                    duplicateCharacters += 1
                                    character = Character.objects.get(
                                        first_name = item["first_name"],
                                        last_name = item["last_name"],
                                        show = show
                                    )
                                else:
                                    savedCharacterCount += 1
                                finally:
                                    quote = Quote(
                                        text = item["quote"],
                                        speaker = character,
                                        episode = episode 
                                    )
                                    if options["save"]:
                                        try:
                                            quote.save()
                                        except IntegrityError:
                                            duplicateQuotes += 1
                                            # continue
                                        else:
                                            savedQuoteCount += 1
        

        print(f'Total attempted items: {totalAttemptedItems}')

        print(f'Total saved shows: {savedShowCount}')
        print(f'Skipped {duplicateShows} duplicated shows')

        print(f'Total saved characters: {savedCharacterCount}')
        print(f'Skipped {duplicateCharacters} duplicated characters')

        print(f'Total saved episodes: {savedEpisodeCount}')
        print(f'Skipped {duplicateEpisodes} duplicated episodes')

        print(f'Total saved quotes: {savedQuoteCount}')
        print(f'Skipped {duplicateQuotes} duplicated quotes')