from django.shortcuts import render, redirect
from .models import AcademicClass, Day, TimeSlot, TimetableEntry
from .services import generate_timetable


def generate_timetable_view(request, class_id):
    generate_timetable(class_id)
    return redirect("view_timetable", class_id=class_id)


def view_timetable(request, class_id):
    academic_class = AcademicClass.objects.get(id=class_id)
    days = Day.objects.all()
    slots = TimeSlot.objects.all().order_by("start_time")

    timetable = {}

    for slot in slots:
        timetable[slot] = {}
        for day in days:
            entry = TimetableEntry.objects.filter(
                academic_class=academic_class,
                day=day,
                time_slot=slot
            ).first()
            timetable[slot][day] = entry

    context = {
        "academic_class": academic_class,
        "days": days,
        "slots": slots,
        "timetable": timetable
    }

    return render(request, "timetable/view_timetable.html", context)
