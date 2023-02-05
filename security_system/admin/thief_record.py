from django.contrib import admin
from ..models import ThiefRecord


@admin.register(ThiefRecord)
class ThiefRecordAdmin(admin.ModelAdmin):
    readonly_fields = (
        'time',
        'image',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(raspberry__admins__in=[request.user.id])
