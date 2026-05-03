from django.shortcuts import render
from .models import Department, TeamMember
# Create your views here.
def home(request):
    leader = TeamMember.objects.filter(is_leader=True).first()
    departments = Department.objects.all()

    return render(request, 'home.html', {
        'leader': leader,
        'departments': departments
    })

def join(request):
    return render(request, 'join.html')