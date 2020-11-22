from django.contrib import admin


from .models import Supplier, Inventory, Transaction

admin.site.site_header = 'TekTile Admin Panel'
admin.site.register(Supplier)
admin.site.register(Inventory)
admin.site.register(Transaction)
