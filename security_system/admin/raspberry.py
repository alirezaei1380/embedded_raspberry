import requests
from django.contrib import admin, messages

from ..models import Raspberry


@admin.register(Raspberry)
class RaspberryAdmin(admin.ModelAdmin):
    def send_data_to_raspberries(self, request, queryset):
        total_n_oks = []
        for single_raspberry in queryset.all():
            result = requests.post(
                # todo: change route
                f'http://{single_raspberry.ip}:8000/security-system/health-check/',
                {
                    'admin_code': single_raspberry.admin_code,
                    'user_code': single_raspberry.user_code,
                }
            )

            if not result.ok:
                total_n_oks.append(single_raspberry.ip)

        if len(total_n_oks):
            self.message_user(
                request,
                f'failed to send data to {",".join(total_n_oks)}. bot others has been sent',
                level=messages.ERROR,
            )
        else:
            self.message_user(
                request,
                'data successfully has been sent to all raspberries',
            )

    send_data_to_raspberries.description = 'Send data to raspberries'

    actions = [send_data_to_raspberries]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        self.send_data_to_raspberries(
            request,
            Raspberry.objects.filter(id=obj.id),
        )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(admins__in=[request.user.id])
