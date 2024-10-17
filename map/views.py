from django.shortcuts import render
import folium
from opencage.geocoder import OpenCageGeocode
from django.http import JsonResponse

# Insira aqui sua chave de API do OpenCage
opencage_key = 'a5e06dcd00a54172bf18379c16c15c2a'
geocoder = OpenCageGeocode(opencage_key)
def index(request):
    address = request.POST.get('address')


    # Faz a requisição ao OpenCage para o endereço
    if address == '' or address == None:
        firstAddress = 'Brazil'
        address = firstAddress
    else:
        firstAddress = ''
    result = geocoder.geocode(address)

    if result and len(result) and firstAddress != 'Brazil':
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
            location = 'Localização Desconhecida'
            zoom = 2  # Zoom muito afastado, pois o local não foi identificado corretamente

        # Cria o mapa com o zoom apropriado
        m = folium.Map(location=[lat, lng], zoom_start=zoom)
        folium.Marker([lat, lng], tooltip='Click for more', popup=location, draggable=True).add_to(m) 
         
    else:
        # Se a localização não for encontrada, usa valores padrão (Brasil)
        lat, lng = -14.2350, -51.9253
        m = folium.Map(location=[lat, lng], zoom_start=4.0)

    # Gerando a representação HTML do mapa para o template
    m = m._repr_html_()

    context = {
        'm': m,
    }

    return render(request, 'index.html', context)