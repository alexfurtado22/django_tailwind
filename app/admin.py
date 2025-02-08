from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Tour, UserProfile


class TourAdmin(admin.ModelAdmin):
    list_display = (
        "oringin_contry",
        "destination_country",
        "price",
        "create_at",
        "update_at",
    )
    date_hierarchy = "create_at"
    list_filter = ("status",)
    search_fields = ("destination_country", "comment")
    ordering = ("create_at",)
    readonly_fields = ("create_at", "update_at")


class CustomerUseAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "📝 Personal Info",
            {
                "classes": ("collapse",),
                "fields": ("first_name", "last_name"),
            },
        ),
        (
            "🔐 Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (
            "📅 Important Dates",
            {
                "classes": ("collapse",),
                "fields": ("last_login", "date_joined"),
            },
        ),
    )

    add_fieldsets = (
        (
            "➕ Add New User",
            {  # Title added
                "classes": ("wide", "collapse"),  # Made collapsible
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "first_name", "last_name", "username")
    ordering = ("email",)


admin.site.register(Tour, TourAdmin)
admin.site.register(UserProfile, CustomerUseAdmin)

# Register your models here.
