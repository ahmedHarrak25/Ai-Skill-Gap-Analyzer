from django.shortcuts import render

def sidebar_preview_view(request):
    return render(request, 'base_preview.html')