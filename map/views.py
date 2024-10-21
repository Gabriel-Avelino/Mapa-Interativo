from django.shortcuts import render
from opencage.geocoder import OpenCageGeocode
from django.http import JsonResponse
from .models import Horario
from django.views.decorators.http import require_GET

# Chave API do OpenCage
opencage_key = 'a5e06dcd00a54172bf18379c16c15c2a'
geocoder = OpenCageGeocode(opencage_key)

def index(request):
    address = request.POST.get('address')  # Usa 'Brazil' como valor padrão
    if address == None:
        address = "Brasil"
    result = geocoder.geocode(address)

    if result:
        lat = result[0]['geometry']['lat']
        lng = result[0]['geometry']['lng']
        if 'road' in result[0]['components']:
            location = result[0]['components']['road']
            zoom = 16  # Zoom mais próximo para estrada
        elif 'municipality' in result[0]['components']:
            location = result[0]['components']['municipality']
            zoom = 12  # Zoom intermediário para cidade
        elif 'state' in result[0]['components']:
            location = result[0]['components']['state']
            zoom = 6  # Zoom mais afastado para estado
        elif 'country' in result[0]['components']:
            location = result[0]['components']['country']
            zoom = 4  # Zoom mais afastado para país
        else:
            location = result[0]['formatted']
            zoom = 4

    else:
        lat, lng, zoom = -14.2350, -51.9253, 4  # Coordenadas padrão do Brasil
        location = "Brasil"

    # Substituição do request.is_ajax()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({
            'lat': lat,
            'lng': lng,
            'zoom': zoom,
            'location': location
        })

    # Renderiza a página HTML com os dados iniciais
    context = {
        'lat': lat,
        'lng': lng,
        'zoom': zoom,
        'location': location
    }

    return render(request, 'index.html', context)

@require_GET
def get_hours(request):
    address = request.GET.get('address')
    
    if not address:
        return JsonResponse({'error': 'Dados incompletos'}, status=400)
    
    horarios = list(Horario.objects.filter(address = address).values('id', 'address', 'segunda_diurno', 'segunda_noturno', 'terca_diurno', 'terca_noturno', 'quarta_diurno', 'quarta_noturno', 'quinta_diurno', 'quinta_noturno', 'sexta_diurno', 'sexta_noturno', 'sabado_diurno', 'sabado_noturno', 'domingo_diurno', 'domingo_noturno'))
    
    return JsonResponse({'horarios': horarios})
                        