from django.http import HttpResponse
from voyage.formulaire import FormContactAjout
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == "POST":
        print(request.POST)
        form = FormContactAjout(request.POST)
        # voyage_id = request.POST.get('voyage_id')
        if form.is_valid():
            
            form.save()
            return HttpResponse({'success': True})
        else:
            return HttpResponse({'form': form})

    return HttpResponse({'error': 'something happend'})
    
