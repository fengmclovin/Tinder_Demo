# models.py
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_images/')

# views.py
from django.shortcuts import render
from .models import User

def index(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def swipe(request, user_id, action):
    # Process swipe action (update preferences, matches, etc.)
    # For simplicity, this example just returns a response indicating the action
    return JsonResponse({'status': 'success', 'action': action, 'user_id': user_id})

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('swipe/<int:user_id>/<str:action>/', views.swipe, name='swipe'),
]

# index.html (simplified)
{% for user in users %}
    <div class="profile-card">
        <img src="{{ user.image.url }}" alt="{{ user.name }}">
        <h3>{{ user.name }}</h3>
        <p>Age: {{ user.age }}, Location: {{ user.location }}</p>
        <button class="swipe-left" onclick="swipe('{{ user.id }}', 'left')">Swipe Left</button>
        <button class="swipe-right" onclick="swipe('{{ user.id }}', 'right')">Swipe Right</button>
    </div>
{% endfor %}

<script>
    function swipe(userId, action) {
        fetch(`/swipe/${userId}/${action}/`)
            .then(response => response.json())
            .then(data => {
                console.log(data);  // Handle response (update UI, show next profile, etc.)
            });
    }
</script>
