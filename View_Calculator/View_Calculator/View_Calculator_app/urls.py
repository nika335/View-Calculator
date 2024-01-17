from django.urls import path
from View_Calculator_app.views import odd_or_even

urlpatterns = [
    path('even_or_odd/<int:number>', odd_or_even)
]
