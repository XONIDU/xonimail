# XONIMAIL

Envio de correos desde terminal, diseñado para dispositivos de bajos recursos (ASUS Eee PC, etc.)

## Descripcion

XONIMAIL es un cliente liviano de Gmail que funciona completamente en la terminal. Perfecto para enviar correos desde dispositivos con recursos limitados sin necesidad de un navegador web pesado o cliente de correo.

## Caracteristicas

- **Interfaz 100% terminal** - Rapido y liviano
- **Multiples destinatarios** - Envia a una o muchas direcciones
- **Composicion interactiva** - Escribe correos de multiples lineas
- **Soporte para contraseñas de aplicacion** - Autenticacion segura con Gmail
- **Optimizado** - Funciona en ASUS Eee PC y dispositivos similares

## Instalacion Rapida

### 1. Clonar el repositorio

```bash
git clone https://github.com/xonidu/xonimail.git
cd xonimail
```

### 2. Instalar dependencias

El programa requiere las siguientes dependencias:
- smtplib (incluido con Python)
- email (incluido con Python)

No se necesitan dependencias externas, pero se incluye un archivo requirements.txt por compatibilidad.

#### Instalacion por Sistema Operativo

##### Linux (General)
```bash
pip install -r requirements.txt
```

##### Arch Linux / Manjaro
```bash
sudo pacman -S python-pip
pip install --break-system-packages -r requirements.txt
```

##### Debian / Ubuntu / antiX
```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install --break-system-packages -r requirements.txt
```

##### Fedora / RHEL / CentOS
```bash
sudo dnf install python3-pip
pip3 install --break-system-packages -r requirements.txt
```

##### openSUSE
```bash
sudo zypper install python3-pip
pip3 install --break-system-packages -r requirements.txt
```

##### macOS
```bash
# Usando Homebrew
brew install python3
pip3 install -r requirements.txt

# O usando pip directamente
pip3 install -r requirements.txt
```

##### Windows
```bash
# En Command Prompt o PowerShell
pip install -r requirements.txt

# Si tienes problemas con permisos
pip install --user -r requirements.txt
```

##### Termux (Android)
```bash
pkg update
pkg install python
pip install -r requirements.txt
```

### 3. Configurar Contraseña de Aplicacion de Gmail

Gmail requiere una **Contraseña de aplicacion** especial en lugar de tu contraseña normal:

1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. Ve a **Seguridad**
3. Activa la **Verificacion en dos pasos** (si no la tienes activada)
4. Regresa a Seguridad y busca **Contraseñas de aplicacion**
5. Selecciona **Correo** y **Windows Computer**
6. Copia la contraseña de 16 caracteres que se genera

### 4. Configurar el Token

Crea un archivo `token.txt` en la misma carpeta y pega tu contraseña de aplicacion:

```bash
# Crear el archivo con tu token (reemplaza con tu token real)
echo "tu-token-de-16-caracteres-aqui" > token.txt

# O usando nano/vim
nano token.txt
```

## Uso

```bash
python start.py
# o
python3 start.py
```

El programa te guiara a traves de:
- Leer el token automaticamente de token.txt
- Ingresar tu direccion de Gmail
- Escribir el asunto y mensaje
- Agregar destinatarios

### Caracteristicas Interactivas

- Si **token.txt** no existe, el programa muestra instrucciones para crearlo
- Presiona **CTRL+C** en cualquier momento para salir
- Presiona **ENTER dos veces** para terminar de escribir tu mensaje
- Escribe **'s'** o **'si'** para confirmar el envio

## Archivos

- `start.py` - Programa principal
- `token.txt` - Archivo con tu token (debes crearlo)
- `requirements.txt` - Dependencias de Python (opcional)

## Requisitos

```
Python 3.6 o superior
smtplib (incluido)
email (incluido)
```

No se necesitan dependencias externas! Todas las librerias vienen con Python.

## Ejemplo de Sesion

```
============================================================
XONIMAIL - ENVIO DE CORREOS DESDE TERMINAL
============================================================
(Presiona CTRL+C en cualquier momento para salir)

==================================================
AYUDA - XONIMAIL
==================================================
Comandos disponibles:
  * CTRL+C - Salir del programa
  * ENTER - Continuar con el siguiente paso

Para enviar correos:
  1. El token se lee automaticamente de token.txt
  2. Ingresa tu correo Gmail
  3. Escribe el asunto y mensaje
  4. Agrega los destinatarios
==================================================

Tu correo Gmail: ejemplo@gmail.com
Token cargado desde token.txt

Asunto del correo: Prueba desde XONIMAIL

Escribe tu mensaje (presiona ENTER dos veces para finalizar):
Hola, este es un correo de prueba
enviado desde XONIMAIL.

Cuantos destinatarios? (numero): 1

Ingresa los 1 correos:
  Destinatario 1: destinatario@gmail.com
```

## Solucion de Problemas

### Error de autenticacion
- Verifica que el token en token.txt sea correcto
- Asegurate de tener activada la verificacion en dos pasos
- Genera una nueva contraseña de aplicacion si es necesario

### Error de conexion
- Revisa tu conexion a internet
- Verifica que el puerto 587 no este bloqueado
- Prueba con otra red

### Error de permisos en Linux
```bash
# Si tienes problemas con --break-system-packages
pip install --user -r requirements.txt
```

## Nota de Seguridad

- Tus credenciales solo se usan durante la sesion
- El token se guarda localmente en token.txt
- No se envian tus datos a ningun servidor externo
- Usa SMTP seguro de Gmail con cifrado TLS

## Autor

Darian Alberto Camacho Salas (XONIDU)

Email: xonidu@gmail.com

