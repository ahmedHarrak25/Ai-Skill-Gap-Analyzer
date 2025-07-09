from django.shortcuts import render, redirect 
from .models import CustomUser
from django.http import JsonResponse
def team_list_view(request):

    team_members = CustomUser.objects.filter(is_superuser=False)
    context = {
        'team_members': team_members
    }
    
    
    return render(request, 'users/team_list.html', context)

def add_user_view(request):
    if request.method == 'POST':
        # Get data from the form
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # ... get other fields ...
        role = request.POST.get('role')
        position = request.POST.get('position')
        department = request.POST.get('department')
        phone = request.POST.get('phone')

        # --- SERVER-SIDE VALIDATION ---
        # Check if user with this email already exists
        if CustomUser.objects.filter(email=email).exists():
            return JsonResponse({'status': 'error', 'message': 'A user with this email already exists.'}, status=400)

        # Check for required fields
        if not all([first_name, last_name, email, password]):
             return JsonResponse({'status': 'error', 'message': 'Missing required fields.'}, status=400)

        # If all checks pass, create the user
        try:
            CustomUser.objects.create_user(
                username=email,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name,
                role=role,
                position=position,
                department=department,
                phone=phone
            )
            # Send back a success message
            return JsonResponse({'status': 'success', 'message': 'User created successfully!'})
        except Exception as e:
            # Catch any other potential errors during user creation
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    # If request.method is GET, just show the form
    return render(request, 'users/add_user.html')


# Create your views here.
