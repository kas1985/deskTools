# deskTools

Version: `2026 deskTools v1.0`

App de escritorio hecha con Flet para monitorizar y mantener un PC.

## Contenido

- Resumen del sistema: CPU, memoria, disco, uptime, red y procesos destacados.
- Procesos: lista de procesos activos con opcion de solicitar cierre.
- Modo juegos: consulta y cambio de plan de energia, modo juego y recursos actuales.
- Video: descarga local de videos mediante `yt-dlp`.
- Almacenamiento: uso de disco y limpieza de temporales del usuario.
- Red: interfaces, trafico acumulado y prueba de ping.

## Estructura

```text
.
|-- main.py
|-- requirements.txt
|-- README.md
`-- app/
    |-- config.py
    |-- data.py
    |-- components.py
    |-- layout.py
    |-- theme.py
    |-- services/
    |   |-- formatting.py
    |   |-- network.py
    |   |-- performance.py
    |   |-- storage.py
    |   |-- system.py
    |   `-- video.py
    `-- views/
        |-- dashboard.py
        |-- downloader.py
        |-- gaming.py
        |-- network.py
        |-- processes.py
        `-- storage.py
```

## Versionado

Cuando se haga una modificacion importante del proyecto, subir la version en `0.1` tanto en `app/config.py` como en este README, y registrar debajo las modificaciones realizadas.

## Historial

### 2026 deskTools v1.0

- Primera version funcional con panel de recursos del sistema.
- Secciones de procesos, modo juegos, descarga de video, almacenamiento y red.
- Servicios separados para sistema, rendimiento, almacenamiento, red y video.
- Interfaz visual basada en Flet con navegacion lateral.

## Ejecutar

```powershell
.\.venv\Scripts\activate
python main.py
```

Tambien puedes ejecutarla sin activar el entorno:

```powershell
.\.venv\Scripts\python.exe main.py
```
