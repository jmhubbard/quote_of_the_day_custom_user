from django.core.management.base import BaseCommand
from quotes.models import Quote
from shows.models import Character, Episode, Show
from users.models import User
from subscriptions.models import Subscription
import random
from emails.utils import email_test

from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Sends out a daily random quote that the user is subscribed to'

    # def add_arguments(self, parser):
    #     parser.add_argument('--save', action='store_true', help='Save quotes, shows, characters, and episodes to the database')

    def handle(self, *args, **options):
        active_shows = Show.objects.filter(is_active = True)
        show_list = []
        for item in active_shows:
            show_list.append(item.name)

        random.shuffle(show_list)

        
        for show in show_list:
            show_quotes = Quote.objects.filter(episode__show__name = show)
            random_quote = random.choice(show_quotes)
            quote_email = f"{random_quote.text} - by {random_quote.speaker}.\n{random_quote.episode.show.name} Season: {random_quote.episode.season} {random_quote.episode.name}"
            current_subscribers = User.objects.filter(subscription__show__name = show, subscription__status = 1)
            for user in current_subscribers:

                email_test(user.email, quote_email)
                # print(user.email, random_quote.text, random_quote.speaker, random_quote.episode.name, random_quote.episode.season, random_quote.episode.show.name)
    