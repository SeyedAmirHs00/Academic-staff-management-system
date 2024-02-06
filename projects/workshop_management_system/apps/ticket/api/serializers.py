from rest_framework import serializers

from apps.ticket import models


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ticket
        fields = '__all__'
