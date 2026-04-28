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
- 🚀 Instalación directa desde AUR con `yay`

El script se ejecuta completamente en terminal, ideal para sistemas sin interfaz gráfica o con recursos muy limitados.

---

## 📥 Instalación

### Arch Linux / Manjaro (AUR)

```bash
# Instalar desde AUR
yay -S xonimail
```

### Desde GitHub (otras distribuciones)

```bash
# Clonar el repositorio
git clone https://github.com/XONIDU/xonimail.git
cd xonimail

# Instalar dependencias
pip install -r requisitos.txt

# Ejecutar
python start.py
```

---

## 🔧 Instalación por plataforma (desde GitHub)

### 🐧 Arch Linux / Manjaro

```bash
sudo pacman -S python-pip
pip install --break-system-packages -r requisitos.txt
```

### 🐧 Debian / Ubuntu / antiX / Mint

```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install --break-system-packages -r requisitos.txt
```

### 🐧 Fedora

```bash
sudo dnf install python3-pip
pip3 install --break-system-packages -r requisitos.txt
```

### 🍎 macOS

```bash
brew install python3
pip3 install -r requisitos.txt
```

### 🪟 Windows

```bash
pip install -r requisitos.txt
```

---

## 🔑 Configuración del Token

Gmail requiere una **contraseña de aplicación** especial en lugar de tu contraseña normal.

### Crear directorio y archivo token:

```bash
# Crear directorio
mkdir -p ~/.xonimail

# Editar archivo token
nano ~/.xonimail/token.txt
```

### Contenido de `~/.xonimail/token.txt`:

```bash
# Tu contraseña de aplicacion de Gmail (16 caracteres)
# Obtenla en: https://myaccount.google.com/apppasswords
# Requiere verificacion en dos pasos activada

# Ejemplo:
# abcd1234efgh5678

# Pega tu token abajo (sin espacios):
```

### Establecer permisos seguros:

```bash
chmod 600 ~/.xonimail/token.txt
```

### Cómo obtener tu token:

```
╔══════════════════════════════════════════════════════════╗
║     INSTRUCCIONES PARA OBTENER CONTRASEÑA DE APLICACIÓN  ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  1. Ve a tu cuenta de Google:                           ║
║     https://myaccount.google.com/                        ║
║                                                          ║
║  2. Ve a "Seguridad"                                     ║
║                                                          ║
║  3. Activa la "Verificación en dos pasos"                ║
║     (si no la tienes activada)                           ║
║                                                          ║
║  4. Regresa a Seguridad y busca                          ║
║     "Contraseñas de aplicación"                          ║
║                                                          ║
║  5. Selecciona "Correo" y "Windows Computer"             ║
║                                                          ║
║  6. Copia la contraseña de 16 caracteres                 ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

> **Importante:** La contraseña normal de Gmail NO funciona. Debes usar una contraseña de aplicación específica.

---

## ⚙️ Uso

### Ejecutar el programa:

```bash
xonimail
```

O desde el directorio de instalación manual:

```bash
python start.py
# o
python3 start.py
```

### Flujo interactivo:

1. El programa verifica que exista `~/.xonimail/token.txt`
2. Solicita tu dirección de correo Gmail
3. Pide el asunto del mensaje
4. Permite redactar el contenido (ENTER dos veces para finalizar)
5. Solicita cantidad de destinatarios y sus direcciones
6. Muestra un resumen del envío
7. Confirma antes de enviar
8. Muestra el progreso y resultado final

### Controles:

- **CTRL+C** - Salir del programa en cualquier momento
- **ENTER dos veces** - Terminar de escribir el mensaje
- **s / si** - Confirmar envío

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

## 📁 Estructura de archivos

### Instalación desde AUR:

```
/usr/bin/xonimail                 # Ejecutable principal
/usr/share/xonimail/xonimail.py   # Programa principal
/usr/share/doc/xonimail/README.md # Documentación
~/.xonimail/token.txt             # Tu token (debes crearlo)
```

### Instalación manual:

```
xonimail/
├── start.py                 # Lanzador principal
├── xonimail.py              # Programa principal
├── requisitos.txt           # Dependencias
└── README.md                # Documentación
```

---

## 🔧 Solución de problemas

### Error de autenticación

- Verifica que el token en `~/.xonimail/token.txt` sea correcto
- Asegúrate de tener activada la verificación en dos pasos
- Genera una nueva contraseña de aplicación

### Error: No se encuentra token.txt

```bash
mkdir -p ~/.xonimail
nano ~/.xonimail/token.txt
# Pega tu token y guarda
chmod 600 ~/.xonimail/token.txt
```

### Error de conexión

- Revisa tu conexión a internet
- Verifica que el puerto 587 no esté bloqueado
- Prueba con otra red

### Error en Arch Linux con --break-system-packages

```bash
# Alternativa usando --user
pip install --user -r requisitos.txt
```

---

## 📦 Dependencias

XONIMAIL **solo usa librerías estándar de Python**:

- `smtplib` - Para conexión SMTP con Gmail
- `email` - Para construir mensajes de correo

No se requieren dependencias externas adicionales.

---

## 🔒 Nota de Seguridad

- Tus credenciales solo se usan durante la sesión
- El token se guarda localmente en `~/.xonimail/token.txt`
- No se envían tus datos a ningún servidor externo
- Usa SMTP seguro de Gmail con cifrado TLS
- No compartas tu archivo token.txt con nadie

---

## 📊 Comandos útiles

### Actualizar XONIMAIL (AUR):

```bash
yay -S xonimail --rebuild
```

### Desinstalar:

```bash
sudo pacman -R xonimail
```

### Ver archivos instalados:

```bash
pacman -Ql xonimail
```

---

## ✉️ Contacto y Créditos

- **Proyecto:** XONIMAIL
- **Contacto:** xonidu@gmail.com
- **Creador:** Darian Alberto Camacho Salas
- **Organización:** XONIDU
- **AUR:** https://aur.archlinux.org/xonimail
- **GitHub:** https://github.com/XONIDU/xonimail

---

**Hecho para computación de bajos recursos** ⚡

