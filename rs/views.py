from django.db.models import OuterRef, Exists

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect

from .models import Room, Reserve
from .forms import AddRoom, EditRoomForm, RoomReservationForm

import datetime


def start(request):
    return render(request, 'rs/base.html')


def show_rooms(request):
    rooms = Room.objects.all()
    context = {"rooms": rooms}
    return render (request, 'rs/show_rooms.html', context)


def add_room(request):
    if request.method == "GET":
        room_form = AddRoom()
        context = {
            "form": room_form,
            "text": "Dodaj salę",
        }
        return render(request, 'rs/add_room.html', context)
    elif request.method == "POST":
        room_form = AddRoom(request.POST)
        if room_form.is_valid():
            room_form.save()
            return redirect('show_rooms')
        else:
            return HttpResponse("Błąd. Taka sala już istnieje!")


def edit_room(request, room_id):
    room = get_object_or_404(Room, id =room_id)
    if request.method == 'GET':
        form = EditRoomForm(instance=room)
        context = {
            "form": form,
            "text": "Zachowaj zmiany",
                   }
        return render(request, "rs/add_room.html", context)
    elif request.method == "POST":
        form = EditRoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("show_rooms")


def room_details(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == "GET":
        context = {
            "room": room,
        }
        return render(request, "rs/details.html", context)


def delete_room(request, room_id):
    room = get_object_or_404(Room, pk=room_id)
    if request.method == "POST":
        room.delete()
        return redirect("show_rooms")
    else:
        context = {
            "room": room
        }
        return render(request, "rs/delete_room.html", context)


def add_reservation(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    if request.method == 'POST':
        form = RoomReservationForm(request.POST)
        form.instance.room = room
        if form.is_valid():
            form.save()
            return redirect("show_rooms")
    else:
        form = RoomReservationForm()
        context = {
            "form": form,
            "room": room,
        }
        return render(request, "rs/add_reservation.html", context)


def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(RoomReservationForm, pk=reservation_id)
    if request.method == "POST":
        reservation.delete()
        return redirect("show_rooms")
    else:
        context = {
            "reservation": reservation,
        }
        return render(request, "rs/cancel_reservation.html", context)


def room_list(request):
    rooms = Room.objects.order_by('name')
    if request.GET.get('filter', 'clear') == 'apply':
        filters = request.GET
        filter_name = filters.get('filter_name', '')
        filter_cap_from = int(filters.get('filter_cap_from', 0) or 0)
        filter_cap_to = int(filters.get('filter_cap_to', 0) or 0)
        filter_projector = bool(filters.get('filter_projector', False)) or False
        filter_date = filters.get('filter_date', '')
        if filter_date:
            filter_date = datetime.datetime.strptime(filter_date, '%Y-%m-%d')

        if filter_name:
            rooms = rooms.filter(name__contains=filter_name)
        if filter_cap_from:
            rooms = rooms.filter(capacity__gte=filter_cap_from)
        if filter_cap_to:
            rooms = rooms.filter(capacity__lte=filter_cap_to)
        if filter_projector:
            rooms = rooms.filter(projector=True)
        if filter_date:
            rooms = rooms.filter(
                ~Exists(
                    Reserve.objects.filter(
                        date=filter_date, room_id=OuterRef('pk')
                    )
                )
            )
    else:  # clear filters clicked
        filters = {
            'filter_name': '',
            'filter_cap_from': '',
            'filter_cap_to': '',
            'filter_projector': False,
        }
    context = {
        "rooms": rooms,
        "filter": filters
    }
    return render(request, "rs/show_rooms.html", context)