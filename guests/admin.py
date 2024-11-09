from django.contrib import admin
from .models import Guest, Party, BringAlongMeal, DietOption, DrinkOption


class GuestInline(admin.TabularInline):
    model = Guest
    fields = ('name', 'email')


class PartyAdmin(admin.ModelAdmin):
    list_display = ('name', 'save_the_date_sent', 'invitation_sent', 'invitation_opened', 'any_guests_attending_wedding', 'any_guests_attending_brunch')
    list_filter = ('invitation_opened',)
    readonly_fields = ('invitation_opened',)
    inlines = [GuestInline]


class DietInline(admin.TabularInline):
    model = DietOption


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'party', 'email', 'is_attending_wedding', 'is_attending_brunch')
    list_filter = ('is_attending_wedding', 'is_attending_brunch')
    # inlines = [DietInline]


class BringAlongMealAdmin(admin.ModelAdmin):
    list_display = ('type', 'vergeben', 'wer_bringts_mit')
    # list_filter = ('still_needed',)

    def wer_bringts_mit(self, obj):
        return ", ".join([p.name for p in obj.parties.all()])
    
    def vergeben(self, obj):
        return f"{obj.assigned}/{obj.max_number}"


class DietAdmin(admin.ModelAdmin):
    pass


class DrinksAdmin(admin.ModelAdmin):
    pass


admin.site.register(Party, PartyAdmin)
admin.site.register(Guest, GuestAdmin)
admin.site.register(BringAlongMeal, BringAlongMealAdmin)
admin.site.register(DietOption, DietAdmin)
admin.site.register(DrinkOption, DrinksAdmin)
