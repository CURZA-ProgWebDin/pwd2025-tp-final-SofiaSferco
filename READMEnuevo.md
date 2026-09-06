<<<<<<< HEAD
# Trabajo Final  
## Programación Web Dinámica  
### Tecnicatura Universitaria en Desarrollo Web  

---

## Consigna  

Para este **trabajo/proyecto final** deberán aplicar todos los conceptos aprendidos en la materia. El objetivo es desarrollar una aplicación web a elección, la cual debe contar con los siguientes elementos:

- Un **frontend** desarrollado con **Vue.js**  
- Un **backend** utilizando **Flask**, que sirva al frontend y realice las consultas a la base de datos  
- Una **base de datos**, pueden optar por **MySQL** o **PostgreSQL**  

El desarrollo debe seguir el patrón **MVC** (Modelo - Vista - Controlador), tal como se trabajó a lo largo de la cursada.

Los puntos clave que deberán demostrar en el proyecto son:

- Creación de los módulos con sus respectivos modelos, controladores y rutas  
- Consumo de los recursos del backend desde el frontend, utilizando una **API RESTful** (Interfaz de Programación de Aplicaciones bajo el estilo arquitectónico de Transferencia de Estado Representacional)  
- Consumo y manipulación de datos desde la base de datos  

---

## Consideraciones  

La estructura del proyecto puede variar según el criterio personal, pero es fundamental que mantenga una **organización lógica y ordenada**, lo cual facilitará el mantenimiento, la comprensión y la modificación de la aplicación.

⚠️ **Importante:**  
No se aceptarán proyectos que no cumplan con los ítems solicitados en la consigna, ni se considerará aprobado si la aplicación no funciona correctamente en su totalidad.

Los requerimientos mínimos son:

✅ Al menos **4 módulos**, de los cuales al menos **2 deben estar relacionados entre sí**  
✅ Implementar un **CRUD** básico (_Create, Read, Update y Delete_)  
✅ Cuidar el **aspecto visual** de la aplicación, incluyendo:  

- Botones  
- Menú de navegación  
- Formularios  
- Validaciones  
- Jerarquía tipográfica  

---

## Sugerencias de Aplicaciones  

Pueden desarrollar el tipo de aplicación que deseen, aquí algunos ejemplos para inspirarse:

- Sistema de gestión de turnos para una veterinaria  
- Menú digital de un restaurante, con precios y categorías  
- Control de stock y precios para una cervecería  
- Aplicación de gestión para un estacionamiento  
- Sistema de control y gestión de una heladería  

---

## Aspectos Esperados  

- Aplicación **100% funcional**  
- Aplicación de los conceptos vistos en la materia  
- Pensamiento crítico sobre el proyecto realizado  
- Análisis y planificación de la mejor forma de estructurar la aplicación, considerando:  
  - Relación entre los módulos  
  - Interacción entre los distintos elementos del sistema  
=======
# Sistema de Gestion y Seguimiento de Obras

Aplicacion academica para administrar el ciclo **Cliente -> Cotizacion -> Obra -> Factura -> Pago**. Esta version conserva las carpetas convencionales del proyecto y utiliza nombres internos en espanol para facilitar la lectura y la defensa del codigo.

El frontend es una SPA de escritorio desarrollada con Vue 3. El backend expone una API REST con Flask y accede a PostgreSQL mediante SQL directo y `psycopg`, sin ORM.

## Requisitos

- Python 3.10 o superior.
- Node.js 18.19 o superior y npm 9 o superior.
- PostgreSQL 14 o superior.
- Cliente `psql` disponible en la terminal.

Cada persona debe utilizar su propia base y sus credenciales locales de PostgreSQL. Los archivos `.env` contienen configuracion local, estan ignorados por Git y no deben versionarse.

## Inicio En Windows PowerShell

Ejecutar los comandos desde la carpeta raiz del proyecto.

### Primera preparacion

Preparar Python e instalar las dependencias del backend:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend\requirements.txt
```

Crear la base, las tablas y los datos de prueba. Reemplazar `TU_USUARIO` y `TU_BASE` por los datos locales:

```powershell
createdb -U TU_USUARIO TU_BASE
psql -U TU_USUARIO -d TU_BASE -f backend\database\schema.sql
psql -U TU_USUARIO -d TU_BASE -f backend\database\seed.sql
```

Si la base ya existe y tiene cargados el schema y el seed, no ejecutar nuevamente estos tres comandos.

Crear el archivo de configuracion la primera vez y abrirlo con Notepad:

```powershell
Copy-Item backend\.env.example backend\.env
notepad backend\.env
```

Si `backend\.env` ya existe, abrirlo directamente:

```powershell
python -m backend.aplicacion
```

Completarlo con los datos de la base que se utilizara:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=TU_BASE
DB_USER=TU_USUARIO
DB_PASSWORD=TU_CONTRASENA
```

Preparar el frontend la primera vez:

```powershell
Set-Location frontend
Copy-Item .env.example .env
npm ci

npm run dev
```

### Arranque habitual

Iniciar el backend desde la carpeta raiz y mantener la terminal abierta:

```powershell
.\.venv\Scripts\Activate.ps1
python -m backend.aplicacion
```

En otra terminal, desde la carpeta raiz, iniciar el frontend:

```powershell
Set-Location frontend
npm run dev
```

Abrir la URL informada por Vite, habitualmente `http://localhost:5173`.

## Primera Preparacion: Linux Y macOS

Desde la carpeta raiz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r backend/requirements.txt
cp backend/.env.example backend/.env
```

Elegir solamente el caso que corresponda para preparar PostgreSQL.

### Caso 1: crear una base nueva

Reemplazar `TU_USUARIO` y `TU_BASE` por los valores locales. Estos comandos crean la base, las tablas y los datos de demostracion:

```bash
createdb -U TU_USUARIO TU_BASE
psql -U TU_USUARIO -d TU_BASE -f backend/database/schema.sql
psql -U TU_USUARIO -d TU_BASE -f backend/database/seed.sql
```

### Caso 2: usar una base existente vacia

No ejecutar `createdb`. Crear las tablas y, si se necesitan datos de demostracion, ejecutar tambien el seed:

```bash
psql -U TU_USUARIO -d TU_BASE -f backend/database/schema.sql
psql -U TU_USUARIO -d TU_BASE -f backend/database/seed.sql
```

El segundo comando es opcional.

### Caso 3: usar una base con las tablas del proyecto

No ejecutar `createdb`, `schema.sql` ni `seed.sql`. Configurar solamente la conexion en `backend/.env`.

En cualquiera de los tres casos, completar `backend/.env` con los datos reales de PostgreSQL:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=TU_BASE
DB_USER=TU_USUARIO
DB_PASSWORD=TU_CONTRASENA
```

Guardar el archivo y luego iniciar la API:

```bash
python -m backend.aplicacion
```

En otra terminal:

```bash
cd frontend
cp .env.example .env
npm ci
npm run dev
```

La API queda disponible en `http://localhost:5000/api`. Vite informa la URL del frontend, habitualmente `http://localhost:5173`.

## Verificacion Disponible

Esta variante no contiene una suite de pruebas automatizadas. La comprobacion disponible en el repositorio es la compilacion de produccion del frontend:

```bash
cd frontend
npm ci
npm run build
```

La salida `frontend/dist/` es generada y no forma parte del codigo fuente.

## Estructura Real

```text
backend/
  aplicacion.py  Entrada y configuracion general de Flask
  config/        Variables de entorno
  controllers/   Validaciones y reglas de negocio
  database/      Conexion, schema y seed
  models/        Consultas SQL directas
  routes/        Blueprints y endpoints REST
  utils/         Validaciones y transformaciones compartidas
frontend/
  index.html      Documento inicial cargado por el navegador
  src/
    principal.js  Entrada de Vue
    Aplicacion.vue Componente raiz
    components/   Componentes reutilizables y formularios
    router/       Rutas de la SPA
    services/     Cliente Axios y servicios por recurso
    stores/       Estado Pinia por recurso
    views/        Inicio y vistas de los cinco modulos
```

## Recorrido General

```text
Usuario
-> Vista Vue
-> Store Pinia
-> Servicio Axios
-> Ruta Flask
-> Controlador
-> Modelo con SQL directo
-> PostgreSQL
-> Respuesta JSON
-> Actualizacion de la interfaz
```

Los requisitos originales y las decisiones generales de alcance, arquitectura y negocio se encuentran en `../README.md` y `../PROJECT.md`.
>>>>>>> 784b43a (project)
