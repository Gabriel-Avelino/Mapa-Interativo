from django.shortcuts import render
import folium
from opencage.geocoder import OpenCageGeocode

# Create your views here.

# Insira aqui sua chave de API do OpenCage
opencage_key = 'a5e06dcd00a54172bf18379c16c15c2a'

def index(request):
    address = request.POST.get('address')
    geocoder = OpenCageGeocode(opencage_key)

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
        country = result[0]['components'].get('country', 'Unknown')
        m = folium.Map(location=[lat, lng], zoom_start=16.0)
        folium.Marker([lat, lng], tooltip='Click for more', popup=country).add_to(m)
    else:
        # Se a localização não for encontrada, usa valores padrão (Brasil)
        lat, lng = -14.2350, -51.9253
        country = 'Brazil'
        m = folium.Map(location=[lat, lng], zoom_start=4.0)

    # Gerando a representação HTML do mapa para o template
    m = m._repr_html_()

    context = {
        'm': m,
    }

    return render(request, 'index.html', context)
