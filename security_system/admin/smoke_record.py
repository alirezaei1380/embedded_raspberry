from django.contrib import admin
from ..models import SmokeRecord


@admin.register(SmokeRecord)
class SmokeRecordAdmin(admin.ModelAdmin):
    readonly_fields = (
        'time',
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(raspberry__admins__in=[request.user.id])
