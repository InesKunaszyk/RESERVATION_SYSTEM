from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=255, unique=True)
    capacity = models.SmallIntegerField()
    projector = models.BooleanField(default=False)

    def __str__(self):
        return (f"Nazwa sali: {self.name}, Wielkość: {self.capacity}, Rzutnik: {self.projector}")


class Reserve(models.Model):
    date = models.DateField()
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    comment = models.TextField(null=True)

    class Meta:
        unique_together = ('room_id', 'date')

    def __str__(self):
        return f"{self.date}, {self.room_id}, {self.comment}"

