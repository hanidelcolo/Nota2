from django.shortcuts import redirect, render
from .models import ContactMessage

def contact(request):
    if request.method == "POST":
        name = request.POST.get("nombre", "").strip()
        email = request.POST.get("correo", "").strip()
        message = request.POST.get("mensaje", "").strip()
        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            return redirect("/contact/?enviado=1")
    return render(request, "core/contact.html", {
        'sent': request.GET.get("enviado") == "1",
    })

# Create your views here.
