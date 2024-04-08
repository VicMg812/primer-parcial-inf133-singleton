from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs
class Player:
    _instance=None
    # def __nuevojugador(cls,id)

# jugadores={}
class Game:
    def __init__(self):
        self.games={}
        self.game_id=1
        # self.game_player="Julian"
        # self.game_number=50
        # self.game_attempts=[]
        # self.game_status="En Progreso"
    def play(self,player_element):
        server_element=43
        player_element="number"
        if player_element ==server_element:
            result="Felicitaciones"
        elif(player_element>server_element):
            result="Numero adivinado menor"
        elif(player_element<server_element):
            result="Numero adivinado mayor"
        datos_jugador={
            "id":self.game_id,
            "jugador":self.player_element,
            "message":result
        }
        self.games[self.game_id]=game_data
        self.game_id+=1
        return game_data
jugadores=[
    {
        "id":1,
        "player":"Julian",
        "number":50,
        "attempts":[],
        "status":"En Progreso"
    },
]
class JuegosService:
    @staticmethod
    def crea_partida(self,data):
        data["id"]=len(jugadores)+1
        jugadores.append(data)
        return jugadores
    @staticmethod
    def busca_por_id(id):
        return next(
            (jugador for jugador in jugadores if jugador["id"]==ci),
            None,
        )
    @staticmethod
    def busca_nombre(player):
        return next(
            (jugador for jugador in jugadores if jugador["player"==player]),
            None,
        )
    @staticmethod
    def actualiza_jugador(id,data):
        jugador=JuegosService.busca_por_id(id)
        if jugador:
            jugador.update(data)
            return jugadores
        else:
            return None
    @staticmethod
    def eliminar_jugador():
        jugadores.clear()
        return jugadores
class HTTPResponseHandler:
    @staticmethod
    def handle_response(handler, status, data):
        handler.send_response(status)
        handler.send_header("Content-type", "application/json")
        handler.end_headers()
        handler.wfile.write(json.dumps(data).encode("utf-8"))
class PlayerHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)
        if parsed_path.path=="/jugadores":
            if "player" in query_params:
                player=query_params["player"][0]
                juagador_nombre=JuegosService.busca_nombre(player)
                if juagador_nombre !=[]:
                    HTTPResponseHandler.handle_response(
                        self,200,juagador_nombre
                    )
                else:
                    HTTPResponseHandler.handle_response(self,204,[])
        elif self.path.startswith("/jugadores"):
            id=int(self.path.split("/")[-1])
            jugador=JuegosService.busca_por_id(id)
            if jugador:
                HTTPResponseHandler.handle_response(self,200,[jugador])
            else:
                HTTPResponseHandler.handle_response(self,204,[])
        else:
            HTTPResponseHandler.handle_response(
                self,204,{"Error":"Ruta no existente"}
            )
    def do_POST(self):
        if self.path=="/jugadores":
            data=self.read_data()
            jugadores=JuegosService.crea_partida(data)
            HTTPResponseHandler.handle_response(self,201,jugadores)
        else:
            HTTPResponseHandler.handle_response(
                self,404,{"Error":"Ruta no existente"}
            )
    def do_PUT(self):
        if self.path.startswith("/jugadores/"):
            id=int(self.path.split("/")[-1])
            data=self.read_data()
            jugadores=JuegosService.actualiza_jugador(id,data)
            if jugadores:
                HTTPResponseHandler.handle_response(
                    self,404,{"Error":"Jugador no encontrado"}
                )
        else:
            HTTPResponseHandler.handle_response(
                self,404,{"Error":"Ruta no existente"}
            )
    def do_DELETE(self):
        if self.path=="/jugadores":
            jugadores=JuegosService.eliminar_jugador()
            HTTPResponseHandler.handle_response(self,200,jugadores)
        else:
            HTTPResponseHandler.handle_response(
                self,404,{"Error":"Ruta no existente"}
            )
    
    def read_data(self):
        content_length=int(self.headers["Content-Length"])
        data=self.rfile.read(content_length)
        data=json.loads(data.decode("utf-8"))
        return data

def main():
    global game
    game = Game()

    try:
        server_address = ("", 8000)
        httpd = HTTPServer(server_address, PlayerHandler)
        print("Iniciando servidor HTTP en puerto 8000...")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("Apagando servidor HTTP")
        httpd.socket.close()

if __name__ == "__main__":
    main()

