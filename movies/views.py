from django.shortcuts import render


def WatchListView(request):
    return render(request, 'index.html')