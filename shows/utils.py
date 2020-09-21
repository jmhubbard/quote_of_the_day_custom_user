from shows.models import Show

#Returns a QuerySet of only active shows
def getActiveShows():
    return Show.objects.filter(is_active = True)
