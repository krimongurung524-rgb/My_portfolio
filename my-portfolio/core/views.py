from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from projects.models import Project
from .models import Skill, Education
from .forms import ContactMessageForm


def home(request):
    return render(request, "pages/home.html", {
        "projects": Project.objects.all(),
        "skills": Skill.objects.all(),
        "education": Education.objects.all(),
    })


@require_POST
def contact(request):
    # Honeypot: hidden field, only bots fill it. Fake success, save nothing.
    if request.POST.get("website"):
        return JsonResponse({"ok": True, "message": "Thank you! Your message has been received."})

    form = ContactMessageForm(request.POST)
    if not form.is_valid():
        return JsonResponse(
            {"ok": False, "message": "Please fill in all fields with a valid email."},
            status=400,
        )

    msg = form.save()

    try:
        send_mail(
            subject=f"Portfolio message from {msg.name}",
            message=f"{msg.message}\n\nReply to: {msg.email}",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.DEFAULT_FROM_EMAIL],
            fail_silently=True,
        )
    except Exception:
        pass

    return JsonResponse({"ok": True, "message": f"Thank you, {msg.name}! Your message has been received."})
