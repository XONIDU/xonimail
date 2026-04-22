#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONIMAIL 2026 - Cliente de Gmail para Terminal
Optimizado para equipos de bajos recursos
Desarrollador: Darian Alberto Camacho Salas
Organizacion: XONIDU
"""

import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from pathlib import Path

class XONIMAIL:
    def __init__(self):
        self.token_file = self.get_token_path()
        self.token = None
        self.remitente = None
        
        self.load_token()
        self.welcome()
    
    def get_token_path(self):
        """Busca token.txt priorizando ~/.xonimail/ (sin sudo)"""
        
        home_token = os.path.join(os.path.expanduser("~"), '.xonimail', 'token.txt')
        if os.path.exists(home_token):
            return home_token
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        local_token = os.path.join(script_dir, 'token.txt')
        if os.path.exists(local_token):
            return local_token
        
        system_token = '/usr/share/xonimail/token.txt'
        if os.path.exists(system_token):
            return system_token
        
        home_legacy = os.path.join(os.path.expanduser("~"), 'xonimail', 'token.txt')
        if os.path.exists(home_legacy):
            return home_legacy
        
        return home_token
    
    def load_token(self):
        try:
            with open(self.token_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        self.token = line
                        break
        except FileNotFoundError:
            print(f"\n[ERROR] No se encuentra token.txt")
            print("[INFO] Gmail requiere una contraseña de aplicacion")
            print(f"[INFO] Crea token.txt en: {os.path.dirname(self.token_file)}")
            sys.exit(1)
        
        if not self.token:
            print("[ERROR] No hay token valido en token.txt")
            sys.exit(1)
    
    def welcome(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        print("=" * 60)
        print("                     XONIMAIL")
        print("=" * 60)
        print(" BY: XONIDU - Darian Alberto Camacho Salas")
        print("=" * 60)
        print(f" Token file: {self.token_file}")
        print("=" * 60)
        print("")
    
    def enviar_correos(self):
        # Solicitar remitente
        self.remitente = input("Tu correo Gmail: ").strip()
        while not self.remitente:
            print("El correo no puede estar vacio")
            self.remitente = input("Tu correo Gmail: ").strip()
        
        # Solicitar asunto
        asunto = input("\nAsunto del correo: ")
        if not asunto:
            asunto = "(Sin asunto)"
        
        # Solicitar mensaje multilinea
        print("\nEscribe tu mensaje (presiona ENTER dos veces para finalizar):")
        lineas = []
        while True:
            linea = input()
            if linea == "" and len(lineas) > 0 and lineas[-1] == "":
                break
            lineas.append(linea)
        cuerpo = "\n".join(lineas[:-1]) if lineas else ""
        
        # Solicitar destinatarios
        while True:
            try:
                num_destinos = input("\nCuantos destinatarios? (numero): ")
                num_destinos = int(num_destinos)
                if num_destinos > 0:
                    break
                else:
                    print("Debe ingresar al menos 1 destinatario")
            except ValueError:
                print("Por favor, ingresa un numero valido")
        
        destinatarios = []
        print(f"\nIngresa los {num_destinos} correos:")
        for i in range(num_destinos):
            while True:
                correo = input(f"  Destinatario {i+1}: ").strip()
                if correo:
                    destinatarios.append(correo)
                    break
                print("El correo no puede estar vacio")
        
        # Mostrar resumen
        print("\n" + "="*50)
        print("RESUMEN DE ENVIO")
        print("="*50)
        print(f"De: {self.remitente}")
        print(f"Asunto: {asunto}")
        print(f"Destinatarios: {len(destinatarios)}")
        for i, dest in enumerate(destinatarios, 1):
            print(f"   {i}. {dest}")
        print("\nMensaje:")
        print("-"*30)
        print(cuerpo)
        print("-"*30)
        
        confirmar = input("\nEnviar correos? (s/n): ").lower()
        if confirmar != 's' and confirmar != 'si':
            print("\nEnvio cancelado. Hasta luego!")
            return
        
        # Enviar correos
        print("\nIniciando envio... (CTRL+C para cancelar)")
        
        try:
            print("Conectando con servidor Gmail...")
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            
            print("Autenticando...")
            server.login(self.remitente, self.token)
            
            print("\nInicio de sesion exitoso. Enviando correos...\n")
            
            exitosos = 0
            fallidos = 0
            
            for i, destino in enumerate(destinatarios, 1):
                try:
                    msg = MIMEMultipart()
                    msg['From'] = self.remitente
                    msg['To'] = destino
                    msg['Subject'] = asunto
                    msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))
                    
                    server.send_message(msg)
                    print(f"[{i}/{len(destinatarios)}] Enviado a {destino}")
                    exitosos += 1
                    
                except Exception as e:
                    print(f"[{i}/{len(destinatarios)}] Error con {destino}: {e}")
                    fallidos += 1
            
            server.quit()
            
            print("\n" + "="*50)
            print("RESUMEN FINAL")
            print("="*50)
            print(f"Envios exitosos: {exitosos}")
            print(f"Envios fallidos: {fallidos}")
            print(f"Total procesados: {len(destinatarios)}")
            print("="*50)
            print("\nProceso completado! Gracias por usar XONIMAIL")
            
        except KeyboardInterrupt:
            print("\n\nProceso interrumpido por el usuario")
            try:
                server.quit()
            except:
                pass
            print("Hasta luego!")
        except Exception as e:
            print(f"\nError critico: {e}")
            print("\nPosibles soluciones:")
            print("  * Verifica que el token en token.txt sea correcto")
            print("  * Asegurate de tener activada la verificacion en dos pasos")
            print("  * Revisa tu conexion a internet")
    
    def run(self):
        self.enviar_correos()

def main():
    try:
        app = XONIMAIL()
        app.run()
    except KeyboardInterrupt:
        print("\n\nBY: XONIDU - Darian Alberto Camacho Salas")
        print("Hasta luego!")
    except EOFError:
        print("\n\nBY: XONIDU - Darian Alberto Camacho Salas")
        print("Hasta luego!")

if __name__ == "__main__":
    main()
