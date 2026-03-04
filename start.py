#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import signal
import os

# -----------------------------------------------------------
# MANEJADOR PARA CTRL+C
# -----------------------------------------------------------
def signal_handler(sig, frame):
    print("\n\nSaliendo del programa... Hasta luego!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# -----------------------------------------------------------
# FUNCION PARA MANEJO DE TOKENS
# -----------------------------------------------------------
def obtener_token():
    """Obtiene el token de token.txt o solicita crear el archivo"""
    archivo_token = "token.txt"
    
    # Verificar si existe el archivo
    if os.path.exists(archivo_token):
        with open(archivo_token, 'r') as f:
            token = f.read().strip()
            if token:
                return token
            else:
                print("\nEl archivo token.txt esta vacio.")
    
    # Si no existe o esta vacio, mostrar instrucciones
    print("\n" + "="*60)
    print("ARCHIVO DE TOKEN NO ENCONTRADO O VACIO")
    print("="*60)
    print("\nGmail requiere una 'Contraseña de aplicacion' especial.")
    print("Debes crear un archivo 'token.txt' con tu token.")
    
    print("\nCOMO OBTENER TU CONTRASEÑA DE APLICACION:")
    print("  1. Ve a tu cuenta de Google: https://myaccount.google.com/")
    print("  2. Ve a 'Seguridad'")
    print("  3. Activa la 'Verificacion en dos pasos' (si no la tienes)")
    print("  4. Regresa a Seguridad y busca 'Contraseñas de aplicacion'")
    print("  5. Selecciona 'Correo' y 'Windows Computer'")
    print("  6. Copia la contraseña de 16 caracteres que se genera")
    
    print("\nCOMO CREAR EL ARCHIVO:")
    print("  1. Crea un archivo llamado 'token.txt' en la misma carpeta")
    print("  2. Pegas tu contraseña de aplicacion (solo el token, sin espacios)")
    print("  3. Guardas el archivo y ejecutas este programa nuevamente")
    
    print("\nEnlace directo: https://myaccount.google.com/apppasswords")
    print("="*60 + "\n")
    
    # Preguntar si quiere crear el archivo ahora
    respuesta = input("¿Quieres crear el archivo token.txt ahora? (s/n): ").lower()
    if respuesta == 's' or respuesta == 'si':
        token_nuevo = input("Pega tu token aqui: ").strip()
        if token_nuevo:
            with open(archivo_token, 'w') as f:
                f.write(token_nuevo)
            print("Token guardado en token.txt")
            return token_nuevo
        else:
            print("Token vacio. No se guardo nada.")
            print("Ejecuta el programa nuevamente cuando tengas el token.")
            sys.exit(1)
    else:
        print("\nEjecuta el programa nuevamente cuando tengas el archivo token.txt listo.")
        sys.exit(0)

# -----------------------------------------------------------
# FUNCION PARA MOSTRAR MENSAJE DE AYUDA
# -----------------------------------------------------------
def mostrar_ayuda():
    print("\n" + "="*50)
    print("XONIMAIL")
    print("="*50)
    print("Comandos disponibles:")
    print("  * CTRL+C - Salir del programa")
    print("  * ENTER - Continuar con el siguiente paso")
    print("\nPara enviar correos:")
    print("  1. El token se lee automaticamente de token.txt")
    print("  2. Ingresa tu correo Gmail")
    print("  3. Escribe el asunto y mensaje")
    print("  4. Agrega los destinatarios")
    print("="*50 + "\n")

# -----------------------------------------------------------
# CONFIGURACION INICIAL
# -----------------------------------------------------------

# Mostrar ayuda automaticamente
mostrar_ayuda()

# Obtener token
token = obtener_token()

# Solicitar credenciales
remitente = input("Tu correo Gmail: ").strip()
while not remitente:
    print("El correo no puede estar vacio")
    remitente = input("Tu correo Gmail: ").strip()

# Mostrar que el token se cargo correctamente
print("Token cargado desde token.txt")

# Solicitar datos del mensaje
asunto = input("\nAsunto del correo: ")
if not asunto:
    asunto = "(Sin asunto)"

print("\nEscribe tu mensaje (presiona ENTER dos veces para finalizar):")
lineas = []
while True:
    linea = input()
    if linea == "" and len(lineas) > 0 and lineas[-1] == "":
        break
    lineas.append(linea)
cuerpo = "\n".join(lineas[:-1])

# Solicitar cantidad de destinatarios
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

# Mostrar resumen antes de enviar
print("\n" + "="*50)
print("RESUMEN DE ENVIO")
print("="*50)
print(f"De: {remitente}")
print(f"Asunto: {asunto}")
print(f"Destinatarios: {len(destinatarios)}")
for i, dest in enumerate(destinatarios, 1):
    print(f"   {i}. {dest}")
print("\nMensaje:")
print("-"*30)
print(cuerpo)
print("-"*30)

confirmar = input("\n¿Enviar correos? (s/n): ").lower()
if confirmar != 's' and confirmar != 'si':
    print("\nEnvio cancelado. Hasta luego!")
    sys.exit(0)

# -----------------------------------------------------------
# ENVIO DE CORREOS
# -----------------------------------------------------------
print("\nIniciando envio... (CTRL+C para cancelar)")

try:
    # Crear conexion segura con Gmail
    print("Conectando con servidor Gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    print("Autenticando...")
    server.login(remitente, token)

    print("\nInicio de sesion exitoso. Enviando correos...\n")

    # Enviar a cada destinatario
    exitosos = 0
    fallidos = 0
    
    for i, destino in enumerate(destinatarios, 1):
        try:
            # Crear el mensaje
            msg = MIMEMultipart()
            msg['From'] = remitente
            msg['To'] = destino
            msg['Subject'] = asunto
            msg.attach(MIMEText(cuerpo, 'plain', 'utf-8'))

            # Enviar
            server.send_message(msg)
            print(f"[{i}/{len(destinatarios)}] Enviado a {destino}")
            exitosos += 1
            
        except Exception as e:
            print(f"[{i}/{len(destinatarios)}] Error con {destino}: {e}")
            fallidos += 1

    # Cerrar conexion
    server.quit()
    
    # Resumen final
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
    print("  * Borra token.txt y genera uno nuevo")
