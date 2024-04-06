from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import CollaborateForm


def contact_me(request):
    """
    Renders the Contact page and handles collaboration form submissions.
    """
    try:
        contact = Contact.objects.latest('updated_on')
    except Contact.DoesNotExist:
        contact = None

    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                "Collaboration request has been sent successfully!"
            )
            return redirect('contact')
    else:
        collaborate_form = CollaborateForm()

    return render(
        request,
        "contact/contact.html",
        {
            "contact": contact,
            "collaborate_form": collaborate_form
        },
    )
