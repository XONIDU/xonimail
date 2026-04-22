#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
XONIMAIL 2026 - Lanzador Universal con Gestor de Token
Cliente de Gmail para terminal en equipos de bajos recursos
Desarrollador: Darian Alberto Camacho Salas
Organizacion: XONIDU
"""

import subprocess
import sys
import os
import platform
import shutil
import time
from pathlib import Path

# ============================================================================
# Colores para terminal
# ============================================================================
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    END = '\033[0m'
    BOLD = '\033[1m'
    
    @staticmethod
    def supports_color():
        if platform.system() == 'Windows':
            try:
                import ctypes
                kernel32 = ctypes.windll.kernel32
                return kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            except:
                return False
        return True

if not Colors.supports_color():
    for attr in dir(Colors):
        if not attr.startswith('_') and attr != 'supports_color':
            setattr(Colors, attr, '')

# ============================================================================
# Deteccion del sistema
# ============================================================================
def get_system():
    return platform.system().lower()

def get_linux_distro():
    if get_system() != 'linux':
        return None
    try:
        if os.path.exists('/etc/os-release'):
            with open('/etc/os-release', 'r') as f:
                content = f.read().lower()
                if 'ubuntu' in content or 'debian' in content or 'mint' in content or 'antix' in content:
                    return 'debian-based'
                elif 'arch' in content or 'manjaro' in content:
                    return 'arch-based'
                elif 'fedora' in content:
                    return 'fedora'
                elif 'centos' in content or 'rhel' in content:
                    return 'centos'
                elif 'opensuse' in content:
                    return 'opensuse'
        if shutil.which('apt'):
            return 'debian-based'
        elif shutil.which('pacman'):
            return 'arch-based'
        elif shutil.which('dnf'):
            return 'fedora'
        elif shutil.which('yum'):
            return 'centos'
        elif shutil.which('zypper'):
            return 'opensuse'
        return 'linux-generico'
    except:
        return 'linux-generico'

def get_python_command():
    if get_system() == 'windows':
        return ['python']
    else:
        try:
            subprocess.run(['python3', '--version'], capture_output=True, check=True)
            return ['python3']
        except:
            return ['python']

def get_pip_command():
    return [sys.executable, '-m', 'pip']

def get_install_flags():
    flags = []
    sistema = get_system()
    distro = get_linux_distro()
    if sistema == 'linux':
        if distro in ['arch-based', 'fedora']:
            flags.append('--break-system-packages')
        else:
            flags.append('--user')
    elif sistema == 'darwin':
        flags.append('--user')
    return flags

def get_script_dir():
    return os.path.dirname(os.path.abspath(__file__))

def get_xonimail_path():
    """Detecta la ruta de xonimail.py en multiples ubicaciones"""
    script_dir = get_script_dir()
    rutas = [
        os.path.join(script_dir, 'xonimail.py'),
        '/usr/share/xonimail/xonimail.py',
        os.path.join(os.path.expanduser("~"), '.xonimail', 'xonimail.py'),
        os.path.join(os.getcwd(), 'xonimail.py')
    ]
    for r in rutas:
        if os.path.exists(r):
            return r
    return None

def print_banner():
    sistema = get_system()
    distro = get_linux_distro()
    sistema_texto = {
        'windows': 'WINDOWS',
        'linux': f'LINUX ({distro.upper()})' if distro else 'LINUX',
        'darwin': 'MACOS'
    }.get(sistema, 'DESCONOCIDO')
    
    banner = f"""
{Colors.PURPLE}{Colors.BOLD}╔══════════════════════════════════════════════════════════╗
║                    XONIMAIL 2026 v1.0                    ║
║              Cliente de Gmail para Terminal               ║
║                   Optimizado para 1GB RAM                 ║
║                                                            ║
║               Sistema detectado: {sistema_texto:<27} ║
║                                                            ║
║               Desarrollado por: Darian Alberto             ║
║                      Camacho Salas                         ║
║                      Organizacion: XONIDU                  ║
╚══════════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def mostrar_ayuda():
    ayuda = f"""
{Colors.BOLD}USO DE XONIMAIL:{Colors.END}

  xonimail

{Colors.BOLD}CARACTERISTICAS:{Colors.END}

  Interfaz 100% terminal
  Envio a multiples destinatarios
  Composicion de mensajes multilinea
  Sin necesidad de sudo

{Colors.BOLD}COMANDOS:{Colors.END}

  CTRL+C     - Salir del programa
  ENTER      - Continuar con el siguiente paso

{Colors.BOLD}OBTENER TOKEN DE GMAIL:{Colors.END}

  https://myaccount.google.com/apppasswords
    """
    print(ayuda)

# ============================================================================
# Clase principal XONIMAIL
# ============================================================================
class XONIMAIL:
    def __init__(self):
        self.token_file = self.get_token_path()
        self.token = None
        self.remitente = None
        
        self.load_token()
        self.setup_readline()
        self.welcome()
    
    def get_token_path(self):
        """Busca token.txt priorizando ~/.xonimail/ (sin sudo)"""
        
        # Opcion 1: Directorio en HOME (recomendado, sin sudo)
        home_token = os.path.join(os.path.expanduser("~"), '.xonimail', 'token.txt')
        if os.path.exists(home_token):
            return home_token
        
        # Opcion 2: Mismo directorio que start.py
        script_dir = get_script_dir()
        local_token = os.path.join(script_dir, 'token.txt')
        if os.path.exists(local_token):
            return local_token
        
        # Opcion 3: /usr/share/xonimail/ (legacy)
        system_token = '/usr/share/xonimail/token.txt'
        if os.path.exists(system_token):
            return system_token
        
        return home_token
    
    def setup_readline(self):
        try:
            import readline
            histfile = Path.home() / ".xonimail_history"
            try:
                readline.read_history_file(histfile)
            except FileNotFoundError:
                pass
            import atexit
            atexit.register(readline.write_history_file, histfile)
        except ImportError:
            pass
    
    def load_token(self):
        try:
            with open(self.token_file, 'r') as f:
                token = f.read().strip()
                if token:
                    self.token = token
                else:
                    print(f"\n[ERROR] El archivo token.txt esta vacio")
                    print(f"[INFO] Crea token.txt en: {os.path.dirname(self.token_file)}")
                    sys.exit(1)
        except FileNotFoundError:
            print(f"\n[ERROR] No se encuentra token.txt")
            print("[INFO] Gmail requiere una contraseña de aplicacion")
            print(f"[INFO] Crea token.txt en: {os.path.dirname(self.token_file)}")
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
        
    def run(self):
        print("Iniciando XONIMAIL...")
        print("Para salir: presiona CTRL+C")
        print("-" * 50)
        
        try:
            # Importar y ejecutar el modulo principal
            import xonimail
            # Si xonimail tiene una funcion main, llamarla
            if hasattr(xonimail, 'main'):
                xonimail.main()
            else:
                # Crear instancia y ejecutar
                app = xonimail.XONIMAIL()
                app.run()
        except ImportError as e:
            print(f"\n[ERROR] No se puede importar xonimail: {e}")
            sys.exit(1)
        except KeyboardInterrupt:
            print("\n[INFO] Programa detenido por el usuario")
        except Exception as e:
            print(f"\n[ERROR] {e}")

# ============================================================================
# Verificacion de dependencias
# ============================================================================
def check_python():
    try:
        cmd = get_python_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def check_pip():
    try:
        cmd = get_pip_command() + ['--version']
        subprocess.run(cmd, capture_output=True, check=True)
        return True
    except:
        return False

def install_pip_linux():
    distro = get_linux_distro()
    print(f"{Colors.YELLOW}Instalando pip en Linux ({distro})...{Colors.END}")
    if distro == 'debian-based':
        try:
            subprocess.run(['sudo', 'apt', 'update'], check=False)
            subprocess.run(['sudo', 'apt', 'install', '-y', 'python3-pip'], check=True)
            return True
        except:
            return False
    elif distro == 'arch-based':
        try:
            subprocess.run(['sudo', 'pacman', '-S', '--noconfirm', 'python-pip'], check=True)
            return True
        except:
            return False
    return False

def install_pip_windows():
    print(f"{Colors.YELLOW}Instalando pip en Windows...{Colors.END}")
    try:
        subprocess.run([sys.executable, '-m', 'ensurepip', '--upgrade'], check=True)
        return True
    except:
        return False

def check_dependencies():
    """Verifica que los modulos estandar existan"""
    try:
        __import__('smtplib')
        __import__('email')
        return True
    except ImportError as e:
        print(f"{Colors.RED}Error: Modulo faltante - {e}{Colors.END}")
        return False

def manage_token():
    """Gestion interactiva del token de Gmail"""
    token_path = XONIMAIL().get_token_path()
    token_dir = os.path.dirname(token_path)
    
    if not os.path.exists(token_dir):
        os.makedirs(token_dir, exist_ok=True)
    
    if not os.path.exists(token_path):
        with open(token_path, 'w') as f:
            f.write("# Tu contraseña de aplicacion de Gmail (16 caracteres)\n")
            f.write("# Obtenla en: https://myaccount.google.com/apppasswords\n")
            f.write("# Requiere verificacion en dos pasos activada\n\n")
            f.write("# Ejemplo:\n")
            f.write("# abcd1234efgh5678\n")
        print(f"\n{Colors.YELLOW}[INFO] Creado token.txt en: {token_path}{Colors.END}")
        print(f"{Colors.YELLOW}[INFO] Agrega tu token y vuelve a ejecutar{Colors.END}")
        print(f"{Colors.CYAN}       https://myaccount.google.com/apppasswords{Colors.END}\n")
        sys.exit(0)
    
    with open(token_path, 'r') as f:
        lines = f.readlines()
    
    token = None
    for line in lines:
        line = line.strip()
        if line and not line.startswith('#'):
            token = line
            break
    
    print(f"\n{Colors.CYAN}{Colors.BOLD}=== GESTOR DE TOKEN ==={Colors.END}")
    print(f"Directorio: {token_path}")
    
    if token:
        masked = token[:8] + "..." + token[-4:] if len(token) > 16 else token
        print(f"Token actual: {masked}")
    else:
        print(f"{Colors.YELLOW}No hay token configurado{Colors.END}")
    
    print(f"\n{Colors.BOLD}Opciones:{Colors.END}")
    print("  1. Configurar nuevo token")
    print("  2. Eliminar token actual")
    print("  3. Continuar con token actual")
    
    opcion = input(f"\n{Colors.YELLOW}Elige una opcion (1-3): {Colors.END}").strip()
    
    if opcion == '1':
        nuevo_token = input(f"{Colors.CYAN}Ingresa tu token de Gmail (16 caracteres): {Colors.END}").strip()
        if nuevo_token and len(nuevo_token) >= 16:
            with open(token_path, 'w') as f:
                f.write("# Tu contraseña de aplicacion de Gmail (16 caracteres)\n")
                f.write("# Obtenla en: https://myaccount.google.com/apppasswords\n")
                f.write("# Requiere verificacion en dos pasos activada\n\n")
                f.write(f"{nuevo_token}\n")
            print(f"{Colors.GREEN}Token guardado correctamente{Colors.END}")
            time.sleep(1)
        else:
            print(f"{Colors.RED}Token invalido. Debe tener al menos 16 caracteres{Colors.END}")
            time.sleep(1)
    
    elif opcion == '2':
        if token:
            with open(token_path, 'w') as f:
                f.write("# Tu contraseña de aplicacion de Gmail (16 caracteres)\n")
                f.write("# Obtenla en: https://myaccount.google.com/apppasswords\n")
                f.write("# Requiere verificacion en dos pasos activada\n\n")
            print(f"{Colors.GREEN}Token eliminado correctamente{Colors.END}")
            time.sleep(1)
            print(f"{Colors.YELLOW}Ejecuta nuevamente para configurar un token{Colors.END}")
            sys.exit(0)
        else:
            print(f"{Colors.YELLOW}No hay token para eliminar{Colors.END}")
            time.sleep(1)
    
    print(f"{Colors.GREEN}Continuando...{Colors.END}")
    return token_path

# ============================================================================
# Funcion principal
# ============================================================================
def main():
    if get_system() == 'windows':
        os.system('cls')
    else:
        os.system('clear')
    
    print_banner()
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help', '/?']:
        mostrar_ayuda()
        if get_system() != 'windows':
            input(f"\n{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")
        return
    
    if not check_python():
        print(f"\n{Colors.RED}Python no esta instalado{Colors.END}")
        sys.exit(1)
    
    ver_py = subprocess.run(get_python_command() + ['--version'], capture_output=True, text=True).stdout.strip()
    print(f"{Colors.BOLD}Python:{Colors.END} {ver_py}")
    
    if not check_pip():
        print(f"\n{Colors.YELLOW}Pip no encontrado. Instalando...{Colors.END}")
        sistema = get_system()
        if sistema == 'linux':
            if not install_pip_linux():
                print(f"{Colors.RED}No se pudo instalar pip.{Colors.END}")
                sys.exit(1)
        elif sistema == 'windows':
            if not install_pip_windows():
                print(f"{Colors.RED}No se pudo instalar pip.{Colors.END}")
                sys.exit(1)
    else:
        print(f"{Colors.GREEN}Pip disponible{Colors.END}")
    
    if not check_dependencies():
        print(f"{Colors.RED}No se pueden importar modulos necesarios{Colors.END}")
        sys.exit(1)
    else:
        print(f"{Colors.GREEN}Modulos disponibles{Colors.END}")
    
    # Gestionar token
    manage_token()
    
    ruta_xonimail = get_xonimail_path()
    if not ruta_xonimail:
        print(f"\n{Colors.RED}No se encuentra xonimail.py{Colors.END}")
        print(f"{Colors.YELLOW}Asegurate de que xonimail.py esta en el directorio actual{Colors.END}")
        sys.exit(1)
    
    xonimail_dir = os.path.dirname(ruta_xonimail)
    print(f"{Colors.GREEN}xonimail.py encontrado en: {xonimail_dir}{Colors.END}")
    
    os.chdir(xonimail_dir)
    print(f"\n{Colors.BOLD}Iniciando XONIMAIL...{Colors.END}")
    print(f"{Colors.CYAN}Para salir: presiona CTRL+C{Colors.END}")
    print("-"*50)
    
    try:
        python_cmd = get_python_command()
        subprocess.run(python_cmd + [ruta_xonimail])
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Programa detenido por el usuario.{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")
    
    print(f"\n{Colors.GREEN}Gracias por usar XONIMAIL{Colors.END}")
    if get_system() != 'windows':
        input(f"{Colors.YELLOW}Presiona Enter para salir...{Colors.END}")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Saliendo...{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error inesperado: {e}{Colors.END}")
