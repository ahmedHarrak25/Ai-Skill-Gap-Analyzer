from django.shortcuts import render
from .models import CustomUser
def team_list_view(request):

    team_members = CustomUser.objects.filter(is_superuser=False)
    context = {
        'team_members': team_members
    }
    
    
    return render(request, 'users/team_list.html', context)
# Create your views here.
