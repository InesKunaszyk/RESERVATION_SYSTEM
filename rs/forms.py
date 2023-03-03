from django import forms
from django.forms import ModelForm, SelectDateWidget, ValidationError
from .models import *
import datetime


class AddRoom(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'projector']


class EditRoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'capacity', 'projector']


class RoomReservationForm(forms.ModelForm):
    class Meta:
        model= Reserve
        fields = ['date', 'comment']
        widgets = {
            'date': SelectDateWidget,
        }

        def clean(self):
            cleaned_data = super().clean()
            res_date = cleaned_data.get('date')

            today = datetime.date.today()
            if res_date < today:
                raise ValidationError('Booking in the past is not allowed')

            already_reserved = list(self.instance.room.reservations.filter(date=res_date))
            if len(already_reserved) > 0:
                raise ValidationError(f'The room is already booked on {res_date}')
