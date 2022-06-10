# Create your views here.
from django.shortcuts import render, redirect
from .forms import FeedbackForm
from .models import Feedback
from django.contrib import messages

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, f"Su comentario ha sido publicado, muchas gracias!")
            return redirect("feedback")
            

    form = FeedbackForm()

    context = {
        'form': form,
        'feedbacks': Feedback.objects.all().values()
    }

    return render(request, 'feedback/feedback.html', context)
