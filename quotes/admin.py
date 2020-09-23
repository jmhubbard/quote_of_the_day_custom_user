from django.contrib import admin
from quotes.models import Quote
# Register your models here.

class QuoteAdmin(admin.ModelAdmin):

  
    list_display = (  
    'quote_text_abridged',
    'quotelength',
    'speaker_name',
    'episode',
    )

    list_filter = (  
    'speaker_name',
    'episode',
    )


    def quotelength(self, quote):
        return len(quote.text)



    def quote_text_abridged(self, quote):
        maxlength = 30
        if len(quote.text) <= maxlength:
            return quote.text
        else:
            # we return a string of length maxlength by slicing the string of maxlength - 1 
            # to account for the addition of the '…'
            return (quote.text[:maxlength-1] + '…' )
    quote_text_abridged.short_description = 'Abridged Quote'


admin.site.register(Quote, QuoteAdmin)
