import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import signal

# -----------------------------------------------------------
# MANEJADOR PARA CTRL+C
# -----------------------------------------------------------
def signal_handler(sig, frame):
    print("\n\nSaliendo del programa... Hasta luego!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

# -----------------------------------------------------------
# FUNCION PARA MOSTRAR INSTRUCCIONES DE LA KEY
# -----------------------------------------------------------
def mostrar_instrucciones_key():
    print("\n" + "="*60)
    print("INSTRUCCIONES: COMO OBTENER TU CONTRASENA DE APLICACION")
    print("="*60)
    print("\nPara Gmail, necesitas una 'Contrasena de aplicacion' porque:")
    print("  * La contrasena normal de Gmail NO funciona directamente")
    print("  * Debes tener activada la verificacion en dos pasos")
    
    print("\nPASOS PARA OBTENERLA:")
    print("  1. Ve a tu cuenta de Google: myaccount.google.com")
    print("  2. Ve a 'Seguridad'")
    print("  3. Activa la 'Verificacion en dos pasos' (si no la tienes)")
    print("  4. Vuelve a 'Seguridad' y busca 'Contrasenas de aplicacion'")
    print("  5. Selecciona 'Correo' y 'Windows Computer'")
    print("  6. Copia la contrasena de 16 caracteres que te generan")
    
    print("\nSi no ves 'Contrasenas de aplicacion', puede que:")
    print("  * No tengas activada la verificacion en dos pasos")
    print("  * Tu administrador bloqueo esta funcion")
    print("  * Prueba con una cuenta personal de Gmail")
    
    print("\nEnlace directo: https://myaccount.google.com/apppasswords")
    print("="*60 + "\n")

# -----------------------------------------------------------
# FUNCION PARA MOSTRAR MENSAJE DE AYUDA
# -----------------------------------------------------------
def mostrar_ayuda():
    print("\n" + "="*50)
    print("AYUDA - XONIMAIL")
    print("="*50)
    print("Comandos disponibles:")
    print("  * CTRL+C - Salir del programa")
    print("  * ENTER - Continuar con el siguiente paso")
    print("\nPara enviar correos:")
    print("  1. Ingresa tu correo Gmail")
    print("  2. Ingresa tu contrasena de aplicacion (token)")
    print("  3. Escribe el asunto y mensaje")
    print("  4. Agrega los destinatarios")
    print("="*50 + "\n")

# -----------------------------------------------------------
# CONFIGURACION INICIAL (solicitada al usuario)
# -----------------------------------------------------------
print("\n" + "="*60)
print("XONIMAIL - ENVIO DE CORREOS DESDE TERMINAL")
print("="*60)
print("(Presiona CTRL+C en cualquier momento para salir)")
print("="*60 + "\n")

# Mostrar ayuda automaticamente la primera vez
mostrar_ayuda()

# Solicitar credenciales
remitente = input("Tu correo Gmail: ").strip()
while not remitente:
    print("El correo no puede estar vacio")
    remitente = input("Tu correo Gmail: ").strip()

# Solicitar token con verificacion de vacio
while True:
    password = input("Tu contrasena de aplicacion (token): ").strip()
    if password:
        break
    else:
        print("\n*** NO HAS INGRESADO UNA CONTRASENA DE APLICACION ***")
        print("Esto es necesario para poder enviar correos desde Gmail.")
        print("\nPresiona ENTER para ver las instrucciones de como obtenerla,")
        respuesta = input("o escribe cualquier tecla para intentar nuevamente: ")
        
        if respuesta == "":
            mostrar_instrucciones_key()
            print("\nVuelve cuando tengas tu contrasena de aplicacion.")
            continuar = input("Presiona ENTER para continuar... ")
        else:
            print("Intentemos de nuevo...\n")

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

confirmar = input("\nEnviar correos? (s/n): ").lower()
if confirmar != 's' and confirmar != 'si':
    print("\nEnvio cancelado. Hasta luego!")
    sys.exit(0)

# -----------------------------------------------------------
# CONFIGURACION DEL SERVIDOR SMTP DE GMAIL
# -----------------------------------------------------------
print("\nIniciando envio... (CTRL+C para cancelar)")

try:
    # Crear conexion segura con Gmail
    print("Conectando con servidor Gmail...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    
    print("Autenticando...")
    server.login(remitente, password)

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
    print("  * Verifica que la contrasena de aplicacion sea correcta")
    print("  * Asegurate de tener activada la verificacion en dos pasos")
    print("  * Revisa tu conexion a internet")
