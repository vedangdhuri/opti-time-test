from timetable.models import (
    AcademicClass, Day, TimeSlot, Subject,
    Room, Batch, TimetableEntry
)
from itertools import cycle


def generate_timetable(academic_class_id):
    academic_class = AcademicClass.objects.get(id=academic_class_id)

    days = Day.objects.all()
    slots = TimeSlot.objects.all().order_by("start_time")
    subjects = Subject.objects.filter(subject_type="THEORY")
    rooms = Room.objects.all()

    subject_cycle = cycle(subjects)
    room_cycle = cycle(rooms)

    # Clear old timetable
    TimetableEntry.objects.filter(academic_class=academic_class).delete()

    for day in days:
        for slot in slots:
            # Skip break slots
            if slot.start_time.strftime("%H:%M") in ["12:00", "14:45"]:
                TimetableEntry.objects.create(
                    academic_class=academic_class,
                    day=day,
                    time_slot=slot,
                    is_break=True
                )
                continue

            subject = next(subject_cycle)
            room = next(room_cycle)

            TimetableEntry.objects.create(
                academic_class=academic_class,
                day=day,
                time_slot=slot,
                subject=subject,
                room=room
            )
