from django.core.management.base import BaseCommand
from quotes.models import Quote
from shows.models import Character, Episode, Show
from users.models import User
from subscriptions.models import Subscription
import random
from emails.utils import email_test
from emails.models import EmailTracker
from datetime import date, timedelta, datetime
from emails.utils import email_daily_quote

from django.db import IntegrityError

class Command(BaseCommand):
    help = 'Sends out a daily random quote that the user is subscribed to'

    # def add_arguments(self, parser):
    #     parser.add_argument('--save', action='store_true', help='Save quotes, shows, characters, and episodes to the database')

    def handle(self, *args, **options):
        #Filters show objects to get current active shows and puts the show names in an array labeled show_list. That array is then randomly
        #shuffled to change the order at which shows are iterated through.
        active_shows = Show.objects.filter(is_active = True)
        show_list = []
        for item in active_shows:
            show_list.append(item.name)

        random.shuffle(show_list)

        #For each show in show_list, all quotes for that show are filtered from all quotes, and one is choicen at random.
        for show in show_list:
            show_quotes = Quote.objects.filter(episode__show__name = show)
            random_quote = random.choice(show_quotes)
            quote_email = f"{random_quote.text} - by {random_quote.speaker}.\n{random_quote.episode.show.name} Season: {random_quote.episode.season} {random_quote.episode.name}"
            #Users are filtred by those that are subscribed to the current show. All subscribed users will be sent and email with the quote.
            current_subscribers = User.objects.filter(subscription__show__name = show, subscription__status = 1)
            for user in current_subscribers:
                today_date = date.today()
                users_last_email = EmailTracker.objects.get(user = user)
                if users_last_email.last_quote_email.date() != today_date:
                    email_daily_quote(quote_email, user.email)
                    users_last_email.last_quote_email = datetime.now()
                    users_last_email.save()