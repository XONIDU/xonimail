#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONIMAIL 2026 - Lanzador Universal de Cliente de Gmail para Terminal
Este script ejecuta xonimail.py
Desarrollado por: Darian Alberto Camacho Salas
#Somos XONIDU
"""

import subprocess
import sys
import os
import platform
import shutil
import importlib.util

# Colores para terminal
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        """Verifica si la terminal soporta colores"""
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

# Desactivar colores si no hay soporte
if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

def get_system():
    """Detecta el sistema operativo"""
    return platform.system().lower()

def get_linux_distro():
    """Detecta la distribucion de Linux"""
    if get_system() != 'linux':
        return None
    
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content:
                    return 'ubuntu'
                elif 'debian' in content:
                    return 'debian'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content:
                    return 'centos'
                elif 'arch' in content:
                    return 'arch'
                elif 'manjaro' in content:
                    return 'manjaro'
                elif 'mint' in content:
                    return 'mint'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    """Obtiene el comando Python correcto"""
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def print_banner():
    """Muestra el banner de XONIMAIL"""
    sistema = get_system()
    distro = get_linux_distro()
    
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.BLUE}{Colors.BOLD}═══════════════════════════════════════════════════════════
                    XONIMAIL 2026 v1.0                    
              Cliente de Gmail para Terminal            
              Envia correos desde dispositivos           
              de bajos recursos                         
                                                          
              Sistema detectado: {sistema_texto}            
                                                          
              Desarrollado por: Darian Alberto            
              Camacho Salas                               
              #Somos XONIDU
═══════════════════════════════════════════════════════════{Colors.END}
    """
    print(banner)

def check_python():
    """Verifica Python instalado"""
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_command(comando):
    """Verifica si un comando existe"""
    return shutil.which(comando) is not None

def check_python_module(module_name):
    """Verifica si un modulo de Python esta instalado"""
    return importlib.util.find_spec(module_name) is not None

def check_dependencies():
    """Verifica las dependencias de Python necesarias"""
    print(f"\n{Colors.BOLD}Verificando dependencias de Python...{Colors.END}")
    
    # XONIMAIL solo usa librerias estandar, pero verificamos por compatibilidad
    dependencias = [
        ('smtplib', 'smtplib', 'Correo SMTP', 'smtplib'),
        ('email', 'email', 'Construir mensajes', 'email'),
    ]
    
    faltantes = []
    
    for modulo, paquete, desc, import_name in dependencias:
        if check_python_module(import_name):
            print(f"{Colors.GREEN}  - {modulo}: OK (incluido en Python){Colors.END}")
        else:
            # Esto nunca deberia pasar porque son modulos estandar
            print(f"{Colors.YELLOW}  - {modulo}: VERIFICANDO...{Colors.END}")
            faltantes.append(paquete)
    
    return faltantes

def install_dependencies(faltantes):
    """Instala las dependencias faltantes"""
    if not faltantes:
        print(f"{Colors.GREEN}Todas las dependencias estan satisfechas{Colors.END}")
        return True
    
    print(f"\n{Colors.BOLD}Instalando dependencias faltantes...{Colors.END}")
    
    sistema = get_system()
    distro = get_linux_distro()
    
    # XONIMAIL usa modulos estandar, pero instalamos por si acaso
    python_paquetes = faltantes
    
    if python_paquetes:
        print(f"Paquetes Python a instalar: {', '.join(python_paquetes)}")
        
        # Construir comando de instalacion
        cmd = [sys.executable, '-m', 'pip', 'install']
        
        # Agregar opciones segun sistema
        if sistema == 'linux':
            if distro in ['arch', 'manjaro', 'fedora']:
                cmd.append('--break-system-packages')
                print(f"{Colors.YELLOW}Usando --break-system-packages para {distro}{Colors.END}")
            else:
                cmd.append('--user')
        elif sistema == 'darwin':
            cmd.append('--user')
        
        cmd.extend(python_paquetes)
        
        # Intentar instalacion
        try:
            print(f"Ejecutando: {' '.join(cmd)}")
            subprocess.run(cmd, check=True)
            print(f"{Colors.GREEN}Dependencias instaladas correctamente{Colors.END}")
        except subprocess.CalledProcessError as e:
            print(f"{Colors.RED}Error instalando dependencias: {e}{Colors.END}")
            print(f"\n{Colors.YELLOW}Intentando metodo alternativo...{Colors.END}")
            
            # Segundo intento: solo --user
            try:
                cmd2 = [sys.executable, '-m', 'pip', 'install', '--user'] + python_paquetes
                subprocess.run(cmd2, check=True)
                print(f"{Colors.GREEN}Instaladas con --user{Colors.END}")
            except:
                print(f"{Colors.RED}Fallo la instalacion{Colors.END}")
                print(f"\n{Colors.YELLOW}Nota: XONIMAIL usa modulos estandar de Python{Colors.END}")
                print(f"Estas dependencias no son realmente necesarias.")
    
    return True

def check_token_file():
    """Verifica si existe el archivo token.txt"""
    token_file = 'token.txt'
    
    if os.path.exists(token_file):
        with open(token_file, 'r') as f:
            token = f.read().strip()
            if token:
                print(f"{Colors.GREEN}Archivo token.txt encontrado{Colors.END}")
                return True
            else:
                print(f"{Colors.YELLOW}Archivo token.txt esta vacio{Colors.END}")
                return False
    else:
        print(f"{Colors.YELLOW}Archivo token.txt no encontrado{Colors.END}")
        return False

def mostrar_ayuda():
    """Muestra ayuda de uso"""
    ayuda = f"""
{Colors.BOLD}USO DE XONIMAIL:{Colors.END}

  python start.py

{Colors.BOLD}DESCRIPCION:{Colors.END}

  XONIMAIL es un cliente de Gmail para terminal que permite
  enviar correos electronicos desde dispositivos de bajos recursos.

{Colors.BOLD}CARACTERISTICAS:{Colors.END}

  - Envio a multiples destinatarios
  - Composicion de mensajes multilinea
  - Autenticacion mediante contraseñas de aplicacion
  - Token almacenado en token.txt
  - Interrupcion segura con Ctrl+C

{Colors.BOLD}ARCHIVO TOKEN.TXT:{Colors.END}

  Crea un archivo 'token.txt' en la misma carpeta con tu
  contraseña de aplicacion de Gmail (16 caracteres).

  Como obtenerla:
  1. https://myaccount.google.com/apppasswords
  2. Activa verificacion en dos pasos
  3. Genera contraseña para "Correo" y "Windows Computer"

{Colors.BOLD}EJEMPLO:{Colors.END}

  echo "tutoken1234567890" > token.txt
  python start.py
    """
    print(ayuda)

def verificar_importaciones():
    """Verifica que todas las importaciones necesarias funcionen"""
    print(f"\n{Colors.BOLD}Verificando importaciones...{Colors.END}")
    
    modulos = [
        ('smtplib', 'smtplib'),
        ('email.mime.text', 'email'),
        ('email.mime.multipart', 'email'),
    ]
    
    todos_ok = True
    for modulo, nombre in modulos:
        try:
            __import__(modulo)
            print(f"{Colors.GREEN}  - {nombre}: OK{Colors.END}")
        except ImportError:
            print(f"{Colors.RED}  - {nombre}: FALLO{Colors.END}")
            todos_ok = False
    
    return todos_ok

def crear_accesos_directos():
    """Crea accesos directos para cada sistema"""
    sistema = get_system()
    
    if sistema == 'windows':
        # Crear .bat para Windows
        with open('INICIAR_XONIMAIL.bat', 'w') as f:
            f.write("""@echo off
title XONIMAIL 2026 - Cliente Gmail para Terminal
color 1F
echo ========================================
echo      XONIMAIL 2026 - Cliente Gmail
echo      Desarrollado por Darian Alberto
echo ========================================
echo.
python start.py
pause
""")
        print(f"{Colors.GREEN}Creado INICIAR_XONIMAIL.bat - Haz doble clic para ejecutar{Colors.END}")
    
    elif sistema == 'linux':
        # Crear .sh para Linux
        with open('INICIAR_XONIMAIL.sh', 'w') as f:
            f.write("""#!/bin/bash
echo "========================================"
echo "      XONIMAIL 2026 - Cliente Gmail"
echo "      Desarrollado por Darian Alberto"
echo "========================================"
echo ""
python3 start.py
read -p "Presiona Enter para salir"
""")
        os.chmod('INICIAR_XONIMAIL.sh', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONIMAIL.sh - Ejecuta con: ./INICIAR_XONIMAIL.sh{Colors.END}")
    
    elif sistema == 'darwin':
        # Crear .command para Mac
        with open('INICIAR_XONIMAIL.command', 'w') as f:
            f.write("""#!/bin/bash
cd "$(dirname "$0")"
echo "========================================"
echo "      XONIMAIL 2026 - Cliente Gmail"
echo "      Desarrollado por Darian Alberto"
echo "========================================"
echo ""
python3 start.py
""")
        os.chmod('INICIAR_XONIMAIL.command', 0o755)
        print(f"{Colors.GREEN}Creado INICIAR_XONIMAIL.command - Haz doble clic para ejecutar{Colors.END}")

def main():
    """Funcion principal"""
    # Limpiar pantalla
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    # Mostrar banner
    print_banner()
    
    # Verificar si hay argumentos de ayuda
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '/?']:
        mostrar_ayuda()
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    # Verificar Python
    if not check_python():
        print(f"\n{Colors.RED}Error: Python no esta instalado{Colors.END}")
        print("Instala Python desde: https://www.python.org/downloads/")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    python_version = subprocess.run(get_python_command() + ['--version'], 
                                   capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {python_version}")
    print(f"{Colors.BOLD}Directorio:{Colors.END} {os.path.dirname(os.path.abspath(__file__))}")
    
    # Verificar archivo token.txt
    print(f"\n{Colors.BOLD}Verificando configuracion...{Colors.END}")
    tiene_token = check_token_file()
    
    if not tiene_token:
        print(f"\n{Colors.YELLOW}No se encontro token valido{Colors.END}")
        print("XONIMAIL necesita un token de Gmail para funcionar.")
        print("\nEjecuta el programa para ver instrucciones:")
        print("  python xonimail.py")
        
        respuesta = input(f"\n{Colors.YELLOW}¿Mostrar instrucciones para obtener token? (s/n): {Colors.END}")
        if respuesta.lower() == 's':
            mostrar_ayuda()
    
    # Verificar dependencias
    faltantes = check_dependencies()
    
    if faltantes:
        print(f"\n{Colors.YELLOW}Verificando dependencias...{Colors.END}")
        install_dependencies(faltantes)
    
    # Verificar que existe xonimail.py
    if not os.path.exists('xonimail.py'):
        print(f"\n{Colors.RED}Error: No se encuentra xonimail.py{Colors.END}")
        print("Asegurate de que xonimail.py esta en el mismo directorio")
        print("\nPuedes descargarlo desde:")
        print("  https://github.com/XONIDU/xonimail")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    # Verificar que las importaciones funcionan
    print(f"\n{Colors.BOLD}Verificando que todo funcione...{Colors.END}")
    if not verificar_importaciones():
        print(f"\n{Colors.RED}Error: No se pueden importar modulos necesarios{Colors.END}")
        print("Esto es extrano porque son modulos estandar de Python.")
        print("Revisa tu instalacion de Python.")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    print(f"\n{Colors.BOLD}Iniciando XONIMAIL...{Colors.END}")
    print(f"{Colors.BOLD}Para salir en cualquier momento:{Colors.END} Ctrl+C")
    print("-" * 60)
    
    # EJECUTAR xonimail.py
    try:
        python_cmd = get_python_command()
        cmd = python_cmd + ['xonimail.py']
        print(f"Ejecutando: {' '.join(cmd)}")
        print("-" * 60)
        
        # Ejecutar xonimail.py
        resultado = subprocess.run(cmd)
        
        if resultado.returncode != 0:
            print(f"\n{Colors.RED}Error: xonimail.py termino con codigo {resultado.returncode}{Colors.END}")
            
    except FileNotFoundError:
        print(f"\n{Colors.RED}Error: No se encuentra xonimail.py{Colors.END}")
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Programa detenido por el usuario{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error ejecutando xonimail.py: {e}{Colors.END}")
    
    print(f"\n{Colors.BLUE}Gracias por usar XONIMAIL 2026{Colors.END}")
    print(f"{Colors.BLUE}Desarrollado por Darian Alberto Camacho Salas{Colors.END}")
    print(f"{Colors.BLUE}#Somos XONIDU{Colors.END}")
    
    # Pausa al final (excepto en Windows que ya tiene pausa por el .bat)
    if get_system() != 'windows':
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        # Crear accesos directos
        crear_accesos_directos()
        
        # Ejecutar programa principal
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
        input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
