# 🎮 Preguntón

Quiz multijugador en tiempo real, estilo Kahoot, en un único archivo HTML. Los alumnos se conectan desde su móvil con un PIN mientras el profesor controla la partida desde la pantalla proyectada.

Funciona como página estática (compatible con **GitHub Pages**) y usa **Firebase Realtime Database** para sincronizar host y jugadores en tiempo real.

---

## 📁 Archivos del proyecto

| Archivo | Descripción |
|---|---|
| `pregunton.html` | La aplicación completa (host + jugador en un solo archivo) |
| `firebase-config.json` | Credenciales de tu proyecto de Firebase |
| `questions.json` | Las preguntas del quiz |

**Los tres archivos deben estar en la misma carpeta.** La app carga `firebase-config.json` y `questions.json` mediante `fetch()` al iniciar.

---

## 🔧 Configuración inicial

### 1. Crear un proyecto en Firebase

1. Ve a [console.firebase.google.com](https://console.firebase.google.com) y crea un proyecto nuevo.
2. Añade una app **Web** (`</>`) dentro del proyecto y copia el objeto de configuración que te muestra.
3. Ve a **Compilación → Realtime Database** → **Crear base de datos** → elige una región → selecciona **modo de prueba**.
4. En la pestaña **Reglas**, asegúrate de ajustarlas.
5. Rellenar `config.dat`

### 3. Editar `questions.json`

Cada pregunta sigue este formato:

```json
{
  "text": "¿Qué significa CPU?",
  "options": ["Opción A", "Opción B", "Opción C", "Opción D"],
  "correct": 2,
  "time": 20
}
```

- `correct`: índice (0-3) de la opción correcta.
- `time`: segundos disponibles para responder.

Puedes añadir tantas preguntas como quieras al array.

### 3.1 Varios cuestionarios predefinidos (opcional)

Si quieres poder elegir entre varios temarios antes de crear la partida (por ejemplo "Sistemas Operativos", "Redes"...), crea un archivo `quiz-sets.json` junto a los demás:

```json
[
  { "name": "Sistemas Operativos", "file": "questions.json" },
  { "name": "Redes",               "file": "questions-redes.json" }
]
```

Cada `file` debe ser un JSON con el mismo formato que `questions.json`, en la misma carpeta. Si `quiz-sets.json` no existe, la app usa `questions.json` por defecto como única opción, igual que antes.

### 3.2 Subir un cuestionario propio al vuelo

En la pantalla "Crear partida" también hay un botón **"📂 Subir mi propio JSON"**: el profesor puede elegir un archivo `.json` desde su móvil u ordenador en el momento, sin tocar el repositorio ni GitHub Pages. Si sube un archivo, ese es el que se usa (tiene prioridad sobre el desplegable).

---

## 💻 Probarlo en local

Como la app usa `fetch()` para cargar los JSON, **no puedes abrir el HTML con doble clic** (falla por CORS en `file://`). Necesitas un servidor local:

```bash
# Con Python (Mac/Linux/Windows)
python3 -m http.server 8000

# Con Node.js
npx serve .
```

Luego abre `http://localhost:8000/pregunton.html`.

Para probarlo desde el móvil de otra persona en la misma red WiFi, usa tu IP local en vez de `localhost` (ej. `http://192.168.1.50:8000/pregunton.html`).

---

## 🚀 Publicarlo en GitHub Pages

1. Sube `pregunton.html`, `firebase-config.json` y `questions.json` a un repositorio de GitHub.
2. Ve a **Settings → Pages** del repositorio.
3. En **Source**, elige la rama (`main`) y la carpeta (`/root`).
4. Guarda; GitHub te dará una URL tipo `https://tu-usuario.github.io/tu-repo/pregunton.html`.

---

## 🕹️ Cómo se usa

1. Abre la URL en el proyector/pantalla del aula y pulsa **"Soy el Host"** → **Crear partida**. Aparecerá un PIN de 4 dígitos.
2. Cada alumno abre la misma URL en su móvil, pulsa **"Soy Jugador"**, introduce el PIN y su nombre.
3. El host ve en tiempo real quién se va conectando y pulsa **Empezar** cuando estén todos.
4. Por cada pregunta: los jugadores responden contrarreloj, el host pulsa **Mostrar resultados** para revelar y actualizar el ranking, y **Siguiente pregunta** para continuar.
5. Al terminar todas las preguntas, se muestra el ranking final.

### Puntuación

Cada acierto suma entre 500 y 1000 puntos: 500 puntos base + hasta 500 extra según la rapidez de la respuesta.

---

## ⚠️ Avisos importantes

- **Seguridad**: las reglas de la base de datos en modo de prueba dejan los datos abiertos a cualquiera con el enlace. No es un problema para un uso puntual en clase, pero cierra el acceso o borra el proyecto después.
- **Coste**: el plan gratuito (Spark) de Firebase no requiere tarjeta de pago y sus límites son más que suficientes para una clase. No hay riesgo de facturación mientras no vincules manualmente una cuenta de facturación y actives el plan Blaze.
- **Sin backend propio**: toda la sincronización en tiempo real la gestiona Firebase; GitHub Pages solo sirve los archivos estáticos.

---

## 🛠️ Tecnologías usadas

- HTML, CSS y JavaScript puro (sin frameworks ni librerías de UI).
- [Firebase Realtime Database](https://firebase.google.com/docs/database) (SDK compat vía CDN).
- Diseño responsive con Flexbox, Grid y `clamp()` para pantallas móviles.
