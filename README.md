# 📧 XONIMAIL - Cliente de Gmail para Terminal
# Creador: Darian Alberto Camacho Salas
# Equipo: XONIDU

**Sistema de envío de correos desde terminal para dispositivos de bajos recursos**

---

## 🎯 Objetivo

XONIMAIL es un cliente liviano de Gmail diseñado para ejecutarse completamente en terminal, ideal para:

- 📨 **Enviar** correos electrónicos sin necesidad de navegador web
- 💻 **Funcionar** en dispositivos de bajos recursos (ASUS Eee PC, laptops antiguas)
- 🔐 **Autenticarse** de forma segura mediante contraseñas de aplicación
- 📤 **Gestionar** múltiples destinatarios en un solo envío
- 📝 **Redactar** mensajes multilínea de forma interactiva
- ⚡ **Optimizar** el uso de recursos del sistema

---

## ⚙️ ¿Qué hace?

**Autenticación Segura:** Usa contraseñas de aplicación de Gmail almacenadas en token.txt

**Composición Interactiva:** Escribe mensajes con múltiples líneas (ENTER dos veces para finalizar)

**Múltiples Destinatarios:** Envía a uno o varios correos simultáneamente

**Gestión de Tokens:** Si no existe token.txt, muestra instrucciones detalladas para crearlo

**Resumen de Envío:** Vista previa antes de enviar con confirmación

**Estadísticas:** Reporte de envíos exitosos y fallidos

### Características principales:

- ✅ Interfaz 100% terminal - Sin dependencias gráficas
- ✅ Lectura automática de token desde archivo
- ✅ Instrucciones integradas para obtener contraseña de aplicación
- ✅ Manejo de errores con soluciones sugeridas
- ✅ Interrupción segura con CTRL+C
- ✅ Composición de mensajes multilínea
- ✅ Confirmación antes de enviar
- ✅ Resumen detallado de envíos
- ✅ Compatible con Python 3.6+

---

## 📥 Instalación

### Requisitos previos
- Python 3.6 o superior
- pip (gestor de paquetes de Python)
- Conexión a internet
- Cuenta de Gmail con verificación en dos pasos activada

### Pasos de instalación

1. **Clona el repositorio:**
```bash
git clone https://github.com/XONIDU/xonimail.git
cd xonimail
```

2. **Instala las dependencias (solo por compatibilidad):**

#### 🐧 Arch Linux / Manjaro
```bash
sudo pacman -S python-pip
pip install --break-system-packages -r requisitos.txt
```

#### 🐧 Debian / Ubuntu / antiX
```bash
sudo apt update
sudo apt install python3 python3-pip -y
pip3 install --break-system-packages -r requisitos.txt
```

#### 🐧 Fedora / RHEL / CentOS
```bash
sudo dnf install python3-pip
pip3 install --break-system-packages -r requisitos.txt
```

#### 🐧 openSUSE
```bash
sudo zypper install python3-pip
pip3 install --break-system-packages -r requisitos.txt
```

#### 🍎 macOS
```bash
# Usando Homebrew
brew install python3
pip3 install -r requisitos.txt

# O usando pip directamente
pip3 install -r requisitos.txt
```

#### 🪟 Windows
```bash
# En Command Prompt o PowerShell
pip install -r requisitos.txt

# Si tienes problemas con permisos
pip install --user -r requisitos.txt
```

#### 📱 Termux (Android)
```bash
pkg update
pkg install python
pip install -r requisitos.txt
```

> **Nota:** Este programa solo usa librerías estándar de Python. El archivo requisitos.txt es solo por compatibilidad con pip.

---

## 🔑 Cómo obtener tu token de Gmail

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

## 🚀 Uso del sistema

### 1. Crear archivo de token
```bash
# Crea el archivo token.txt con tu contraseña de aplicación
echo "tu-token-de-16-caracteres-aqui" > token.txt
# o usa nano/vim
nano token.txt
```

### 2. Ejecutar el programa
```bash
python start.py
# o
python3 start.py
```

### 3. Seguir las instrucciones interactivas
```
============================================================
XONIMAIL - ENVIO DE CORREOS DESDE TERMINAL
============================================================
(Presiona CTRL+C en cualquier momento para salir)

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

---

## 📁 Estructura del proyecto

```
xonimail/
├── 📄 start.py                 # Archivo principal del programa
├── 📄 token.txt                # Tu token de Gmail (debes crearlo)
├── 📄 requisitos.txt         # Dependencias de Python (solo compatibilidad)
└── 📄 README.md                # Este archivo
```

---

## 📋 Ejemplo de sesión completa

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

Tu correo Gmail: darian@gmail.com
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
De: darian@gmail.com
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

## 🔧 Solución de problemas

### Error de autenticación
```
╔══════════════════════════════════════════════════════════╗
║                    POSIBLES SOLUCIONES                   ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  • Verifica que el token en token.txt sea correcto       ║
║  • Asegurate de tener activada la verificación en        ║
║    dos pasos en tu cuenta de Gmail                       ║
║  • Genera una nueva contraseña de aplicación             ║
║  • Borra token.txt y crea uno nuevo                      ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝
```

### Error de conexión
- Revisa tu conexión a internet
- Verifica que el puerto 587 no esté bloqueado
- Prueba con otra red

### Error de permisos en Linux
```bash
# Si tienes problemas con --break-system-packages
pip install --user -r requisitos.txt
```

---

## 🔒 Nota de Seguridad

- Tus credenciales solo se usan durante la sesión
- El token se guarda localmente en token.txt
- No se envían tus datos a ningún servidor externo
- Usa SMTP seguro de Gmail con cifrado TLS
- No compartas tu archivo token.txt con nadie

---

## 👨‍💻 Desarrollador

**Darian Alberto Camacho Salas**

---

## 📞 Contacto

¿Dudas, sugerencias o reportes de errores?

**Instagram:** @xonidu

**Facebook:** xonidu

**Email:** xonidu@gmail.com

---

## 📝 Licencia

Este proyecto está bajo una **licencia educativa**. El código puede ser utilizado con fines de aprendizaje y enseñanza, siempre respetando los derechos de autor y dando crédito al desarrollador.

**No se permite el uso comercial no autorizado ni la redistribución sin permiso explícito.**

---

### ⚡ XONIMAIL v1.0 - Cliente de Gmail para Terminal ⚡
