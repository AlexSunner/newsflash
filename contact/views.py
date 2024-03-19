from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import CollaborateForm

def contact_me(request):
    """
    Renders the Contact page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()
    
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Collaboration request received!")
            return redirect('contact')  # Redirect after successful form submission
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