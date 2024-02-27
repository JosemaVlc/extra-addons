from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import translate

def codigo_postal_mas_cercano(codigos_postales, codigo_postal_referencia, pais):
    # Crear un geolocalizador
    geolocalizador = Nominatim(user_agent="mi-aplicacion")

    # Obtener las coordenadas del código postal de referencia
    referencia = geolocalizador.geocode(codigo_postal_referencia + ", " + pais)
    coordenadas_referencia = (referencia.latitude, referencia.longitude)

    # Inicializar variables para el código postal más cercano y su distancia
    codigo_postal_mas_cercano = None
    distancia_minima = float('inf')

    # Iterar sobre la lista de códigos postales
    for cp in codigos_postales:
        # Obtener las coordenadas del código postal actual
        ubicacion_cp = geolocalizador.geocode(cp + ", " + pais)
        coordenadas_cp = (ubicacion_cp.latitude, ubicacion_cp.longitude)

        # Calcular la distancia entre el código postal actual y el de referencia
        distancia = geodesic(coordenadas_referencia, coordenadas_cp).kilometers

        # Actualizar el código postal más cercano si se encuentra uno más cercano
        if distancia < distancia_minima:
            codigo_postal_mas_cercano = cp
            distancia_minima = distancia

    return codigo_postal_mas_cercano

def traducir():
    texto_traducido = translate.translator('es', 'en', 'hola')
    print(texto_traducido)



# Ejemplo de uso:
codigos_postales = ["46019", "46026", "46011", "46014"]
codigo_postal_referencia = "46100"
pais = "Spain"  # Aquí debes especificar el país
cp_cercano = codigo_postal_mas_cercano(codigos_postales, codigo_postal_referencia, pais)
print(f"El código postal más cercano a {codigo_postal_referencia} es {cp_cercano}.")
traducir()

