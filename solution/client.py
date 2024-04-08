import requests
url="http://localhost:8000/"
ruta_post = url + "jugadores"
nuevo_jugador = {
    "player": "Juanito",
    "number": 23,
    "attempts":[],
    "genero":"Jugando",
}
post_response = requests.request(method="POST", url=ruta_post, json=nuevo_jugador)
print(post_response.text)
ruta_get = url + "jugadores"
get_response = requests.request(method="GET", url=ruta_get)
print(get_response.text)
#Busca por id
buscar_get=url+"jugadores/2"
bus_response=requests.request(method="GET",url=buscar_get)
print("Jugador buscado")
print(bus_response.text)
#Busca por nombre del jugador
dig_get=url+"jugadores?player=Juanito"
diagnostico_response=requests.request(method="GET",url=dig_get)
print("El jugador es:")
print(diagnostico_response.text)
#actualizar jugador
actu_jugador=url+"jugadores/2"
actualizar_jugador={
    "player":"Jose",
}
post_response=requests.request(method="GET",url=actu_jugador,json=actualizar_jugador)
print("Jugador Actualizado")
print(post_response.text)
#Eliminar partida
ruta_delete=url+"jugadores/1"
delete_response=requests.request(method="GET",url=ruta_delete)
print("Partida eliminada:")
print(delete_response.text)