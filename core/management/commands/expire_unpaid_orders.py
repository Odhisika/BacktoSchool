from django.core.management.base import BaseCommand
from orders.models import Order
from django.utils import timezone

class Command(BaseCommand):
    help = 'Expire unpaid orders older than 3 days'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_orders = Order.objects.filter(status='Pending Payment', created_at__lt=now - timezone.timedelta(days=3))

        for order in expired_orders:
            order.status = 'Expired'
            order.save()
            self.stdout.write(self.style.WARNING(f"Expired Order #{order.order_number}"))
        
        self.stdout.write(self.style.SUCCESS("Checked and expired overdue unpaid orders."))
