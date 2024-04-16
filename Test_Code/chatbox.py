# models.py
from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Message

@login_required
def chat(request, receiver_id):
    receiver = get_object_or_404(User, pk=receiver_id)
    messages = Message.objects.filter(sender=request.user, receiver=receiver) | \
               Message.objects.filter(sender=receiver, receiver=request.user)
    return render(request, 'chat.html', {'receiver': receiver, 'messages': messages})

@login_required
def send_message(request, receiver_id):
    if request.method == 'POST':
        receiver = get_object_or_404(User, pk=receiver_id)
        content = request.POST.get('content')
        message = Message(sender=request.user, receiver=receiver, content=content)
        message.save()
    return redirect('chat', receiver_id=receiver_id)

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('chat/<int:receiver_id>/', views.chat, name='chat'),
    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),
]

# chat.html (simplified)
{% for message in messages %}
    {% if message.sender == request.user %}
        <div class="message sent">
            <p>{{ message.content }}</p>
            <span>{{ message.timestamp }}</span>
        </div>
    {% else %}
        <div class="message received">
            <p>{{ message.content }}</p>
            <span>{{ message.timestamp }}</span>
        </div>
    {% endif %}
{% endfor %}

<form action="{% url 'send_message' receiver_id=receiver.id %}" method="post">
    {% csrf_token %}
    <input type="text" name="content" placeholder="Type your message...">
    <button type="submit">Send</button>
</form>
