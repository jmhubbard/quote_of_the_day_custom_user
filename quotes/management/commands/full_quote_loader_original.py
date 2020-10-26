from django.core.management.base import BaseCommand
from quotes.models import Quote
from shows.models import Character, Episode, Show
from quotes.quotelist_withoutmovies import quotelistdict

from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Creates quotes, shows, characters, and episodes from quotes.quotelist.quotedictlist'

    def add_arguments(self, parser):
        parser.add_argument('--save', action='store_true', help='Save quotes, shows, characters, and episodes to the database')

    def handle(self, *args, **options):
        totalAttemptedItems = 0
        #Show Counts
        savedShowCount = 0
        duplicateShows = 0
        #Character Counts
        savedCharacterCount = 0
        duplicateCharacters = 0
        #Episode Counts
        savedEpisodeCount = 0
        duplicateEpisodes = 0
        #Quote Counts
        savedQuoteCount = 0
        duplicateQuotes = 0

        for item in quotelistdict:
            totalAttemptedItems += 1
            #Create an instance of Show using the provided show name
            show = Show(
                name = item["show"],
                is_active = False,
            )
            if options["save"]:
                try:
                    #Save the show instance if it doesn't exist in database
                    show.save()
                except IntegrityError:
                    #If the show already exists then get that shows object to use when saving episodes
                    duplicateShows += 1
                    show = Show.objects.get(name=item["show"])
                else:
                    savedShowCount += 1
                finally:
                    #Create an instance of Episode using the provided episode name, season and the previous show instance
                    episode = Episode(
                        name = item["episode"],
                        season = item["season"],
                        show = show
                    )
                    try:
                        episode.save()
                    except IntegrityError:
                        #If the episode already exists then get that episodes object to use when saving character
                        duplicateEpisodes += 1
                        episode = Episode.objects.get(
                            name=item["episode"],
                            season=item["season"],
                            show=show
                            )
                    else:
                        savedEpisodeCount += 1
                    finally:
                        #Create an instance of Character using the provided first name, last name, and previous show object
                        character = Character(
                            first_name = item["first_name"],
                            last_name = item["last_name"],
                            show = show
                        )
                        try:
                            character.save()
                        except IntegrityError:
                            #If the Character already exists then get that character object to use when saving quote
                            duplicateCharacters += 1
                            character = Character.objects.get(
                                first_name = item["first_name"],
                                last_name = item["last_name"],
                                show = show
                            )
                        else:
                            savedCharacterCount += 1
                        finally:
                            #Create an instance of Quote using the provided quote text, the previous character, and the previous episode
                            quote = Quote(
                                text = item["quote"],
                                speaker = character,
                                episode = episode 
                            )
                            try:
                                quote.save()
                            except IntegrityError:
                                duplicateQuotes += 1
                                # continue
                            else:
                                savedQuoteCount += 1
    

        print(f'Total attempted items: {totalAttemptedItems}')
        #Final Show Counts
        print(f'Total saved shows: {savedShowCount}')
        print(f'Skipped {duplicateShows} duplicated shows')
        #Final Character Counts
        print(f'Total saved characters: {savedCharacterCount}')
        print(f'Skipped {duplicateCharacters} duplicated characters')
        #Final Episode Counts
        print(f'Total saved episodes: {savedEpisodeCount}')
        print(f'Skipped {duplicateEpisodes} duplicated episodes')
        #Final Quote Counts
        print(f'Total saved quotes: {savedQuoteCount}')
        print(f'Skipped {duplicateQuotes} duplicated quotes')
