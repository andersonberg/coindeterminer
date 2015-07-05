from django.contrib import admin
from solution.models import Coin


class CoinAdmin(admin.ModelAdmin):
    pass

admin.site.register(Coin, CoinAdmin)
