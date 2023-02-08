#!/usr/bin/env python
from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import json
from time import sleep
from wakeonlan import send_magic_packet
import requests
       
MAX_CONTAINERS = 3
IPRPI1 = "192.168.43.188"          #PIETRO: 192.168.43.188   #CASA LUCA: 192.168.1.180
MACRPI1 = "b8:27:eb:2d:cb:df"

IPRPI2 = "192.168.43.147"           #PIETRO: 192.168.43.147  #CASA LUCA: 192.168.1.80
MACRPI2 = "b8:27:eb:0d:0a:72"



class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
    
        return

    def do_POST(self):
        R1off = False
        R2off = False
        self.send_response(200)
        textByte = self.rfile.read(int(self.headers['Content-Length']))
        dataJson = json.loads(textByte.decode('utf-8'))
        self.end_headers()

        if dataJson["action"] == "TurnOff":
            if dataJson["RaspberryIP"] != None:    #RASPBERRY specificato
                try:
                    r = requests.post(f'http://{dataJson["RaspberryIP"]}:8000', data=textByte)
                    self.wfile.write("turn Off ".format(self.path).encode('utf-8'))
                except:
                    pass                
                return
            else:
                try:
                    r1 = requests.post(f'http://{IPRPI1}:8000', data=textByte)
                except:
                    pass
                try:
                    r2 = requests.post(f'http://{IPRPI2}:8000', data=textByte)
                except:
                    pass

                self.wfile.write("turn Off ".format(self.path).encode('utf-8'))
                return
        elif dataJson["action"] == "print":
                r1 = ""
                r2 = ""
                try:
                    r1 = requests.post(f'http://{IPRPI1}:8000', data=textByte)
                except:
                    pass
                try:
                    r2 = requests.post(f'http://{IPRPI2}:8000', data=textByte)
                except:
                    pass
                
                resp = f"RASPBERRY 1 - {IPRPI1}\n\n{r1}\nRASPBERRY 2 - {IPRPI2}\n\n{r2}"
                self.wfile.write(resp.encode('utf-8'))
                return

        try:
            r = requests.get(f'http://{IPRPI1}:8000')    #RASPBERRY 1
            print("RASP1")
            
            n1 = int(r.text)
            if n1<MAX_CONTAINERS:  #se c'è posto               
                r = requests.post(f'http://{IPRPI1}:8000', data=textByte)
                self.wfile.write(f"Eseguo il container sul Raspy 1 ({IPRPI1}) sulla porta {r.text}".format(self.path).encode('utf-8'))
                return
            else:
                print("R1FULL")
        except:
            R1off = True
            print("R1OFF")
            pass
        
        try:
            r = requests.get(f'http://{IPRPI2}:8000')    #RASPBERRY 2
            n2 = int(r.text)
            if n2<MAX_CONTAINERS:
                r = requests.post(f'http://{IPRPI2}:8000', data=textByte)

                self.wfile.write(f"Eseguo il container sul Raspy 2 ({IPRPI2}) sulla porta {r.text}".format(self.path).encode('utf-8'))
                return

        except:
            #R2off = True
            print("R2OFF")
            pass

        if R1off:    #RPI1 OFF 
            send_magic_packet(MACRPI1)
            sleep(5)
            r = requests.post(f'http://{IPRPI1}:8000', data=textByte)

            self.wfile.write(f"Eseguo il container sul Raspy 1 ({IPRPI1}) sulla porta {r.text}".format(self.path).encode('utf-8'))
        elif R2off:    #RPI2 OFF
            send_magic_packet(MACRPI2)
            sleep(5)
            r = requests.post(f'http://{IPRPI2}:8000', data=textByte)

            self.wfile.write(f"Eseguo il container sul Raspy 2 ({IPRPI2}) sulla porta {r.text}".format(self.path).encode('utf-8'))
        else:           #BOTH FULL
            print("SEGMENTATION FAULT")

            self.wfile.write("Segmentation Fault (spazio nei server non disponibile, riprova più tardi...)".format(self.path).encode('utf-8'))

        return

if __name__ == '__main__':
# Creiamo un oggetto HTTPServer che ascolterà sulla porta 8000
    server = HTTPServer(('', 8000), MyServer)
    print('Server in esecuzione...')
# Avvio server
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass