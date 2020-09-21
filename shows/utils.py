from shows.models import Show
def getActiveShows():
    return Show.objects.filter(is_active = True)
