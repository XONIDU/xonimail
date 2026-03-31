# 📄 XONIMAIL

**Advertencia:** Este código tiene únicamente fines educativos. No debe usarse para actividades malintencionadas ni para enviar correos no deseados. El autor no se hace responsable del uso indebido.

## 🎯 ¿Qué es XONIMAIL?

XONIMAIL es un cliente de Gmail para terminal diseñado para dispositivos de bajos recursos (ASUS Eee PC, laptops antiguas, etc.). Consta de dos componentes:

- **start.py** - Lanzador universal que verifica dependencias y ejecuta el programa principal
- **xonimail.py** - Programa principal con la funcionalidad de envío de correos

Permite:

- 📨 Enviar correos electrónicos sin necesidad de navegador web
- 📤 Gestionar múltiples destinatarios en un solo envío
- 📝 Redactar mensajes multilínea de forma interactiva
- 🔐 Autenticación segura mediante contraseñas de aplicación de Gmail
- ⚡ Optimizado para funcionar en dispositivos con recursos limitados

El script se ejecuta completamente en terminal, ideal para sistemas sin interfaz gráfica o con recursos muy limitados.

---

## 📥 Instalación

Clona el repositorio desde GitHub:

```bash
git clone https://github.com/XONIDU/xonimail.git
cd xonimail
```

---

## ✅ Requisitos

- Python 3.6+ instalado
- Conexión a internet
- Cuenta de Gmail con verificación en dos pasos activada
- Contraseña de aplicación de Gmail (16 caracteres)

---

## 🔧 Instalación por plataforma

### 🐧 Arch Linux / Manjaro

```bash
# Instalar Python y pip
sudo pacman -S python-pip

# Instalar dependencias Python
pip install -r requisitos.txt --break-system-packages
```

### 🐧 Debian / Ubuntu / antiX / Mint

```bash
# Actualizar repositorios
sudo apt update

# Instalar Python y pip
sudo apt install python3 python3-pip -y

# Instalar dependencias Python
pip3 install -r requisitos.txt --break-system-packages
```

### 🐧 Fedora / RHEL / CentOS

```bash
# Instalar Python y pip
sudo dnf install python3-pip

# Instalar dependencias Python
pip3 install -r requisitos.txt --break-system-packages
```

### 🐧 openSUSE

```bash
# Instalar Python y pip
sudo zypper install python3-pip

# Instalar dependencias Python
pip3 install -r requisitos.txt --break-system-packages
```

### 🍎 macOS

```bash
# Usando Homebrew
brew install python3

# Instalar dependencias Python
pip3 install -r requisitos.txt
```

### 🪟 Windows

1. Instala Python 3 desde [python.org](https://www.python.org/downloads/)
2. Abre una terminal (cmd o PowerShell) y ejecuta:

```bash
pip install -r requisitos.txt
```

### 📱 Termux (Android)

```bash
# Actualizar paquetes
pkg update

# Instalar Python
pkg install python

# Instalar dependencias
pip install -r requisitos.txt
```

---

## 🔑 Configuración del Token

Gmail requiere una **contraseña de aplicación** especial en lugar de tu contraseña normal:

### Cómo obtener tu token:

1. Ve a tu cuenta de Google: https://myaccount.google.com/
2. Ve a **Seguridad**
3. Activa la **Verificación en dos pasos** (si no la tienes activada)
4. Regresa a Seguridad y busca **Contraseñas de aplicación**
5. Selecciona **Correo** y **Windows Computer**
6. Copia la contraseña de 16 caracteres que se genera

### Crear archivo token.txt:

```bash
# Crea el archivo con tu token (reemplaza con tu token real)
echo "tu-token-de-16-caracteres-aqui" > token.txt

# O usando nano/vim
nano token.txt
```

> **Nota:** La contraseña normal de Gmail NO funciona. Debes usar una contraseña de aplicación específica.

---

## ⚙️ Uso

Ejecuta el lanzador:

```bash
python start.py
# o
python3 start.py
```

El programa te guiará paso a paso:

1. Verifica que exista el archivo `token.txt`
2. Solicita tu dirección de correo Gmail
3. Pide el asunto del mensaje
4. Permite redactar el contenido (ENTER dos veces para finalizar)
5. Solicita cantidad de destinatarios y sus direcciones
6. Muestra un resumen del envío
7. Confirma antes de enviar
8. Muestra el progreso y resultado final

### Características interactivas:

- Si **token.txt** no existe, el programa muestra instrucciones para crearlo
- Presiona **CTRL+C** en cualquier momento para salir
- Presiona **ENTER dos veces** para terminar de escribir tu mensaje
- Escribe **'s'** o **'si'** para confirmar el envío

### Accesos directos

El lanzador crea automáticamente accesos directos para facilitar la ejecución:

- **Windows:** `INICIAR_XONIMAIL.bat` (doble clic)
- **Linux:** `INICIAR_XONIMAIL.sh` (ejecutar con `./INICIAR_XONIMAIL.sh`)
- **MacOS:** `INICIAR_XONIMAIL.command` (doble clic)

---

## 📋 Ejemplo de sesión

```
============================================================
XONIMAIL - ENVIO DE CORREOS DESDE TERMINAL
============================================================
(Presiona CTRL+C en cualquier momento para salir)

Tu correo Gmail: usuario@gmail.com
Token cargado desde token.txt

Asunto del correo: Reporte semanal

Escribe tu mensaje (presiona ENTER dos veces para finalizar):
Hola equipo,
Adjunto el reporte de esta semana.
Saludos.

Cuantos destinatarios? (numero): 2

Ingresa los 2 correos:
  Destinatario 1: juan@gmail.com
  Destinatario 2: maria@gmail.com

==================================================
RESUMEN DE ENVIO
==================================================
De: usuario@gmail.com
Asunto: Reporte semanal
Destinatarios: 2
   1. juan@gmail.com
   2. maria@gmail.com

Mensaje:
------------------------------
Hola equipo,
Adjunto el reporte de esta semana.
Saludos.
------------------------------

¿Enviar correos? (s/n): s

Iniciando envio... (CTRL+C para cancelar)
Conectando con servidor Gmail...
Autenticando...

Inicio de sesion exitoso. Enviando correos...

[1/2] Enviado a juan@gmail.com
[2/2] Enviado a maria@gmail.com

==================================================
RESUMEN FINAL
==================================================
Envios exitosos: 2
Envios fallidos: 0
Total procesados: 2
==================================================

Proceso completado! Gracias por usar XONIMAIL
```

---

## ✋ Pausar / Detener

- Para detener el programa en cualquier momento: **Ctrl + C**
- Si necesitas cancelar el envío, responde **'n'** en la confirmación

---

## 🔒 Consideraciones de seguridad y ética

- **No compartas tu archivo token.txt** con nadie
- Tus credenciales solo se usan durante la sesión
- El token se guarda localmente en tu computadora
- Usa SMTP seguro de Gmail con cifrado TLS
- No se envían tus datos a ningún servidor externo
- Este programa es SOLO para fines educativos

---

## 🐛 Problemas comunes

### "Error de autenticación"
- Verifica que el token en token.txt sea correcto
- Asegúrate de tener activada la verificación en dos pasos
- Genera una nueva contraseña de aplicación

### "Error de conexión"
- Revisa tu conexión a internet
- Verifica que el puerto 587 no esté bloqueado
- Prueba con otra red

### "No se encuentra token.txt"
- El programa te guiará para crearlo
- Sigue las instrucciones de la sección "Configuración del Token"

### "Error en Linux con --break-system-packages"
```bash
# Alternativa usando --user
pip install --user -r requisitos.txt
```

---

## 📦 Archivos incluidos

- **start.py** — Lanzador universal (verifica dependencias y ejecuta el programa)
- **xonimail.py** — Programa principal con la funcionalidad de envío de correos
- **requisitos.txt** — Dependencias Python (solo por compatibilidad)
- **token.txt** — Archivo con tu token (debes crearlo)
- **README.md** — Este archivo de documentación

---

## 📊 Nota sobre dependencias

XONIMAIL **solo usa librerías estándar de Python**:
- `smtplib` - Para conexión SMTP con Gmail
- `email` - Para construir mensajes de correo

No se requieren dependencias externas. El archivo `requisitos.txt` es solo por compatibilidad con el sistema de instalación.

---

## ✉️ Contacto y Créditos

- **Proyecto:** XONIMAIL
- **Contacto:** xonidu@gmail.com
- **Creador:** Darian Alberto Camacho Salas
- **Somos XONIDU**

