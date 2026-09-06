# PROJECT.md

# Sistema de Gestión y Seguimiento de Obras

## 1. Objetivo del proyecto

Desarrollar una aplicación web denominada **Sistema de Gestión y Seguimiento de Obras** que permita gestionar y realizar el seguimiento integral de las obras ejecutadas por una empresa.

El sistema administra el ciclo:

**Cliente → Cotización → Obra → Factura → Pago**

Debe permitir centralizar la información comercial, operativa y económica relacionada con las obras y facilitar el seguimiento de su ejecución, facturación y cobro.

---

## 2. Contexto y alcance

El proyecto corresponde inicialmente a un trabajo práctico académico.

Sin embargo, las decisiones de diseño deben evitar bloquear innecesariamente una posible evolución futura hacia un sistema utilizado en un entorno real.

Toda decisión adicional debe distinguir entre:

1. requisito necesario para la entrega actual;
2. decisión mínima tomada para no bloquear una evolución futura;
3. mejora opcional fuera del alcance actual.

No deben implementarse funcionalidades futuras solamente porque podrían resultar útiles.

### Dentro del alcance

El sistema gestionará:

* Clientes.
* Cotizaciones.
* Obras.
* Facturas.
* Pagos.
* Estado de ejecución de las obras.
* Estado de facturación.
* Estado de cobro.

### Fuera del alcance actual

Quedan fuera del alcance:

* Proveedores.
* Materiales.
* Compras.
* Maquinaria.
* Empleados.
* Gestión avanzada de recursos.
* Otras funcionalidades ajenas a la administración y seguimiento definido para las obras.

Podrán considerarse en futuras versiones, pero no deben implementarse durante el alcance actual.

### Dashboard

El Dashboard es una mejora opcional.

Solo debe considerarse después de completar correctamente los módulos CRUD principales.

---

## 3. Requisitos funcionales generales

El sistema debe permitir:

* Registrar, consultar, modificar y eliminar clientes cuando las reglas de negocio lo permitan.
* Registrar, consultar, modificar y eliminar cotizaciones.
* Asociar cada cotización a un cliente.
* Crear manualmente una obra a partir de una cotización aceptada.
* Registrar, consultar, modificar y eliminar obras cuando las reglas de negocio lo permitan.
* Administrar el estado de ejecución de las obras.
* Registrar, consultar, modificar y eliminar facturas.
* Asociar cada factura a una obra.
* Registrar, consultar, modificar y eliminar pagos.
* Asociar cada pago a una factura.
* Consultar el estado de ejecución, facturación y cobro de las obras.

---

## 4. Stack tecnológico obligatorio

### Frontend

* Vue.js
* JavaScript
* Vue Router
* Pinia
* Axios
* Vite

### Backend

* Python
* Flask
* Flask Blueprints
* API REST
* Arquitectura MVC

### Base de datos

* PostgreSQL

### Comunicación

Frontend y backend deben mantenerse separados.

La comunicación se realizará mediante solicitudes HTTP a una API REST desarrollada con Flask.

Los datos se intercambiarán en formato JSON.

Axios será utilizado desde Vue para consumir los endpoints de la API.

No reemplazar estas tecnologías ni incorporar frameworks alternativos sin una decisión explícita.

---

## 5. Principio de diseño de datos

El modelo debe mantenerse lo más simple, coherente y normalizado posible dentro del alcance del proyecto.

Como criterio general:

**Todo dato que pueda derivarse de manera confiable a partir de información ya almacenada debe calcularse cuando sea necesario, evitando almacenarlo redundantemente o crear tablas auxiliares innecesarias.**

Por lo tanto:

* no crear tablas auxiliares para valores que puedan resolverse razonablemente mediante selects y validaciones;
* no almacenar estados derivados cuando puedan calcularse a partir de relaciones y datos existentes;
* evitar duplicación innecesaria de información;
* utilizar consultas para obtener totales, estados e indicadores derivados cuando corresponda.

Los datos derivados pueden utilizarse normalmente para consultas, filtros, estadísticas, totales, indicadores y futuras métricas del Dashboard.

---

## 6. Arquitectura general

La aplicación utilizará una arquitectura cliente-servidor.

Flujo general:

Usuario

↓

Frontend Vue.js

↓

Axios / HTTP / JSON

↓

API REST Flask

↓

Controladores y modelos

↓

PostgreSQL

↓

Respuesta JSON

↓

Frontend actualiza la interfaz

### Frontend

Responsabilidades:

* Interfaz de usuario.
* Navegación.
* Formularios.
* Validaciones iniciales.
* Visualización de información.
* Gestión del estado de la aplicación.
* Consumo de la API REST.

### Backend

Responsabilidades:

* API REST.
* Lógica de negocio.
* Validaciones.
* Operaciones CRUD.
* Coordinación con PostgreSQL.
* Protección de las reglas del sistema.
* Cálculo de información derivada cuando corresponda.

### Base de datos

Responsabilidades:

* Persistencia.
* Relaciones.
* Integridad referencial.
* Restricciones.
* Claves primarias.
* Claves foráneas.
* Restricciones de unicidad.

Las reglas críticas no deben depender únicamente del frontend.

---

## 7. Arquitectura Backend

Estructura prevista:

backend/

* app.py
* config/
* controllers/
* models/
* routes/
* database/
* utils/
* requirements.txt
* .env

### app.py

Punto de entrada de Flask y configuración general de la aplicación.

### config/

Configuración del proyecto y manejo de variables de entorno.

### controllers/

Lógica de negocio y procesamiento de las solicitudes.

### models/

Representación de las entidades y operaciones relacionadas con PostgreSQL.

### routes/

Definición de endpoints REST.

Las rutas deben organizarse mediante Flask Blueprints.

### database/

Configuración de la conexión con PostgreSQL y scripts relacionados con la base de datos.

### utils/

Solo debe utilizarse cuando exista una necesidad concreta de funciones auxiliares reutilizables.

No crear capas adicionales como `services`, `schemas` u otras abstracciones sin una necesidad concreta y aprobación previa.

---

## 8. Arquitectura Frontend

El frontend será una **Single Page Application (SPA)** desarrollada con Vue.js.

Estructura prevista:

frontend/

* public/
* src/

  * assets/
  * components/
  * views/
  * router/
  * stores/
  * services/
  * App.vue
  * main.js
* package.json
* vite.config.js

### assets/

Recursos estáticos.

### components/

Componentes reutilizables.

### views/

Vistas principales correspondientes a los módulos.

### router/

Configuración de Vue Router.

### stores/

Gestión del estado mediante Pinia.

### services/

Servicios encargados de consumir la API mediante Axios.

### App.vue

Componente principal.

### main.js

Punto de entrada del frontend.

---

## 9. Componentes de interfaz previstos

La interfaz debe ser minimalista, clara, consistente y comprensible.

Se podrán utilizar componentes reutilizables para:

* navegación;
* encabezados;
* tablas;
* formularios;
* botones;
* confirmaciones;
* mensajes de validación;
* notificaciones.

Las vistas principales serán:

* Clientes.
* Cotizaciones.
* Obras.
* Facturas.
* Pagos.

Dashboard será opcional.

No crear componentes genéricos o abstracciones solamente para anticipar necesidades futuras.

---
# MODELO DE DATOS

## 10. Entidad Cliente

Representa una persona física o jurídica para la cual la empresa realiza cotizaciones y ejecuta obras.

### Campos

`id_cliente`

* SERIAL
* PRIMARY KEY
* generado automáticamente.

`cuit_cuil`

* VARCHAR(11)
* NOT NULL
* UNIQUE.

`razon_social`

* TEXT
* NOT NULL.

`responsable`

* TEXT
* opcional.

`telefono`

* TEXT
* opcional.

`email`

* TEXT
* opcional.

### Relaciones

Cliente 1 → N Cotizaciones

La relación entre Cliente y Obra es indirecta:

**Cliente → Cotización → Obra**

Un Cliente puede tener múltiples Obras a través de sus Cotizaciones, pero la tabla `Obra` no almacena directamente `id_cliente`.

### Reglas de negocio

* El CUIT/CUIL debe ser único.
* El CUIT/CUIL debe almacenarse normalizado, sin espacios ni guiones, y contener exactamente 11 dígitos numéricos.
* No se implementará durante el alcance actual la validación matemática del dígito verificador.
* La razón social es obligatoria.
* Un Cliente puede registrar múltiples Cotizaciones.
* Un Cliente puede tener múltiples Obras indirectamente a través de sus Cotizaciones.
* No puede registrarse una Cotización sin Cliente.
* Toda Obra pertenece indirectamente al Cliente correspondiente a su Cotización de origen.
* Un Cliente puede eliminarse únicamente cuando no posea Cotizaciones asociadas.
* No es necesario comprobar directamente la existencia de Obras para eliminar un Cliente, ya que toda Obra deriva obligatoriamente de una Cotización.
* Los campos de texto deberán respetar las reglas generales de normalización y validación definidas en la sección 41.

---

## 11. Entidad Cotización

Representa una propuesta comercial presentada a un cliente con el objetivo de obtener la contratación de una obra.

Se utiliza una única entidad para representar los diferentes tipos de contratación.

### Tipos permitidos

* Presupuesto.
* Licitación pública.
* Licitación privada.
* Concurso de precios.
* Compra directa.

No crear tablas independientes para cada tipo.

### Estados

Todos los tipos de Cotización utilizan exactamente los mismos tres estados:

* **Presentada.**
* **Aceptada.**
* **Rechazada.**

No incorporar estados diferentes según el tipo de contratación.

No incorporar:

* borrador;
* en preparación;
* en evaluación;
* adjudicada;
* aprobada;
* perdida;
* otros estados intermedios.

### Campos

`id_cotizacion`

* SERIAL
* PRIMARY KEY.

`codigo_cotizacion`

* VARCHAR(20)
* UNIQUE.
* generado automáticamente.
* formato previsto: `COT-YYYY-NNN`.

`id_cliente`

* INTEGER
* FOREIGN KEY → Cliente
* NOT NULL.

`tipo_cotizacion`

* VARCHAR(30)
* NOT NULL.

`numero_contratacion`

* TEXT
* condicional.

`titulo`

* TEXT
* NOT NULL.

`fecha`

* DATE
* NOT NULL.

`monto`

* NUMERIC(12,2)
* NOT NULL.

`estado`

* VARCHAR(20)
* NOT NULL.

### Reglas

* Toda Cotización pertenece a un Cliente existente.
* El código es único y generado automáticamente.
* El tipo debe seleccionarse entre las opciones definidas.
* El número de contratación es obligatorio para Licitación Pública, Licitación Privada, Concurso de Precios y Compra Directa.
* Para Presupuesto puede ser opcional.
* El monto debe ser mayor que cero.
* Una Cotización en estado `Aceptada` puede originar una única Obra.
* Una Cotización `Presentada` o `Rechazada` no puede originar una Obra.
* Una misma Cotización nunca puede generar más de una Obra.
* La creación de la Obra no es automática.
* El título de la Cotización se utiliza como título inicial de la Obra.
* El Cliente asociado a la Cotización determina el Cliente correspondiente a la Obra que posteriormente se origine en ella.
* Una Cotización puede modificarse mientras no tenga una Obra asociada.
* Una vez que haya originado una Obra, queda bloqueada para edición y no puede eliminarse.
* Los campos de texto deberán respetar las reglas generales de normalización y validación definidas en la sección 41.

---

## 12. Entidad Obra

Representa un proyecto contratado que se origina en una Cotización aceptada.

Constituye el núcleo operativo del sistema y vincula la etapa comercial con ejecución, facturación y cobro.

### Creación de una Obra

La creación de una Obra será **manual y controlada por el usuario**.

Al crear una Obra, el selector de Cotización debe mostrar únicamente Cotizaciones que:

* estén en estado `Aceptada`;
* todavía no tengan una Obra asociada.

La Cotización seleccionada determina el Cliente correspondiente a la Obra.

El Cliente no debe seleccionarse ni almacenarse nuevamente en `Obra`.

La Obra conserva la referencia a la Cotización que le dio origen.

### Campos

`id_obra`

* SERIAL
* PRIMARY KEY.

`codigo_obra`

* VARCHAR(20)
* UNIQUE
* NOT NULL.
* generado automáticamente.
* formato previsto: `OBR-YYYY-NNN`.

`id_cotizacion`

* INTEGER
* FOREIGN KEY → Cotización
* UNIQUE
* NOT NULL.

`titulo`

* TEXT
* NOT NULL.

`fecha_inicio`

* DATE
* opcional/condicional.

`fecha_estimada_fin`

* DATE
* opcional.

`fecha_fin`

* DATE
* opcional/condicional.

`monto_contratado`

* NUMERIC(12,2)
* NOT NULL.

`estado_ejecucion`

* VARCHAR(20)
* NOT NULL.

`tipo_documento`

* VARCHAR(30)
* opcional.

`numero_documento`

* TEXT
* opcional.

`fecha_documento`

* DATE
* opcional.

`motivo_estado`

* TEXT
* condicional.

### Estados de ejecución permitidos

* Pendiente.
* En ejecución.
* Finalizada.
* Suspendida.
* Cancelada.

No implementar una tabla independiente de estados.

No implementar historial de estados durante el alcance actual.

### Reglas

* Toda Obra debe originarse en una Cotización `Aceptada`.
* Cada Cotización puede originar como máximo una Obra.
* El Cliente correspondiente a la Obra se obtiene mediante la Cotización seleccionada.
* `Obra` no almacena `id_cliente`.
* El título se copia inicialmente desde la Cotización.
* El título de la Obra puede modificarse posteriormente según las reglas de edición establecidas.
* El código de Obra es único y automático.
* El monto contratado se ingresa manualmente.
* El monto contratado puede diferir del monto ofertado.
* El monto contratado debe ser mayor que cero.

### Reglas de estado de ejecución

#### Pendiente

* Es el estado inicial.
* No debe tener `fecha_inicio`.
* No debe tener `fecha_fin`.
* `fecha_inicio` se registrará cuando la Obra pase a un estado que la requiera, como `En ejecución`.

#### En ejecución

* Requiere `fecha_inicio`.
* No requiere `fecha_fin`.

#### Finalizada

* Requiere `fecha_inicio`.
* Requiere `fecha_fin`.
* Si se informa `fecha_fin`, el estado debe ser `Finalizada`.
* La fecha de finalización no puede ser anterior a la fecha de inicio.

#### Suspendida

* Requiere `fecha_inicio`.
* Requiere `motivo_estado`.
* No requiere `fecha_fin`.

#### Cancelada

* Requiere `motivo_estado`.
* No requiere `fecha_fin`.

Las reglas generales para los cambios manuales de estado se encuentran definidas en las secciones 37 y 38.

### Documento contractual

El instrumento contractual de una Obra es opcional.

`tipo_documento` será un select con los siguientes valores:

* Contrato.
* Orden de compra.
* Pedido de compra.
* Resolución.
* Otros.

No se utilizará `Sin documento` como opción.

Cuando una contratación no posea instrumento contractual, los campos:

* `tipo_documento`;
* `numero_documento`;
* `fecha_documento`;

deberán permanecer vacíos y almacenarse como `NULL`.

Cuando exista un instrumento contractual, los tres campos deberán completarse.

Por lo tanto, `tipo_documento`, `numero_documento` y `fecha_documento` constituyen un conjunto coherente: o bien los tres permanecen vacíos, o bien los tres contienen información.

La opción `Otros` no requerirá inicialmente un campo adicional de descripción.

No se creará una entidad independiente para los tipos de documento contractual.

### Estado de facturación de la Obra

El estado de facturación de una Obra es **derivado**.

No debe almacenarse como columna adicional ni requiere una tabla independiente.

Se calcula comparando la suma de las Facturas asociadas a la Obra con `monto_contratado`.

Estados visuales:

* **Sin facturar:** no existen Facturas asociadas.
* **Facturada parcialmente:** la suma de las Facturas es mayor que cero y menor que el monto contratado.
* **Facturada totalmente:** la suma de las Facturas coincide con el monto contratado.

El total facturado nunca puede superar el monto contratado.

### Estado de cobro de la Obra

El estado global de cobro de una Obra también es **derivado**.

No debe almacenarse como columna adicional ni requiere una tabla independiente.

Se obtiene mediante:

**Obra → Facturas → Pagos**

y se compara el total efectivamente cobrado con `monto_contratado`.

Estados visuales:

* **Adeudada:** no existen Pagos asociados a las Facturas de la Obra.
* **Pagada parcialmente:** existen Pagos, pero su suma es menor que el monto contratado.
* **Pagada:** la suma de los Pagos coincide con el monto contratado.

Este estado representa el cobro global de la Obra y es independiente del estado individual de cada Factura.

### Relaciones

Cotización 1 → 0..1 Obra

Obra 1 → N Facturas

Existe además la relación conceptual:

Cliente 1 → N Obras

Esta relación es indirecta y se determina mediante:

**Cliente → Cotización → Obra**

---

## 13. Entidad Factura

Representa una factura emitida por la empresa asociada a una Obra.

Una Obra puede requerir múltiples Facturas por avances, certificaciones o etapas.

### Campos

`id_factura`

* SERIAL
* PRIMARY KEY.

`id_obra`

* INTEGER
* FOREIGN KEY → Obra
* NOT NULL.

`numero_factura`

* TEXT
* UNIQUE
* NOT NULL.

`fecha_emision`

* DATE
* NOT NULL.

`importe`

* NUMERIC(12,2)
* NOT NULL.

`observaciones`

* TEXT
* opcional.

### Estado individual de la Factura

El estado de pago de una Factura es **derivado**.

No debe ser editable manualmente.

Estados visuales:

* **Pendiente:** la Factura no tiene un Pago asociado.
* **Pagada:** existe su Pago asociado y el importe del Pago coincide con el importe de la Factura.

No es necesario almacenar redundantemente este estado si puede obtenerse de manera confiable mediante la relación Factura → Pago.

### Reglas

* Toda Factura pertenece a una Obra existente.
* Una Obra puede tener múltiples Facturas.
* Cada Factura pertenece exclusivamente a una Obra.
* El número de Factura debe ser único.
* El importe debe ser mayor que cero.
* La suma total de las Facturas de una Obra no puede superar el monto contratado.
* No se permiten pagos parciales de una Factura.
* Una Factura que ya posee un Pago no puede recibir otro.
* Una Factura puede modificarse mientras no tenga un Pago asociado.
* Una vez que tenga un Pago asociado, queda bloqueada para edición y no puede eliminarse mientras exista dicho Pago.
* Los campos de texto deberán respetar las reglas generales de normalización definidas en la sección 41.
* Cuando `observaciones` quede vacío después de su normalización, deberá almacenarse como `NULL`.

---

## 14. Entidad Pago

Representa el registro del pago recibido correspondiente a una Factura.

Dentro del alcance actual existe un único Pago por Factura.

No se implementan pagos parciales.

### Campos

`id_pago`

* SERIAL
* PRIMARY KEY.

`id_factura`

* INTEGER
* FOREIGN KEY → Factura
* UNIQUE
* NOT NULL.

`fecha_pago`

* DATE
* NOT NULL.

`importe`

* NUMERIC(12,2)
* NOT NULL.

`medio_pago`

* VARCHAR(30)
* NOT NULL.

`observaciones`

* TEXT
* opcional en general;
* obligatorio cuando `medio_pago` sea `Otros`.

### Medios de pago permitidos

`medio_pago` se seleccionará entre:

* Transferencia.
* Efectivo.
* Cheque.
* Echeq.
* Otros.

No se creará una tabla independiente para medios de pago.

### Reglas

* Todo Pago pertenece a una Factura existente.
* Cada Pago corresponde exclusivamente a una Factura.
* Una Factura puede tener como máximo un Pago.
* El importe debe ser mayor que cero.
* El importe debe coincidir exactamente con el importe total de la Factura.
* No se permiten pagos parciales.
* No se permiten múltiples Pagos para una Factura.
* El Pago se relaciona indirectamente con la Obra a través de la Factura.
* Los Pagos no se editan.
* Si un Pago fue registrado incorrectamente, debe eliminarse y registrarse nuevamente.
* Pago es la última entidad de la cadena y no posee entidades dependientes dentro del modelo actual.
* La eliminación de un Pago está permitida.
* Al eliminar un Pago no deben actualizarse manualmente estados almacenados; los estados y totales derivados deberán reflejar la nueva situación al volver a calcularse.
* Cuando `medio_pago` sea `Otros`, `observaciones` será obligatorio y no podrá quedar vacío ni contener únicamente espacios.
* Cuando `observaciones` sea opcional y quede vacío después de eliminar espacios al inicio y al final, deberá almacenarse como `NULL`.
* No se incorporará un campo `moneda` dentro del alcance actual.

---

## 15. Niveles de seguimiento económico

El sistema distingue dos niveles diferentes.

### Nivel Obra

Permite conocer el estado económico global respecto del monto contratado.

Se muestran de forma derivada:

**Facturación**

* Sin facturar.
* Facturada parcialmente.
* Facturada totalmente.

**Cobro**

* Adeudada.
* Pagada parcialmente.
* Pagada.

Estos valores se obtienen a partir de las relaciones:

Obra → Facturas → Pagos.

### Nivel Factura

Permite conocer el estado de pago de cada factura individual.

Estados derivados:

* Pendiente.
* Pagada.

Se obtiene a partir de:

Factura → Pago.

No confundir el estado individual de una factura con el estado global de cobro de una obra.

---

## 16. Relaciones generales

Cliente 1 → N Cotizaciones

Cotización 1 → 0..1 Obra

Obra 1 → N Facturas

Factura 1 → 0..1 Pago

Existe además la relación conceptual:

Cliente 1 → N Obras

Esta relación es indirecta y se determina mediante:

**Cliente → Cotización → Obra**

La tabla `Obra` no almacena `id_cliente`.

Por lo tanto, el Cliente correspondiente a una Obra se obtiene siempre mediante la Cotización que le dio origen:

**Obra → Cotización → Cliente**

De esta manera:

* toda Cotización pertenece obligatoriamente a un Cliente;
* toda Obra se origina obligatoriamente en una Cotización `Aceptada`;
* una Cotización puede originar como máximo una Obra;
* el Cliente correspondiente a una Obra queda determinado por el Cliente de su Cotización;
* una Obra puede tener múltiples Facturas;
* cada Factura pertenece exclusivamente a una Obra;
* una Factura puede tener como máximo un Pago;
* cada Pago pertenece exclusivamente a una Factura.

Estas cardinalidades representan el diseño aprobado.

No modificarlas sin una nueva decisión explícita.

---

## 17. Información manual, heredada, automática y derivada

### Cliente

Carga manual:

* CUIT/CUIL.
* Razón social.
* Responsable.
* Teléfono.
* Email.

Generado:

* ID.

### Cotización

Select:

* Cliente.
* Tipo de Cotización.
* Estado.

Carga manual:

* Número de contratación cuando corresponda.
* Título.
* Fecha.
* Monto.

Generado:

* ID.
* Código de Cotización.

### Obra

Select:

* Cotización `Aceptada` que todavía no tenga Obra.

Heredado inicialmente desde la Cotización:

* Título.

El título heredado constituye el valor inicial de la Obra y puede modificarse posteriormente según las reglas de edición definidas.

Derivado mediante la Cotización:

* Cliente.

El Cliente no se selecciona ni se almacena nuevamente en `Obra`.

Se obtiene mediante:

**Obra → Cotización → Cliente**

Carga manual:

* Monto contratado.
* Fechas cuando corresponda.
* Datos contractuales cuando existan.
* Estado de ejecución cuando corresponda.
* Motivo cuando corresponda.

Generado:

* ID.
* Código de Obra.

Derivado:

* Estado de facturación.
* Estado de cobro.

### Factura

Select:

* Obra.

Carga manual:

* Número de Factura.
* Fecha de emisión.
* Importe.
* Observaciones.

Generado:

* ID.

Derivado:

* Estado individual de pago.

### Pago

Select:

* Factura pendiente.
* Medio de pago.

Carga manual:

* Fecha de Pago.
* Importe.
* Observaciones cuando corresponda.

`observaciones` será obligatorio cuando el medio de pago seleccionado sea `Otros`.

Generado:

* ID.

Su existencia permite derivar:

* Estado individual de la Factura;
* total cobrado de la Obra;
* estado global de cobro de la Obra.

Los estados y totales derivados no deben almacenarse redundantemente cuando puedan obtenerse de manera confiable mediante las relaciones existentes.

---

## 18. Validaciones

Las reglas de negocio deben validarse principalmente en el backend.

El frontend debe repetir aquellas validaciones que mejoren la experiencia del usuario.

La base de datos debe proteger las restricciones estructurales que correspondan mediante:

* PRIMARY KEY;
* FOREIGN KEY;
* UNIQUE;
* NOT NULL;
* otras restricciones justificadas.

No confiar únicamente en el frontend para garantizar integridad.

---

## 19. API REST

Cada módulo tendrá endpoints REST para las operaciones CRUD que correspondan.

Módulos:

* clientes;
* cotizaciones;
* obras;
* facturas;
* pagos.

Las rutas Flask deben organizarse mediante Blueprints.

Los controladores deben concentrar la lógica y validaciones correspondientes.

Los modelos deben encargarse de la interacción con los datos según la arquitectura definida.

La definición exacta de URLs, métodos HTTP y códigos de respuesta deberá quedar documentada antes de implementar cada API si todavía no fue definida.

---

## 20. Vue Router

Vue Router administrará la navegación de la SPA.

Vistas principales previstas:

* `/clientes`
* `/cotizaciones`
* `/obras`
* `/facturas`
* `/pagos`

El Dashboard podrá utilizar `/` si finalmente se implementa.

La definición final de rutas podrá ajustarse durante el diseño del frontend sin modificar los módulos funcionales aprobados.

---

## 21. Pinia

Pinia administrará el estado compartido del frontend.

Se utilizarán stores cuando exista información que deba compartirse o gestionarse entre vistas y componentes.

Los datos permanentes seguirán teniendo PostgreSQL como fuente de verdad.

Pinia no sustituye la persistencia en la base de datos.

Evitar crear stores innecesarios si el estado no necesita ser compartido.

---

## 22. Axios

Axios será utilizado para centralizar la comunicación entre Vue y Flask.

Los servicios relacionados con la API se ubicarán en:

`src/services/`

Se prevén servicios por recurso:

* clienteService.js
* cotizacionService.js
* obraService.js
* facturaService.js
* pagoService.js

La configuración común de Axios debe evitar duplicación innecesaria.

---

## 23. Dependencias

Antes de incorporar una nueva dependencia:

1. explicar para qué se necesita;
2. comprobar si puede resolverse razonablemente con las herramientas existentes;
3. solicitar autorización.

Dependencias backend:

`requirements.txt`

Dependencias frontend:

`package.json`

No instalar librerías solamente por conveniencia si agregan complejidad innecesaria.

---

## 24. Variables de entorno

Las credenciales y configuraciones sensibles no deben escribirse directamente en el código.

El backend utilizará variables de entorno para configurar la conexión con PostgreSQL.

Las variables definidas para la conexión son:

* `DB_HOST`
* `DB_PORT`
* `DB_NAME`
* `DB_USER`
* `DB_PASSWORD`

Los valores reales correspondientes al entorno local deberán almacenarse en:

`.env`

El archivo `.env` no debe incorporarse al repositorio ni publicarse en Git.

Debe existir:

`.env.example`

para documentar las variables necesarias sin contener credenciales ni valores sensibles reales.

La aplicación deberá obtener la configuración de conexión a PostgreSQL a partir de estas variables y no deberá contener usuarios, contraseñas, nombres de base de datos ni configuraciones particulares de la computadora de desarrollo escritos directamente en el código.

Cualquier variable de entorno adicional que posteriormente resulte necesaria deberá responder a una necesidad concreta del proyecto y quedar documentada en `.env.example`.

---

## 25. Base de datos y datos de prueba

La base de datos será PostgreSQL.

El modelo debe implementarse respetando las relaciones, restricciones y reglas definidas en este documento.

Se incluirá:

`backend/database/seed.sql`

El seed deberá contener el conjunto mínimo de datos de prueba definido en la sección 51, suficiente para representar todos los estados funcionales relevantes del sistema.

La cantidad de registros no será uniforme entre las tablas.

La distribución definida será:

* 3 Clientes;
* 7 Cotizaciones;
* 5 Obras;
* 3 Facturas;
* 2 Pagos.

Los datos deben respetar:

* claves primarias;
* claves foráneas;
* restricciones;
* cardinalidades;
* reglas de negocio;
* estados permitidos;
* reglas de facturación y Pago;
* consistencia entre los montos relacionados.

La composición concreta y las relaciones entre los registros deberán respetar la estructura detallada definida en la sección 51.

El objetivo del seed es facilitar las pruebas, permitir visualizar todos los estados funcionales relevantes y reproducir un conjunto de datos coherente durante la presentación.

---

## 26. Interfaz

La interfaz debe ser:

* minimalista;
* clara;
* consistente;
* intuitiva;
* fácil de defender y explicar.

Debe contemplar:

* navegación clara;
* jerarquía tipográfica;
* formularios;
* validaciones;
* botones de acción;
* tablas o listados;
* mensajes de error;
* confirmaciones para acciones destructivas cuando corresponda.

La vista **Obras** debe permitir visualizar de manera clara:

* estado de ejecución;
* monto contratado;
* estado global de facturación;
* estado global de cobro.

La vista **Facturas** debe permitir visualizar claramente el estado individual de cada factura:

* Pendiente.
* Pagada.

No incorporar complejidad visual innecesaria.

---

## 27. Criterio académico

El sistema debe poder ser comprendido y defendido por la desarrolladora.

Por lo tanto:

* favorecer claridad sobre sofisticación;
* evitar código innecesariamente complejo;
* evitar abstracciones sin necesidad concreta;
* explicar decisiones técnicas relevantes;
* mantener separación clara entre frontend, backend y base de datos;
* demostrar MVC;
* demostrar API REST;
* demostrar Vue Router;
* demostrar Pinia;
* demostrar Axios;
* demostrar conexión y operaciones sobre PostgreSQL;
* utilizar Flask Blueprints para organizar las rutas.

Una solución más sofisticada no es automáticamente una solución mejor para este proyecto.

---

## 28. Evolución futura

El sistema podrá evolucionar posteriormente hacia una herramienta real.

Las decisiones actuales no deben bloquear innecesariamente esa posibilidad.

Sin embargo, esto no justifica implementar ahora funcionalidades fuera del alcance académico.

Las mejoras futuras deben permanecer claramente diferenciadas de los requisitos actuales.

---

## 29. Estado del diseño

Este documento representa las decisiones vigentes del proyecto.

Debe actualizarse cuando se aprueben cambios relacionados con:

* alcance;
* reglas de negocio;
* entidades;
* atributos;
* modelo relacional;
* relaciones;
* arquitectura;
* estructura de carpetas;
* tecnologías;
* dependencias;
* endpoints;
* validaciones;
* variables de entorno;
* interfaz;
* decisiones relevantes de implementación.

Una decisión no documentada no debe asumirse automáticamente como aprobada.

Si durante la implementación aparece una contradicción o una decisión no definida, debe consultarse antes de incorporarla al código.

## 30. Portabilidad, instalación y reproducción del proyecto

El proyecto debe poder instalarse y ejecutarse desde un clon limpio del repositorio tanto en Windows como en Linux, evitando dependencias de rutas absolutas o configuraciones específicas de la computadora de desarrollo.

La instalación y ejecución completa deberá estar documentada en `README.md`.

### Requisitos de portabilidad

* No utilizar rutas absolutas específicas de Windows o Linux dentro del código.
* Utilizar variables de entorno para configuraciones dependientes del entorno.
* Mantener las dependencias Python declaradas en `requirements.txt`.
* Mantener las dependencias frontend declaradas en `package.json`.
* Incluir `.env.example` con las variables necesarias, sin credenciales reales.
* Mantener `.env` fuera del repositorio.
* Documentar las versiones o requisitos mínimos relevantes de Python, Node.js, npm y PostgreSQL.
* Documentar comandos de instalación y ejecución para Windows y Linux cuando difieran.

### Reproducción de la base de datos

Una persona que clone el repositorio debe poder crear y preparar la base PostgreSQL siguiendo únicamente la documentación del proyecto.

El repositorio deberá incluir los scripts SQL necesarios para:

* crear la estructura de la base de datos;
* crear tablas, relaciones y restricciones;
* cargar datos iniciales/de prueba cuando corresponda.

Los scripts no deben depender de datos, usuarios, contraseñas o rutas particulares de la computadora de desarrollo.

### Objetivo de instalación

Partiendo de un clon limpio del repositorio y teniendo instalados los requisitos previos documentados, debe ser posible:

1. configurar las variables de entorno;
2. instalar las dependencias del backend;
3. crear y preparar la base de datos PostgreSQL;
4. cargar los datos de prueba;
5. iniciar Flask;
6. instalar las dependencias del frontend;
7. iniciar Vue/Vite;
8. acceder a la aplicación y utilizarla con los datos de prueba.

El `README.md` será la guía principal para reproducir este procedimiento.

## Acceso a PostgreSQL

Para el alcance actual se utilizará **SQL directo mediante `psycopg`**.

No se utilizará ORM.

La interacción entre Flask y PostgreSQL debe realizarse mediante consultas SQL explícitas desde la capa correspondiente del backend.

Esta decisión busca:

* mantener visible y comprensible la interacción con la base de datos;
* permitir demostrar consultas SQL, relaciones y operaciones CRUD;
* evitar incorporar una capa ORM que no es necesaria para los requisitos actuales;
* mantener una implementación sencilla y defendible académicamente.

La incorporación futura de un ORM queda fuera del alcance actual y requerirá una nueva decisión.

---

## 31. Ejecución de Frontend y Backend

Frontend y backend serán aplicaciones separadas.

Durante el desarrollo:

* Vue/Vite ejecutará el frontend;
* Flask ejecutará la API REST;
* Vue consumirá la API Flask mediante Axios;
* Flask accederá a PostgreSQL.

Flujo:

**Vue/Vite → Axios → Flask API REST → PostgreSQL**

Flask no servirá el frontend Vue durante el alcance actual.

Esta separación permite demostrar claramente:

* arquitectura cliente-servidor;
* API REST;
* consumo mediante Axios;
* separación entre frontend y backend.

---

## 32. Dependencias base del Backend

Las dependencias base previstas son:

* `Flask`: desarrollo del backend y API REST.
* `psycopg`: conexión y ejecución de consultas sobre PostgreSQL.
* `python-dotenv`: carga de variables de entorno durante el desarrollo local.
* `Flask-Cors`: permitir la comunicación entre Vue/Vite y Flask durante el desarrollo cuando se ejecuten desde orígenes diferentes.

No se utilizará SQLAlchemy ni otro ORM.

Toda dependencia adicional deberá justificarse y aprobarse antes de incorporarse.

Las dependencias efectivamente utilizadas deberán quedar declaradas en `requirements.txt`.

---

## 33. Configuración de conexión a PostgreSQL

La configuración de PostgreSQL utilizará variables de entorno separadas.

Variables previstas:

`DB_HOST`

`DB_PORT`

`DB_NAME`

`DB_USER`

`DB_PASSWORD`

Los valores reales estarán en `.env`.

`.env` no debe incorporarse al repositorio.

`.env.example` deberá documentar las variables necesarias sin contener credenciales reales.

No deben existir usuarios, contraseñas, nombres de base de datos ni configuraciones particulares de la computadora de desarrollo escritos directamente en el código.

---

## 34. Creación reproducible de la Base de Datos

La estructura principal prevista será:

`backend/database/schema.sql`

`backend/database/seed.sql`

### schema.sql

Debe contener lo necesario para reproducir la estructura del modelo:

* tablas;
* claves primarias;
* claves foráneas;
* restricciones de unicidad;
* restricciones `NOT NULL`;
* restricciones adicionales que hayan sido aprobadas.

### seed.sql

Debe contener los datos de prueba definidos para el proyecto respetando relaciones, restricciones y reglas de negocio.

No se incorporará inicialmente un sistema de migraciones.

El procedimiento para crear y preparar PostgreSQL desde un clon limpio deberá quedar documentado en `README.md`.

---

## 35. Política de eliminación e integridad referencial

Como criterio general, no se utilizará eliminación automática en cascada sobre las entidades principales del sistema.

La existencia de registros dependientes debe impedir la eliminación del registro del cual dependen.

Por lo tanto:

* un Cliente con Cotizaciones asociadas no puede eliminarse;
* una Cotización que haya originado una Obra no puede eliminarse;
* una Obra con Facturas asociadas no puede eliminarse;
* una Factura con un Pago asociado no puede eliminarse;
* un Pago puede eliminarse porque no posee una entidad posterior dependiente dentro del modelo actual.

### Eliminación de Cliente

Un Cliente puede eliminarse únicamente cuando no posea Cotizaciones asociadas.

Si el Cliente posee al menos una Cotización, su eliminación debe quedar bloqueada.

No es necesario comprobar adicionalmente si el Cliente posee Obras, ya que toda Obra se origina obligatoriamente en una Cotización y el Cliente de la Obra se determina mediante dicha Cotización.

Si se desea eliminar un Cliente que posee Cotizaciones, primero deberán eliminarse las Cotizaciones correspondientes respetando sus propias reglas de integridad.

Por lo tanto:

* una Cotización sin Obra asociada puede eliminarse;
* una Cotización que haya originado una Obra no puede eliminarse;
* mientras exista una Cotización asociada al Cliente, el Cliente no podrá eliminarse.

De esta manera, las dependencias posteriores quedan protegidas progresivamente por las reglas de cada entidad:

**Cliente → Cotización → Obra → Factura → Pago**

No se incorporará un mecanismo de baja lógica mediante un campo `activo` o `inactivo` para Cliente dentro del alcance actual.

La incorporación futura de una baja lógica podrá evaluarse si aparece una necesidad concreta que la justifique.

Cuando una eliminación esté impedida por relaciones existentes, el backend debe devolver un error comprensible indicando el motivo.

Cuando un registro no tenga dependencias que impidan su eliminación, podrá eliminarse.

No utilizar `ON DELETE CASCADE` para resolver automáticamente estas relaciones.

### Efecto de eliminar un Pago

El estado individual de una Factura es derivado.

Por lo tanto, si se elimina su Pago:

* no debe actualizarse manualmente una columna de estado;
* la Factura volverá a resultar `Pendiente` al calcular su estado;
* los totales y el estado global de cobro de la Obra también deberán reflejar automáticamente la nueva situación al volver a calcularse.

Este comportamiento es consecuencia del principio general de utilizar datos derivados y no información redundante.


## 36. Reglas de modificación después de crear entidades dependientes

Las entidades podrán modificarse mientras no existan entidades dependientes que requieran preservar la consistencia de la información registrada.

### Cotización

Una Cotización podrá modificarse mientras no tenga una Obra asociada.

Una vez que una Cotización haya originado una Obra:

* la Cotización quedará bloqueada para edición;
* no podrá modificarse el Cliente;
* no podrá modificarse el tipo de Cotización;
* no podrá modificarse el número de contratación;
* no podrá modificarse el título;
* no podrá modificarse la fecha;
* no podrá modificarse el monto;
* no podrá modificarse el estado;
* no podrá eliminarse mientras exista la Obra asociada.

### Obra

Una Obra podrá modificarse normalmente mientras no tenga Facturas asociadas, respetando las demás reglas de negocio y validaciones definidas para la entidad.

Una vez que la Obra tenga al menos una Factura asociada, sus datos generales quedarán bloqueados para edición.

No podrán modificarse:

* la Cotización de origen;
* el título;
* el monto contratado;
* la fecha estimada de finalización;
* los datos del documento contractual.

El seguimiento de la ejecución de la Obra continuará habilitado aun cuando existan Facturas asociadas.

Por lo tanto, podrá modificarse:

* el estado de ejecución;
* `fecha_inicio`, cuando sea necesaria para mantener la coherencia con el estado;
* `fecha_fin`, cuando sea necesaria para mantener la coherencia con el estado;
* `motivo_estado`, cuando sea necesario para mantener la coherencia con el estado.

Estos campos solo podrán modificarse cuando corresponda al seguimiento de la ejecución y deberán respetar las reglas de estado establecidas para la Obra.

La existencia de Facturas no impide que la Obra continúe cambiando de estado.

### Factura

Una Factura podrá modificarse mientras no tenga un Pago asociado.

Una vez que exista un Pago:

* la Factura quedará bloqueada para edición;
* no podrá modificarse la Obra asociada;
* no podrá modificarse el número de Factura;
* no podrá modificarse la fecha de emisión;
* no podrá modificarse el importe;
* no podrá modificarse las observaciones;
* no podrá eliminarse mientras exista el Pago asociado.

### Pago

Los Pagos no se editarán.

Si un Pago fue registrado incorrectamente, deberá eliminarse y registrarse nuevamente.

La eliminación de un Pago estará permitida porque Pago es la última entidad de la cadena y no posee entidades dependientes dentro del modelo actual.

Al eliminar un Pago, los estados y totales derivados deberán reflejar automáticamente la nueva situación al volver a calcularse.

---

## 37. Reglas de estado de ejecución de la Obra

Los estados de ejecución permitidos continúan siendo:

* `Pendiente`
* `En ejecución`
* `Finalizada`
* `Suspendida`
* `Cancelada`

Los cambios de estado pueden realizarse manualmente, respetando las validaciones correspondientes a cada estado.

### Pendiente

Es el estado inicial de una Obra.

Una Obra en estado `Pendiente` no debe tener `fecha_inicio` ni `fecha_fin`.

`fecha_inicio` representa el inicio efectivo de la Obra y deberá registrarse cuando esta pase a un estado que la requiera.

No se permitirá guardar una Obra en estado `Pendiente` con `fecha_inicio` o `fecha_fin` informadas.

### En ejecución

Una Obra en estado `En ejecución` debe tener obligatoriamente `fecha_inicio`.

No se permitirá guardar el estado `En ejecución` sin fecha de inicio.

### Finalizada

Existe una relación obligatoria entre el estado `Finalizada` y `fecha_fin`.

Se deben cumplir ambas reglas:

* si se selecciona el estado `Finalizada`, `fecha_fin` es obligatoria;
* si se ingresa `fecha_fin`, el estado debe ser `Finalizada`.

Si alguna de estas condiciones no se cumple, el sistema debe informar el motivo y no permitir crear o guardar el registro.

### Suspendida

Una Obra en estado `Suspendida`:

* debe tener `fecha_inicio`;
* debe tener un motivo obligatorio;
* no requiere `fecha_fin`.

Mientras permanezca suspendida puede mantenerse sin fecha de finalización.

### Cancelada

Cuando se seleccione el estado `Cancelada`, el campo destinado al motivo debe habilitarse y ser obligatorio.

No se permitirá guardar una Obra como `Cancelada` sin indicar el motivo.

---

## 38. Cambios manuales de estado

Los estados de ejecución no son irreversibles.

El usuario puede cambiar manualmente una Obra de un estado a otro, incluyendo cambios desde `Suspendida`, `Cancelada` o `Finalizada`.

El nuevo estado siempre debe cumplir las validaciones que le correspondan.

Antes de guardar un cambio de estado, la interfaz debe solicitar confirmación explícita al usuario.

Ejemplo de mensaje:

`¿Confirma que desea cambiar el estado de la obra?`

La finalidad de esta confirmación es evitar cambios accidentales sin incorporar un historial de estados, que permanece fuera del alcance actual.

---

## 39. Cobro total de la Obra

El estado global de cobro de la Obra es un dato derivado y se determinará a partir de la suma de los Pagos asociados a sus Facturas.

Cuando la suma total de los Pagos asociados a las Facturas de una Obra alcance exactamente el `monto_contratado`:

* el estado global de cobro derivado será `Pagada`;
* el Pago que complete el cobro total se registrará normalmente si cumple todas las reglas de validación correspondientes;
* el cobro total no modificará automáticamente el estado de ejecución de la Obra ni su `fecha_fin`.

El estado de ejecución y el estado de cobro representan conceptos diferentes. Una Obra puede encontrarse totalmente cobrada sin que necesariamente haya finalizado su ejecución.

Por lo tanto, si después de registrar un Pago la Obra queda totalmente cobrada y su estado de ejecución todavía no es `Finalizada`, el sistema deberá informar esta situación mediante una advertencia al usuario.

Mensaje de referencia:

`Pago registrado correctamente. La obra se encuentra totalmente cobrada. Si la obra ya finalizó, recuerde cambiar su estado a Finalizada e indicar la fecha de finalización.`

Esta advertencia no impedirá el registro del Pago ni obligará a finalizar la Obra.

Cuando corresponda finalizar efectivamente la Obra, el usuario deberá modificar manualmente su estado respetando las reglas definidas para `Finalizada`, incluyendo la obligatoriedad de `fecha_fin`.

Una Obra también puede ser finalizada antes de encontrarse totalmente cobrada.

Por lo tanto:

* una Obra puede estar `Finalizada` y continuar `Adeudada` o `Pagada parcialmente`;
* una Obra puede estar `Pagada` y continuar en un estado de ejecución distinto de `Finalizada`;
* los estados de ejecución y de cobro deberán mantenerse independientes y reflejar la situación real de cada dimensión.

---

## 40. Validación básica de fechas de Obra

Las validaciones cronológicas se mantendrán simples dentro del alcance actual.

Cuando corresponda comparar las fechas de una Obra:

* una fecha de finalización no puede ser anterior a la fecha de inicio.

No se incorporarán inicialmente otras validaciones cronológicas que no respondan a una regla de negocio necesaria.

## 41. Consistencia y validaciones del modelo de datos

Esta sección consolida reglas destinadas a mantener la consistencia del modelo de datos y establecer validaciones básicas para los datos ingresados.

Como criterio general, las validaciones deben ser simples, concretas y suficientes para el alcance actual del sistema, evitando incorporar complejidad que no responda a una necesidad funcional definida.

Las reglas deberán implementarse principalmente en el backend mediante Flask. PostgreSQL mantendrá las restricciones estructurales correspondientes y aquellas restricciones adicionales que se definan expresamente en esta sección.

---

### 41.1. Consistencia Cliente – Cotización – Obra

La relación entre Cliente, Cotización y Obra seguirá la cadena:

**Cliente → Cotización → Obra**

Toda Cotización pertenece obligatoriamente a un Cliente y toda Obra debe originarse obligatoriamente en una Cotización `Aceptada`.

Por lo tanto, la tabla `Obra` no almacenará directamente `id_cliente`.

El Cliente correspondiente a una Obra se determinará a través de la Cotización que le dio origen:

**Obra → Cotización → Cliente**

Cuando sea necesario consultar, mostrar o utilizar información del Cliente correspondiente a una Obra, deberá obtenerse mediante la relación con la Cotización.

Esta decisión evita almacenar redundantemente `id_cliente` en `Obra` y elimina la posibilidad de que una Obra quede asociada directamente a un Cliente diferente del Cliente correspondiente a su Cotización.

La relación conceptual entre Cliente y Obra continúa siendo válida:

* un Cliente puede tener múltiples Obras;
* toda Obra pertenece a un Cliente;
* la relación entre ambos se determina indirectamente mediante la Cotización de origen.

Al crear una Obra, el usuario seleccionará una Cotización válida según las reglas ya definidas.

La Cotización seleccionada determinará automáticamente el Cliente correspondiente a la Obra, por lo que el Cliente no deberá seleccionarse ni almacenarse nuevamente en `Obra`.

Este criterio mantiene el principio general del proyecto de evitar información redundante cuando pueda derivarse de manera confiable a partir de relaciones ya existentes.

---

### 41.2. Validación de montos

Los importes monetarios del sistema se manejarán con dos decimales.

Se utilizará `NUMERIC(12,2)` para los campos monetarios definidos en el modelo.

Como reglas básicas:

* `Cotización.monto` debe ser mayor que cero;
* `Obra.monto_contratado` debe ser mayor que cero;
* no se permitirán valores iguales o inferiores a cero para dichos campos.

No se incorporarán inicialmente reglas adicionales de monto mínimo comercial, precisión superior a dos decimales ni políticas especiales de redondeo.

Estas reglas serán validadas por el backend.

No se incorporará manejo de diferentes monedas dentro del alcance actual.

La incorporación de moneda, conversión entre monedas y tipos de cambio podrá evaluarse en una versión futura.

---

### 41.3. Documento contractual de la Obra

El instrumento contractual de una Obra es opcional.

Su finalidad es registrar el documento mediante el cual se instrumenta formalmente una contratación cuando dicho documento exista.

`tipo_documento` será un select con los siguientes valores:

* `Contrato`
* `Orden de compra`
* `Pedido de compra`
* `Resolución`
* `Otros`

No se utilizará `Sin documento` como opción.

Cuando una contratación no posea instrumento contractual, los campos:

* `tipo_documento`;
* `numero_documento`;
* `fecha_documento`;

deberán permanecer vacíos y almacenarse como `NULL`.

Cuando exista un instrumento contractual, los tres campos deberán completarse.

Por lo tanto, `tipo_documento`, `numero_documento` y `fecha_documento` se consideran un conjunto coherente: o bien no existe instrumento contractual y los tres permanecen vacíos, o bien existe y los tres contienen información.

La opción `Otros` no requerirá inicialmente un campo adicional de descripción.

No se creará una entidad independiente para los tipos de documento contractual.

---

### 41.4. Validación de CUIT/CUIL

El CUIT/CUIL constituye un dato especialmente relevante dentro del modelo porque identifica de manera única al Cliente, entidad a partir de la cual se originan las relaciones posteriores del sistema.

Se aplicarán tres niveles de protección.

#### Frontend

Se realizará una validación básica destinada a evitar el envío de datos evidentemente incorrectos.

#### Backend

Antes de validar y almacenar el CUIT/CUIL:

* se eliminarán espacios y guiones;
* el resultado deberá contener exactamente 11 dígitos;
* solo se admitirán caracteres numéricos.

El CUIT/CUIL se almacenará normalizado, sin espacios ni guiones.

No se implementará durante el alcance actual la validación matemática del dígito verificador.

La validación del dígito verificador podrá evaluarse como mejora futura.

#### PostgreSQL

El campo se definirá como:

`VARCHAR(11)`

y deberá contar con:

* `NOT NULL`;
* `UNIQUE`;
* una restricción `CHECK` que garantice que el valor almacenado contenga exactamente 11 dígitos numéricos.

De esta manera, la base de datos actuará como última barrera para impedir el almacenamiento de un CUIT/CUIL estructuralmente inválido.

---

### 41.5. Normalización general de campos de texto

Como criterio general, los campos de texto ingresados por el usuario deberán eliminar los espacios ubicados al inicio y al final antes de ser validados y almacenados.

Los espacios internos del contenido deberán conservarse.

Para campos opcionales:

* si después de quitar los espacios al inicio y al final el valor queda vacío, deberá almacenarse como `NULL`.

Para campos obligatorios:

* después de quitar los espacios al inicio y al final, el valor debe conservar contenido;
* no se permitirá guardar una cadena vacía o compuesta únicamente por espacios.

No se aplicarán transformaciones automáticas generales de mayúsculas, minúsculas, eliminación de acentos u otras modificaciones que puedan alterar el contenido ingresado por el usuario.

---

### 41.6. Validaciones básicas de Cliente

#### Razón social

`razon_social` es obligatoria.

Debe:

* eliminar espacios al inicio y al final;
* contener información después de dicha normalización;
* admitir letras, números, espacios y caracteres especiales.

No se establece un límite máximo como regla de negocio.

#### Responsable

`responsable` es opcional.

Debe:

* eliminar espacios al inicio y al final;
* almacenarse como `NULL` cuando quede vacío después de dicha normalización.

No se establecen restricciones adicionales de longitud o caracteres.

#### Teléfono

`telefono` es opcional.

Debe:

* eliminar espacios al inicio y al final;
* admitir únicamente caracteres numéricos;
* almacenarse como `NULL` cuando quede vacío.

No se establece una longitud mínima o máxima como regla de negocio.

#### Email

`email` es opcional.

Debe:

* eliminar espacios al inicio y al final;
* almacenarse como `NULL` cuando quede vacío;
* cuando se informe, respetar una validación básica equivalente al formato `usuario@dominio.extension`.

No se implementará una validación avanzada del formato de correo electrónico.

---

### 41.7. Títulos y numeraciones

#### Título de Cotización y Obra

El título es obligatorio.

Debe:

* eliminar espacios al inicio y al final;
* contener información después de dicha normalización;
* admitir texto libre, incluyendo letras, números, espacios y caracteres especiales.

No se establece un límite máximo como regla de negocio.

El título de la Cotización se utilizará como título inicial de la Obra y podrá modificarse posteriormente en la Obra según las reglas de edición ya definidas.

#### Numeraciones administrativas y comerciales

Los campos destinados a números de contratación, documentos y facturas deberán respetar la obligatoriedad establecida para cada entidad y situación.

Cuando corresponda informar uno de estos valores:

* deberán eliminarse los espacios al inicio y al final;
* no podrán quedar vacíos cuando sean obligatorios;
* podrán contener letras, números, guiones, barras y otros caracteres que formen parte de la numeración correspondiente;
* no se aplicarán transformaciones adicionales sobre su contenido.

No se establece un límite máximo de caracteres como regla de negocio.

---

### 41.8. Observaciones y motivos

Los campos de observaciones serán opcionales salvo cuando una regla específica determine su obligatoriedad.

Deberán eliminar los espacios al inicio y al final y, cuando queden vacíos después de dicha normalización, deberán almacenarse como `NULL`.

`motivo_estado` será condicional según las reglas de estado de la Obra ya definidas.

Cuando el estado correspondiente exija un motivo:

* deberá contener información;
* no podrá quedar vacío ni contener únicamente espacios.

No se establecen restricciones adicionales de longitud o caracteres para observaciones o motivos.

---

### 41.9. Tipos y longitudes de campos de texto

Los tipos y longitudes se definirán de manera concreta para evitar decisiones técnicas abiertas durante la implementación inicial.

Se utilizarán los siguientes criterios:

* `cuit_cuil`: `VARCHAR(11)`;
* `codigo_cotizacion`: `VARCHAR(20)`;
* `codigo_obra`: `VARCHAR(20)`;
* estados: `VARCHAR(20)`;
* tipos de Cotización: `VARCHAR(30)`;
* `tipo_documento`: `VARCHAR(30)`;
* `medio_pago`: `VARCHAR(30)`.

Se utilizará `TEXT` para los campos de texto libre para los cuales no se haya establecido una longitud máxima como regla de negocio, incluyendo:

* `razon_social`;
* `responsable`;
* `telefono`;
* `email`;
* títulos;
* `numero_contratacion`;
* `numero_documento`;
* `numero_factura`;
* observaciones;
* `motivo_estado`.

El uso de `TEXT` no elimina las reglas de obligatoriedad, formato o normalización correspondientes a cada campo.

Los tamaños establecidos constituyen los criterios concretos para la primera implementación.

Si durante una revisión posterior aparece una necesidad real de modificar alguno de ellos, podrá ajustarse en esa instancia.

No deberán dejarse parámetros genéricos como `VARCHAR(n)` para que sean determinados durante la implementación.

---

### 41.10. Medios de Pago

`medio_pago` será obligatorio.

Se implementará mediante un select con los siguientes valores:

* `Transferencia`
* `Efectivo`
* `Cheque`
* `Echeq`
* `Otros`

El campo utilizará:

`VARCHAR(30)`

No se creará una tabla independiente de medios de pago.

Cuando se seleccione `Otros`, el campo `observaciones` del Pago pasará a ser obligatorio.

En ese caso:

* deberá contener información;
* se eliminarán los espacios al inicio y al final;
* no podrá quedar vacío ni contener únicamente espacios.

`observaciones` utilizará `TEXT`.

No se incorporará un campo `moneda` en Pago dentro del alcance actual.

La gestión de diferentes monedas queda expresamente fuera de esta primera versión y podrá evaluarse como mejora futura, ya que su implementación correcta requeriría definir la moneda de los distintos importes y el tratamiento de pagos efectuados en una moneda diferente.

---

### 41.11. Política de restricciones `CHECK` en PostgreSQL

No se utilizarán restricciones `CHECK` de forma generalizada en esta primera versión.

Los estados, tipos, medios de pago, montos y demás reglas funcionales serán validados principalmente en Flask.

Aunque determinados valores provengan de selects en el frontend, el backend deberá continuar validándolos antes de realizar operaciones sobre la base de datos.

PostgreSQL continuará siendo responsable de las restricciones estructurales correspondientes, incluyendo:

* claves primarias;
* claves foráneas;
* `NOT NULL`;
* `UNIQUE`;
* demás restricciones estructurales expresamente definidas en el modelo.

Como excepción a la política general, `cuit_cuil` contará además con una restricción `CHECK` en PostgreSQL que garantice que el valor almacenado contenga exactamente 11 dígitos numéricos.

Esta protección adicional se justifica por la importancia del CUIT/CUIL como identificador único del Cliente y por la posición de Cliente como entidad de origen de las relaciones posteriores del sistema.

Para el resto de las validaciones funcionales, se considera suficiente en esta primera versión la validación realizada por Flask, evitando duplicar innecesariamente reglas entre backend y base de datos.

Si durante una revisión posterior se identifica una necesidad concreta de reforzar alguna regla directamente en PostgreSQL, podrán incorporarse restricciones adicionales en esa instancia.

## 42. Generación de códigos internos

Las Cotizaciones y Obras utilizarán códigos internos generados automáticamente por el sistema.

Los formatos serán:

* Cotización: `COT-YYYY-NNN`
* Obra: `OBR-YYYY-NNN`

### Año del código

`YYYY` corresponderá al año actual del sistema en el momento en que se crea el registro.

Dentro del alcance actual, el sistema está pensado para registrar Cotizaciones y Obras a partir de su puesta en funcionamiento, manteniendo el orden de carga sincronizado con la realidad operativa.

No se contempla inicialmente la carga histórica de Cotizaciones u Obras correspondientes a años anteriores.

La incorporación de registros históricos podrá evaluarse como mejora futura.

### Numeración incremental

`NNN` representa una numeración correlativa creciente e independiente para cada tipo de entidad.

La numeración no se reiniciará al cambiar de año.

Por lo tanto:

* Cotización y Obra mantienen numeraciones independientes;
* la numeración comienza en `001` para cada entidad;
* cada nuevo registro utiliza el número correspondiente a su identificador autogenerado;
* el año forma parte del código para identificar el año de creación del registro, pero no determina el reinicio de la numeración;
* al cambiar de año, la numeración continúa de forma correlativa.

Ejemplos:

* `COT-2026-001`
* `COT-2026-002`
* `OBR-2026-001`
* `OBR-2026-002`
* `COT-2027-003`
* `OBR-2027-003`

El correlativo utilizado en `codigo_cotizacion` se obtendrá a partir de `id_cotizacion`.

El correlativo utilizado en `codigo_obra` se obtendrá a partir de `id_obra`.

De esta manera, la numeración aprovechará los identificadores autogenerados por PostgreSQL y no requerirá mantener contadores adicionales ni calcular manualmente el siguiente número disponible.

### Cantidad de dígitos

La numeración se mostrará con un mínimo de tres dígitos.

Por lo tanto:

* `1` se representará como `001`;
* `25` se representará como `025`;
* `999` se representará como `999`.

No se establecerá un límite máximo de 999 registros.

Si la numeración supera dicho valor, continuará normalmente:

* `1000`;
* `1001`;
* y sucesivos.

Esto permite mantener el formato previsto sin introducir una limitación artificial sobre la cantidad de registros.

### Eliminación de registros y reutilización de códigos

Los números correspondientes a registros eliminados no se reutilizarán.

Como el correlativo del código se obtiene a partir del identificador autogenerado del registro, la eliminación de una Cotización u Obra no provocará que su número vuelva a utilizarse para un registro posterior.

Si un registro es eliminado, su número quedará como un salto dentro de la secuencia.

Por ejemplo, si existen:

* `OBR-2026-014`
* `OBR-2026-015`

y posteriormente se elimina `OBR-2026-015`, el siguiente registro podrá utilizar:

`OBR-2026-016`

y no volverá a utilizar `OBR-2026-015`.

Los saltos de numeración son válidos y pueden representar registros que existieron y posteriormente fueron eliminados.

No se implementará lógica destinada a buscar o reutilizar números faltantes.

### Unicidad

`codigo_cotizacion` y `codigo_obra` deberán mantener una restricción `UNIQUE` en PostgreSQL.

La generación del código será responsabilidad del backend utilizando el identificador autogenerado correspondiente y el año de creación del registro.

La base de datos deberá actuar como última garantía para impedir la existencia de códigos duplicados.

No será necesario incorporar tablas auxiliares, contadores propios ni mecanismos destinados a calcular el siguiente correlativo.

No se incorporará inicialmente un mecanismo adicional de alta concurrencia que agregue complejidad innecesaria para la escala prevista del proyecto.

Si en una futura utilización real el nivel de concurrencia justificara una estrategia más robusta para la generación de códigos, podrá mejorarse el mecanismo sin modificar el formato ni el significado de los códigos internos.

## 43. Creación, inicialización y reproducción de la base de datos

La creación de la base de datos PostgreSQL será un paso manual de instalación previo a la ejecución de los scripts del proyecto.

El proyecto no automatizará la ejecución de `CREATE DATABASE`.

El nombre de la base, usuario, contraseña, host y puerto podrán variar según el entorno donde se instale el sistema y se configurarán mediante las variables definidas en `.env`:

* `DB_HOST`
* `DB_PORT`
* `DB_NAME`
* `DB_USER`
* `DB_PASSWORD`

De esta manera, la aplicación no dependerá de nombres de base de datos, usuarios, contraseñas ni configuraciones particulares de la computadora de desarrollo.

### Responsabilidad de `schema.sql`

El archivo:

`backend/database/schema.sql`

será responsable de crear la estructura necesaria dentro de una base de datos PostgreSQL previamente creada.

Deberá contener la definición de:

* tablas;
* claves primarias;
* claves foráneas;
* restricciones `UNIQUE`;
* restricciones `NOT NULL`;
* tipos de datos;
* demás restricciones de base de datos aprobadas en este documento.

`schema.sql`:

* no creará la base de datos;
* no eliminará automáticamente la base de datos;
* no eliminará automáticamente tablas existentes;
* no eliminará registros existentes;
* no se ejecutará automáticamente al iniciar Flask.

Dentro del alcance actual, `schema.sql` está pensado principalmente para la instalación inicial del proyecto sobre una base de datos vacía.

Si se ejecuta sobre una base que ya contiene la estructura creada, no deberá intentar destruirla ni reconstruirla automáticamente.

Cualquier procedimiento destructivo de reinicio de la base deberá ser una acción explícita y separada y no formará parte del comportamiento normal de `schema.sql`.

### Responsabilidad de `seed.sql`

El archivo:

`backend/database/seed.sql`

será responsable exclusivamente de cargar los datos iniciales de prueba definidos para el proyecto.

`seed.sql`:

* no creará la base de datos;
* no creará las tablas;
* no eliminará registros existentes;
* no se ejecutará automáticamente al iniciar Flask;
* se ejecutará después de `schema.sql`;
* estará pensado para cargar los datos de prueba sobre la estructura previamente creada.

La ejecución de `seed.sql` será necesaria para reproducir el conjunto inicial de datos utilizado para pruebas y presentación, pero no será necesaria para el funcionamiento normal de una base destinada a recibir datos reales.

### IDs de los registros del seed

Los identificadores definidos como `SERIAL` no se asignarán manualmente dentro de `seed.sql`.

PostgreSQL será responsable de generar automáticamente las claves primarias de:

* Cliente;
* Cotización;
* Obra;
* Factura;
* Pago.

Esto permitirá que las secuencias asociadas a los identificadores permanezcan sincronizadas automáticamente y evitará la necesidad de reajustarlas después de ejecutar el seed.

Las relaciones entre los registros de prueba deberán establecerse utilizando valores únicos y conocidos que permitan identificar de forma confiable los registros relacionados.

### Códigos internos en los datos de prueba

Los códigos internos de Cotizaciones y Obras incluidos en `seed.sql` se definirán explícitamente como datos de prueba coherentes con las reglas establecidas en la sección 42.

`seed.sql` no deberá reproducir la lógica del backend utilizada para generar automáticamente nuevos códigos.

La generación automática definida en la sección 42 se aplicará a las altas realizadas por la aplicación.

### Datos de prueba

`seed.sql` deberá contener el conjunto mínimo de registros coherentes definido en la sección 51.

La cantidad de registros no será uniforme entre las tablas.

La distribución será:

* 3 Clientes;
* 7 Cotizaciones;
* 5 Obras;
* 3 Facturas;
* 2 Pagos.

Los registros deberán respetar las relaciones, restricciones, cardinalidades y reglas de negocio definidas en este documento.

La composición concreta de los datos deberá respetar la distribución de estados, relaciones y escenarios definida en la sección 51.

El objetivo será que el conjunto permita probar y demostrar todos los estados funcionales relevantes del sistema sin incorporar registros redundantes.

### Uso normal de la aplicación

Una vez realizada la instalación inicial, el uso habitual del sistema no requerirá volver a ejecutar `schema.sql` ni `seed.sql`.

El inicio normal de la aplicación consistirá en utilizar la base PostgreSQL ya configurada y levantar el backend Flask y el frontend Vue.

Reiniciar Flask, Vue o PostgreSQL no deberá recrear la estructura ni eliminar los datos existentes.

### Evolución futura

Dentro del alcance actual no se implementará un sistema de migraciones de base de datos.

Si el sistema evoluciona hacia un entorno productivo donde sea necesario modificar estructuras existentes conservando los datos almacenados, deberá incorporarse posteriormente una estrategia de migraciones.

La ausencia de migraciones en la versión actual no deberá resolverse mediante la eliminación automática de tablas o datos.

## 44. Contrato general de la API REST.
### 44.1. Endpoints y métodos HTTP

Los métodos HTTP disponibles para cada recurso deberán responder a las reglas de negocio definidas en este documento.

No se incorporarán operaciones únicamente para conseguir una simetría CRUD si contradicen las reglas de negocio de una entidad.

#### Cliente

| Acción | Método | Endpoint |
| --- | --- | --- |
| Listar Clientes | `GET` | `/api/clientes` |
| Obtener un Cliente | `GET` | `/api/clientes/{id_cliente}` |
| Crear Cliente | `POST` | `/api/clientes` |
| Modificar Cliente | `PUT` | `/api/clientes/{id_cliente}` |
| Eliminar Cliente | `DELETE` | `/api/clientes/{id_cliente}` |

La modificación y eliminación deberán respetar las reglas de bloqueo y relaciones establecidas para Cliente.

#### Cotización

| Acción | Método | Endpoint |
| --- | --- | --- |
| Listar Cotizaciones | `GET` | `/api/cotizaciones` |
| Obtener una Cotización | `GET` | `/api/cotizaciones/{id_cotizacion}` |
| Crear Cotización | `POST` | `/api/cotizaciones` |
| Modificar Cotización | `PUT` | `/api/cotizaciones/{id_cotizacion}` |
| Eliminar Cotización | `DELETE` | `/api/cotizaciones/{id_cotizacion}` |

Una Cotización podrá modificarse o eliminarse únicamente mientras las reglas de negocio lo permitan.

Una vez que haya originado una Obra, deberá respetarse el bloqueo definido para la entidad.

#### Obra

| Acción | Método | Endpoint |
| --- | --- | --- |
| Listar Obras | `GET` | `/api/obras` |
| Obtener una Obra | `GET` | `/api/obras/{id_obra}` |
| Crear Obra | `POST` | `/api/obras` |
| Modificar generalmente una Obra | `PUT` | `/api/obras/{id_obra}` |
| Modificar parcialmente el seguimiento de una Obra | `PATCH` | `/api/obras/{id_obra}` |
| Eliminar Obra | `DELETE` | `/api/obras/{id_obra}` |

`PUT` se utilizará para la edición general de una Obra mientras sus reglas de negocio permitan dicha modificación.

`PATCH` se utilizará para las actualizaciones parciales relacionadas con el seguimiento de ejecución de la Obra.

Cuando una Obra tenga al menos una Factura asociada, sus datos generales permanecerán bloqueados, pero podrá utilizarse `PATCH` para modificar:

* el estado de ejecución;
* `fecha_inicio`, cuando sea necesaria para mantener la coherencia con el estado;
* `fecha_fin`, cuando sea necesaria para mantener la coherencia con el estado;
* `motivo_estado`, cuando sea necesario para mantener la coherencia con el estado.

La operación deberá respetar en todos los casos las reglas de cambio de estado definidas para Obra.

#### Factura

| Acción | Método | Endpoint |
| --- | --- | --- |
| Listar Facturas | `GET` | `/api/facturas` |
| Obtener una Factura | `GET` | `/api/facturas/{id_factura}` |
| Crear Factura | `POST` | `/api/facturas` |
| Modificar Factura | `PUT` | `/api/facturas/{id_factura}` |
| Eliminar Factura | `DELETE` | `/api/facturas/{id_factura}` |

Una Factura podrá modificarse mientras no tenga un Pago asociado.

Una vez que exista un Pago, deberán respetarse las reglas de bloqueo definidas para Factura.

#### Pago

| Acción | Método | Endpoint |
| --- | --- | --- |
| Listar Pagos | `GET` | `/api/pagos` |
| Obtener un Pago | `GET` | `/api/pagos/{id_pago}` |
| Crear Pago | `POST` | `/api/pagos` |
| Eliminar Pago | `DELETE` | `/api/pagos/{id_pago}` |

Pago no tendrá endpoints `PUT` ni `PATCH`.

Los Pagos no son editables según las reglas de negocio vigentes. Si un Pago fue registrado incorrectamente, deberá eliminarse y registrarse nuevamente.

### 44.2. Uso de PUT y PATCH

`PUT` será el método utilizado para la edición general de los recursos que admitan modificación.

Dentro del alcance actual utilizarán `PUT`:

* Cliente;
* Cotización;
* Obra;
* Factura.

Cada operación deberá respetar las reglas de edición y bloqueo correspondientes a la entidad.

`PATCH` se utilizará únicamente cuando exista una necesidad funcional concreta de realizar una actualización parcial.

Dentro del alcance actual se utilizará `PATCH` en Obra para modificar el seguimiento de ejecución sin habilitar la edición general de los demás datos.

Cuando una Obra tenga Facturas asociadas, `PATCH` permitirá modificar únicamente:

* el estado de ejecución;
* `fecha_inicio`, cuando sea necesaria para mantener la coherencia con el estado;
* `fecha_fin`, cuando sea necesaria para mantener la coherencia con el estado;
* `motivo_estado`, cuando sea necesario para mantener la coherencia con el estado.

Pago no utilizará `PUT` ni `PATCH`, ya que no admite edición. Si un Pago fue registrado incorrectamente, deberá eliminarse y registrarse nuevamente.

No se implementará `PATCH` de forma generalizada en recursos que no lo necesiten.

### 44.3. Códigos de estado HTTP

La API utilizará los siguientes códigos HTTP de manera consistente:

| Código | Nombre | Métodos donde puede aparecer | Criterio de uso | Ejemplos en el sistema |
| --- | --- | --- | --- | --- |
| **200** | `OK` | `GET`, `PUT`, `PATCH`, `DELETE` | La operación solicitada se realizó correctamente. | Listar Clientes, obtener una Obra, modificar una Cotización, cambiar el estado de una Obra, eliminar un Pago. |
| **201** | `Created` | `POST` | Se creó correctamente un nuevo recurso. | Crear Cliente, Cotización, Obra, Factura o Pago. |
| **400** | `Bad Request` | `POST`, `PUT`, `PATCH` | Los datos enviados son inválidos, incompletos o no cumplen las validaciones de entrada. | CUIT/CUIL con formato incorrecto, monto menor o igual a cero, campo obligatorio faltante, estado no permitido o fechas incoherentes. |
| **404** | `Not Found` | `GET`, `POST`, `PUT`, `PATCH`, `DELETE` | No existe un recurso necesario para realizar la operación. | ID solicitado inexistente, crear una Factura indicando una Obra inexistente o crear un Pago para una Factura inexistente. |
| **409** | `Conflict` | `POST`, `PUT`, `PATCH`, `DELETE` | Los datos pueden ser válidos, pero la operación entra en conflicto con una regla de negocio, una relación existente o el estado actual del recurso. | CUIT/CUIL duplicado, segundo Pago para una Factura, segunda Obra para una Cotización, eliminar Cliente con Cotizaciones, modificar Cotización con Obra o eliminar Factura con Pago. |
| **500** | `Internal Server Error` | Cualquiera | Se produjo un error interno inesperado que no corresponde a un error del usuario ni a una regla de negocio prevista. | Error inesperado de PostgreSQL, excepción no controlada de Flask o fallo interno del servidor. |

Las eliminaciones exitosas utilizarán `200 OK` y devolverán un mensaje de confirmación.

No se utilizará `204 No Content` dentro de la convención actual.

### 44.4. Estructura de respuestas y mensajes

La API utilizará una estructura uniforme para las respuestas.

Las consultas exitosas no generarán mensajes visibles de confirmación para el usuario.

Las altas, modificaciones y eliminaciones exitosas mostrarán una confirmación.

Los errores previstos mostrarán una explicación clara de la causa.

Los errores internos inesperados mostrarán un mensaje genérico y no expondrán detalles técnicos al usuario.

| Situación | HTTP | Respuesta API | ¿Mostrar al usuario? | Qué mostrar |
| --- | --- | --- | --- | --- |
| Listar registros correctamente | `200` | `data` | No | Nada. Vue muestra los datos obtenidos. |
| Obtener un registro correctamente | `200` | `data` | No | Nada. Vue muestra los datos en la vista o formulario correspondiente. |
| Crear correctamente | `201` | `message` + `data` | Sí | `"Cliente creado correctamente"`, `"Obra creada correctamente"`, etc. |
| Crear correctamente con advertencia funcional | `201` | `message` + `data` | Sí | El `message` incluirá la confirmación de la operación y la advertencia correspondiente. |
| Modificar correctamente | `200` | `message` + `data` | Sí | `"Cliente modificado correctamente"`, `"Obra modificada correctamente"`, etc. |
| Eliminar correctamente | `200` | `message` | Sí | `"Cliente eliminado correctamente"`, `"Pago eliminado correctamente"`, etc. |
| Datos inválidos | `400` | `error` | Sí | Motivo concreto, por ejemplo: `"El CUIT/CUIL debe contener exactamente 11 dígitos."` |
| Recurso no encontrado | `404` | `error` | Sí | `"Cliente no encontrado"`, `"Factura no encontrada"`, etc. |
| Regla de negocio impide la operación | `409` | `error` | Sí | Motivo concreto, por ejemplo: `"La factura no puede eliminarse porque tiene un pago asociado."` |
| Error interno inesperado | `500` | `error` | Sí, pero genérico | `"Ocurrió un error interno. Intente nuevamente."` |

#### Consultas exitosas

Las consultas devolverán:

`{"data": ...}`

Para listados, `data` contendrá una colección.

Para consultas individuales, `data` contendrá el objeto solicitado.

#### Creaciones y modificaciones exitosas

Las altas y modificaciones exitosas devolverán:

`{"message": "...", "data": ...}`

`data` contendrá el recurso resultante después de la operación.

Esta misma estructura se utilizará para los `PATCH` exitosos de Obra.

Cuando una creación sea exitosa pero deba comunicar además una advertencia funcional al usuario, se mantendrá la misma estructura:

`{"message": "...", "data": ...}`

No se agregará un campo adicional como `warning`.

En estos casos, `message` contendrá el texto completo que deba mostrarse al usuario, incluyendo tanto la confirmación de la operación exitosa como la advertencia correspondiente.

`data` continuará conteniendo el recurso creado normalmente.

Una advertencia funcional posterior a una operación exitosa no modificará el código HTTP de éxito ni convertirá la operación en un error.

Dentro del alcance actual, este criterio se aplicará al alta de un Pago que complete el cobro total de una Obra cuyo estado de ejecución todavía no sea `Finalizada`.

#### Eliminaciones exitosas

Las eliminaciones devolverán:

`{"message": "..."}`

#### Errores

Los errores previstos e internos utilizarán:

`{"error": "..."}`

Los errores `400`, `404` y `409` deberán proporcionar mensajes comprensibles que expliquen la causa concreta.

Los errores `500` no deberán devolver al frontend:

* trazas de ejecución;
* consultas SQL;
* credenciales;
* información de conexión;
* mensajes internos de PostgreSQL;
* detalles técnicos innecesarios.

### 44.5. Convenciones de representación JSON

Los datos intercambiados entre Vue y Flask deberán respetar las siguientes convenciones:

| Tema | Convención | Criterio |
| --- | --- | --- |
| **Nombres de campos** | `snake_case` | Mantener los mismos nombres utilizados en backend y base de datos, por ejemplo `id_cliente`, `fecha_inicio` y `monto_contratado`. |
| **Campos opcionales sin valor** | `null` | Si un campo existe pero no tiene valor, la API devuelve `null`; no `""`, `"null"` ni una omisión arbitraria. |
| **Texto opcional** | `null` cuando no exista valor | Campos como `telefono`, `observaciones` o `numero_contratacion` podrán devolverse como `null`. |
| **Fechas** | `"YYYY-MM-DD"` | La API utilizará este formato, consistente con `DATE` de PostgreSQL. La interfaz mostrará las fechas al usuario en formato argentino `DD/MM/AAAA`. |
| **NUMERIC(12,2)** | Número JSON | Los importes se devolverán como números JSON. La API no incluirá símbolos monetarios ni separadores de miles y no se exigirá conservar visualmente ceros decimales finales. La presentación con exactamente dos decimales será responsabilidad del frontend. |
| **IDs** | Número entero | Por ejemplo `"id_cliente": 5`, no `"5"`. |
| **Estados y valores de select** | Texto | Por ejemplo `"estado": "Aceptada"` para Cotización, `"estado_ejecucion": "En ejecución"` para Obra o `"medio_pago": "Transferencia"` para Pago. |
| **Booleanos, si se utilizan** | `true` / `false` | No deberán representarse como `"true"` o `"false"` en texto. |
| **Colecciones** | Array JSON | Cuando una consulta de colección no encuentre registros, deberá devolver `[]`, no `null`. |
| **Objeto individual inexistente** | Error `404` | No se devolverá `data: null` como una consulta exitosa. Corresponde responder `404` con `error`. |

La representación utilizada por la API deberá mantenerse separada del formato visual utilizado por Vue.

Los importes serán tratados por la API como valores numéricos. El frontend será responsable de aplicar la representación visual correspondiente, incluyendo la visualización con dos decimales.

### 44.6. Filtros y parámetros de consulta

Los listados podrán admitir parámetros de consulta (`query parameters`) cuando exista una necesidad funcional concreta de filtrado.

No se crearán endpoints específicos cuando la necesidad pueda resolverse de forma clara mediante filtros sobre el recurso existente.

Dentro del alcance actual se implementarán los siguientes parámetros:

| Recurso | Parámetro | Tipo | Significado |
| --- | --- | --- | --- |
| Cotizaciones | `estado` | texto | Devuelve únicamente Cotizaciones que tengan el estado indicado. |
| Cotizaciones | `sin_obra` | booleano | Cuando sea `true`, devuelve únicamente Cotizaciones que no tengan una Obra asociada. |
| Obras | `estado_ejecucion` | texto | Devuelve únicamente Obras que tengan el estado de ejecución indicado. |
| Obras | `con_saldo_por_facturar` | booleano | Cuando sea `true`, devuelve únicamente Obras cuyo total facturado sea menor que `monto_contratado`. |
| Facturas | `sin_pago` | booleano | Cuando sea `true`, devuelve únicamente Facturas que no tengan un Pago asociado. |

Los parámetros podrán combinarse cuando sea necesario.

#### Selector de Cotización para crear una Obra

Para obtener las Cotizaciones que pueden originar una nueva Obra se utilizará:

`GET /api/cotizaciones?estado=Aceptada&sin_obra=true`

Esto devolverá únicamente Cotizaciones:

* en estado `Aceptada`;
* sin una Obra asociada.

#### Selector de Obra para crear una Factura

Para obtener las Obras disponibles para registrar una nueva Factura se utilizará:

`GET /api/obras?con_saldo_por_facturar=true`

Esto devolverá únicamente Obras cuyo total facturado sea menor que su `monto_contratado`.

La disponibilidad de una Obra para este selector será, por lo tanto, un dato derivado de sus Facturas existentes y de su `monto_contratado`.

El backend será responsable de realizar este cálculo y devolver únicamente las Obras que todavía admitan facturación.

#### Selector de Factura para crear un Pago

Para obtener las Facturas disponibles para registrar un Pago se utilizará:

`GET /api/facturas?sin_pago=true`

Esto devolverá únicamente Facturas que todavía no tengan un Pago asociado.

#### Filtros derivados

`sin_obra`, `con_saldo_por_facturar` y `sin_pago` son parámetros de consulta de la API.

No son campos de las tablas y no deberán almacenarse en PostgreSQL.

`sin_obra=true` se determinará comprobando la ausencia de una Obra relacionada con la Cotización.

`con_saldo_por_facturar=true` se determinará comprobando que el total facturado de la Obra sea menor que su `monto_contratado`.

`sin_pago=true` se determinará comprobando la ausencia de un Pago relacionado con la Factura.

El backend será responsable de traducir estos parámetros a las consultas SQL correspondientes.

Dentro del alcance actual solo será necesario admitir:

* `sin_obra=true`;
* `con_saldo_por_facturar=true`;
* `sin_pago=true`.

No será necesario implementar inicialmente sus variantes `false`.

#### Alcance de los filtros

No se implementará inicialmente un sistema genérico de filtrado para cualquier campo.

Tampoco se incorporarán, salvo que posteriormente surja una necesidad concreta:

* paginación;
* búsqueda textual genérica;
* ordenamiento configurable;
* filtros arbitrarios por cualquier columna.

Los filtros de la API deberán responder a necesidades reales de la interfaz y de las reglas de negocio, evitando agregar complejidad innecesaria.

## 45. Transacciones y atomicidad de operaciones críticas

Las operaciones que dependan de consultar el estado actual de los datos antes de insertar, modificar o eliminar deberán ejecutarse dentro de una misma transacción cuando exista riesgo de inconsistencia entre la validación y la escritura.

El objetivo es garantizar que una operación crítica se complete de forma íntegra o no produzca ningún cambio parcial.

### 45.1. Criterio general

Cuando una operación requiera:

* consultar datos relacionados;
* calcular totales;
* comprobar reglas de negocio;
* y posteriormente realizar una escritura;

la validación y la escritura deberán formar parte de una misma operación transaccional cuando una modificación concurrente pueda afectar el resultado.

Cuando la regla de negocio dependa de información asociada a un registro que pueda ser afectada simultáneamente por otra operación, se utilizará un bloqueo de fila de PostgreSQL mediante `SELECT ... FOR UPDATE` cuando sea necesario para garantizar la consistencia.

El bloqueo deberá aplicarse únicamente sobre el registro necesario y durante la transacción correspondiente, evitando mecanismos de concurrencia más complejos que no resulten necesarios para el alcance actual.

Si todas las validaciones y operaciones se completan correctamente, la transacción deberá confirmarse mediante `commit`.

Si durante la operación se produce un error o no puede completarse correctamente, deberá realizarse `rollback` y no deberá persistir ningún cambio parcial.

### 45.2. Alta y modificación de Factura

Las operaciones que puedan modificar el total facturado de una Obra deberán proteger la validación del límite de facturación frente a operaciones concurrentes.

Esto se aplicará tanto:

* al alta de una nueva Factura mediante `POST`;
* como a la modificación del importe de una Factura existente mediante `PUT`.

Dentro de la misma transacción, el backend deberá:

1. obtener y bloquear la fila de la Obra correspondiente mediante `SELECT ... FOR UPDATE`;
2. obtener su `monto_contratado`;
3. calcular el total de las Facturas asociadas a esa Obra que corresponda para la operación;
4. calcular el nuevo total facturado resultante;
5. comprobar que dicho total no supere `monto_contratado`;
6. realizar el `INSERT` o `UPDATE` de la Factura únicamente si la validación resulta correcta.

En el alta de una Factura, el nuevo total se calculará sumando el importe de la nueva Factura al total ya facturado.

En la modificación de una Factura, el nuevo total deberá calcularse teniendo en cuenta el nuevo importe de la Factura modificada sin contabilizar simultáneamente su importe anterior.

El bloqueo de la fila de la Obra deberá mantenerse hasta finalizar la transacción.

De esta manera, dos operaciones concurrentes sobre Facturas de una misma Obra no podrán validar simultáneamente el límite utilizando el mismo total anterior. La segunda operación deberá realizar su comprobación sobre los datos resultantes después de finalizar la primera.

Si el nuevo total facturado supera `monto_contratado`, la operación no deberá persistirse.

La API responderá con `409 Conflict`.

Mensaje de referencia:

`No se puede registrar o modificar la factura porque el monto total facturado excede el monto contratado de la obra.`

Una vez que una Obra posea al menos una Factura asociada, `monto_contratado` permanecerá bloqueado para edición según las reglas ya definidas.

### 45.3. Alta de Pago

Antes de registrar un Pago, el backend deberá comprobar que:

* la Factura correspondiente exista;
* todavía no exista otro Pago asociado a esa misma Factura;
* el importe del Pago coincida exactamente con el importe de la Factura;
* se cumplan las demás reglas de validación definidas para Pago.

La comprobación de existencia previa de un Pago y la inserción del nuevo Pago deberán ejecutarse de manera consistente dentro de la operación correspondiente.

Si ya existe un Pago asociado a la Factura, el nuevo Pago no deberá registrarse.

La API responderá con `409 Conflict`.

Mensaje de referencia:

`Ya existe un pago registrado para esta factura.`

Después de registrar correctamente un Pago, los totales y estados derivados de Factura y Obra deberán reflejar la nueva situación al volver a calcularse.

Si el nuevo Pago completa el cobro total de la Obra, se aplicará la regla definida en la sección 39.

El registro del Pago no modificará automáticamente el estado de ejecución de la Obra ni su `fecha_fin`.

### 45.4. Eliminación de Pago

La eliminación de un Pago no requerirá actualizar manualmente estados almacenados en Factura u Obra.

Los estados y totales derivados deberán recalcularse a partir de los datos existentes después de la eliminación.

Por lo tanto, no deberán almacenarse ni actualizarse redundantemente estados derivados como consecuencia de eliminar un Pago.

### 45.5. Errores y consistencia

Las reglas de negocio deberán validarse antes de confirmar una transacción.

Cuando una operación no pueda completarse por una regla de negocio, deberá devolverse el código HTTP correspondiente según las convenciones definidas en la sección 44.

Cuando se produzca un error técnico inesperado durante una operación transaccional, deberá realizarse `rollback` y responderse con `500 Internal Server Error`, sin exponer detalles técnicos al frontend.

El manejo concreto de conexiones PostgreSQL, apertura y cierre de conexiones, `commit`, `rollback` y tratamiento de excepciones se definirá en la sección correspondiente a la gestión técnica de PostgreSQL.

## 46. Validaciones definitivas por operación

Las operaciones de creación, modificación y eliminación deberán validar tanto los datos recibidos como las reglas de negocio correspondientes antes de realizar cambios persistentes.

Las validaciones específicas de cada recurso se definen a continuación.

### 46.1. Cliente

#### POST — Crear Cliente

Para crear un Cliente serán obligatorios:

* `cuit_cuil`;
* `razon_social`.

Serán opcionales:

* `responsable`;
* `telefono`;
* `email`.

Antes de crear el Cliente deberá validarse que:

* `cuit_cuil` se normalice eliminando espacios y guiones;
* después de su normalización, `cuit_cuil` contenga exactamente 11 dígitos numéricos;
* no exista otro Cliente con el mismo `cuit_cuil` normalizado;
* `razon_social` no quede vacía después de eliminar espacios al inicio y al final;
* `email`, cuando se informe, cumpla el formato básico definido;
* `telefono`, cuando se informe, contenga únicamente números.

El valor de `cuit_cuil` almacenado en la base de datos será siempre el valor normalizado, compuesto por exactamente 11 dígitos numéricos y sin espacios ni guiones.

Por ejemplo, un valor ingresado como:

`20-12345678-3`

deberá normalizarse y almacenarse como:

`20123456783`

Los campos opcionales sin contenido después de su normalización deberán tratarse como `null`.

Los datos inválidos o campos obligatorios faltantes producirán `400 Bad Request`.

Si ya existe otro Cliente con el mismo `cuit_cuil` normalizado, la operación deberá rechazarse con `409 Conflict`.

Mensaje de referencia:

`Ya existe un cliente con el CUIT/CUIL indicado.`

#### PUT — Modificar Cliente

La modificación general de un Cliente requerirá:

* `cuit_cuil`;
* `razon_social`.

Continuarán siendo opcionales:

* `responsable`;
* `telefono`;
* `email`.

Se aplicarán las mismas reglas de normalización y validación utilizadas en la creación.

En particular, `cuit_cuil` deberá normalizarse eliminando espacios y guiones antes de comprobar que el resultado contenga exactamente 11 dígitos numéricos.

El valor almacenado deberá ser siempre el CUIT/CUIL normalizado, sin espacios ni guiones.

Al comprobar la unicidad de `cuit_cuil`, podrá coincidir con el valor correspondiente al propio Cliente que está siendo modificado, pero no con el de otro Cliente.

Si el Cliente indicado por `id_cliente` no existe, la API responderá `404 Not Found`.

Si otro Cliente ya posee el mismo `cuit_cuil` normalizado, la modificación deberá rechazarse con `409 Conflict`.

Mensaje de referencia:

`Ya existe un cliente con el CUIT/CUIL indicado.`

Los datos inválidos o campos obligatorios faltantes producirán `400 Bad Request`.

#### DELETE — Eliminar Cliente

Antes de eliminar un Cliente deberá comprobarse su existencia y si posee Cotizaciones asociadas.

Si el Cliente indicado por `id_cliente` no existe, la API responderá `404 Not Found`.

Si el Cliente posee al menos una Cotización asociada, no podrá eliminarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`El cliente no puede eliminarse porque tiene cotizaciones asociadas.`

Si el Cliente existe y no posee Cotizaciones asociadas, podrá eliminarse según las convenciones de respuesta definidas para `DELETE`.

### 46.2. Cotización

#### POST — Crear Cotización

Para crear una Cotización serán obligatorios:

* `id_cliente`;
* `tipo_cotizacion`;
* `titulo`;
* `fecha`;
* `monto`.

`id_cliente` se obtendrá mediante la selección de un Cliente existente en el formulario. No será un dato de carga manual.

Si no existen Clientes disponibles, el formulario no dispondrá de opciones para crear una Cotización. Esta situación no constituye por sí misma un error de la API.

El backend deberá igualmente validar que el `id_cliente` recibido corresponda a un Cliente existente, independientemente de las restricciones aplicadas por el frontend.

`codigo_cotizacion` no será enviado por el frontend, ya que será generado automáticamente por el sistema.

`estado` tampoco será enviado por el frontend durante la creación.

Toda Cotización nueva se registrará automáticamente con estado:

`Presentada`

Los cambios posteriores a `Aceptada` o `Rechazada` podrán realizarse mediante `PUT`, siempre que la Cotización no haya originado una Obra y se respeten las demás reglas de negocio.

`numero_contratacion` tendrá obligatoriedad condicional:

* será obligatorio para `Licitación pública`;
* será obligatorio para `Licitación privada`;
* será obligatorio para `Concurso de precios`;
* será obligatorio para `Compra directa`;
* será opcional para `Presupuesto`.

Antes de crear la Cotización deberá validarse que:

* `id_cliente` corresponda a un Cliente existente;
* `tipo_cotizacion` pertenezca a los tipos permitidos;
* `titulo` no quede vacío después de aplicar la normalización correspondiente;
* `fecha` sea válida;
* `monto` sea mayor que cero;
* `numero_contratacion` esté informado cuando resulte obligatorio según el tipo de Cotización;
* los campos de texto respeten las reglas generales de normalización definidas para el proyecto.

Los campos obligatorios faltantes o los datos que no cumplan las validaciones producirán `400 Bad Request`.

Las validaciones de existencia e integridad de las relaciones deberán mantenerse también en el backend aunque el frontend utilice selects que limiten las opciones disponibles.

#### PUT — Modificar Cotización

Una Cotización podrá modificarse mediante `PUT` únicamente mientras no tenga una Obra asociada.

La modificación general requerirá:

* `id_cliente`;
* `tipo_cotizacion`;
* `titulo`;
* `fecha`;
* `monto`;
* `estado`.

`numero_contratacion` continuará sujeto a la obligatoriedad correspondiente al tipo de Cotización.

Se aplicarán las mismas reglas de normalización y validación utilizadas durante la creación.

`estado` deberá pertenecer a los valores permitidos:

* `Presentada`;
* `Aceptada`;
* `Rechazada`.

Mientras la Cotización no tenga una Obra asociada podrán modificarse sus datos respetando las reglas de negocio correspondientes.

Una vez que la Cotización haya originado una Obra, quedará bloqueada para edición y no podrá modificarse:

* el Cliente;
* el tipo de Cotización;
* el número de contratación;
* el título;
* la fecha;
* el monto;
* el estado.

Si la Cotización indicada por `id_cotizacion` no existe, la API responderá `404 Not Found`.

Si la Cotización ya posee una Obra asociada, la modificación será rechazada con `409 Conflict`.

Mensaje de referencia:

`La cotización no puede modificarse porque ya tiene una obra asociada.`

Los campos obligatorios faltantes o los datos inválidos producirán `400 Bad Request`.

#### DELETE — Eliminar Cotización

Antes de eliminar una Cotización deberá comprobarse su existencia y si posee una Obra asociada.

Si la Cotización indicada por `id_cotizacion` no existe, la API responderá `404 Not Found`.

Si la Cotización ya originó una Obra, no podrá eliminarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`La cotización no puede eliminarse porque tiene una obra asociada.`

Si la Cotización existe y no posee una Obra asociada, podrá eliminarse según las convenciones de respuesta definidas para `DELETE`.

### 46.3. Obra

#### POST — Crear Obra

Una Obra se creará manualmente a partir de una Cotización en estado `Aceptada` que todavía no haya originado otra Obra.

Para crear una Obra serán obligatorios:

* `id_cotizacion`;
* `titulo`;
* `monto_contratado`.

`id_cotizacion` se obtendrá mediante la selección de una Cotización disponible en el formulario. No será un dato de carga manual.

El frontend deberá utilizar para este selector únicamente Cotizaciones en estado `Aceptada` que todavía no tengan una Obra asociada.

Si no existen Cotizaciones disponibles, el formulario no dispondrá de opciones para crear una Obra. Esta situación no constituye por sí misma un error de la API.

El backend deberá igualmente validar que:

* `id_cotizacion` corresponda a una Cotización existente;
* la Cotización se encuentre en estado `Aceptada`;
* la Cotización todavía no tenga una Obra asociada.

`codigo_obra` no será enviado por el frontend, ya que será generado automáticamente por el sistema.

`estado_ejecucion` tampoco será enviado por el frontend durante la creación.

Toda Obra nueva se registrará automáticamente con estado de ejecución:

`Pendiente`

El título se inicializará a partir del título de la Cotización seleccionada y podrá modificarse antes de crear la Obra.

La inicialización del título será responsabilidad del frontend.

Al seleccionar una Cotización disponible, Vue deberá precargar el campo `titulo` del formulario de Obra con el título de dicha Cotización.

El usuario podrá conservar ese valor o modificarlo antes de crear la Obra.

El valor final del campo `titulo` será enviado por el frontend en la solicitud `POST /api/obras`.

El backend no deberá volver a copiar ni sobrescribir automáticamente el título a partir de la Cotización. Su responsabilidad será validar que el `titulo` recibido no quede vacío después de aplicar la normalización correspondiente y almacenarlo como título de la nueva Obra.

Serán opcionales durante la creación, según corresponda:

* `fecha_estimada_fin`;
* `tipo_documento`;
* `numero_documento`;
* `fecha_documento`.

`fecha_inicio` no deberá informarse durante la creación, ya que toda Obra nueva comienza en estado `Pendiente` y este estado representa una Obra que todavía no ha iniciado efectivamente.

`fecha_inicio` podrá registrarse posteriormente cuando la Obra cambie a un estado que la requiera.

`fecha_fin` tampoco deberá informarse durante la creación de una Obra en estado `Pendiente`, ya que la existencia de `fecha_fin` requiere que la Obra se encuentre en estado `Finalizada`.

`motivo_estado` no será necesario durante la creación, ya que la Obra comienza automáticamente en estado `Pendiente`.

Antes de crear la Obra deberá validarse que:

* la Cotización seleccionada cumpla las condiciones necesarias para originar una Obra;
* `titulo` no quede vacío después de aplicar la normalización correspondiente;
* `monto_contratado` sea mayor que cero;
* no se hayan informado `fecha_inicio`, `fecha_fin` ni `motivo_estado`;
* `fecha_estimada_fin`, cuando se informe, sea una fecha válida;
* los datos del documento contractual respeten las reglas definidas para dichos campos;
* los campos de texto respeten las reglas generales de normalización del proyecto.

Los campos obligatorios faltantes o los datos inválidos producirán `400 Bad Request`.

Si la Cotización no puede utilizarse para crear una Obra porque no se encuentra `Aceptada` o porque ya posee una Obra asociada, la operación deberá rechazarse según las convenciones de conflicto de reglas de negocio definidas para la API.

Las validaciones deberán mantenerse en el backend aunque el frontend utilice un select que limite las Cotizaciones disponibles.

#### PUT — Modificar generalmente una Obra

Una Obra podrá modificarse generalmente mediante `PUT` mientras no tenga Facturas asociadas.

La modificación general permitirá modificar, respetando las reglas correspondientes:

* el título;
* el monto contratado;
* la fecha de inicio;
* la fecha estimada de finalización;
* el estado de ejecución;
* el motivo de estado;
* los datos del documento contractual;
* la fecha de finalización cuando corresponda según el estado.

La Cotización de origen no deberá modificarse una vez creada la Obra.

Se aplicarán las reglas generales de normalización y todas las validaciones de coherencia entre estados, fechas y campos condicionales definidas para Obra.

En particular, una Obra cuyo estado resultante sea `Pendiente` no deberá tener `fecha_inicio` ni `fecha_fin`.

Si la Obra indicada por `id_obra` no existe, la API responderá `404 Not Found`.

Si la Obra ya posee al menos una Factura asociada, sus datos generales estarán bloqueados y no podrán modificarse mediante `PUT`.

En ese caso, la operación deberá rechazarse con `409 Conflict`.

Mensaje de referencia:

`La obra no puede modificarse de forma general porque tiene facturas asociadas.`

Los campos obligatorios faltantes, estados inválidos, fechas incoherentes o demás datos que no cumplan las validaciones producirán `400 Bad Request`.

#### PATCH — Modificar seguimiento de ejecución

`PATCH` se utilizará para las modificaciones parciales relacionadas con el seguimiento de ejecución de la Obra.

Podrán modificarse mediante esta operación:

* `estado_ejecucion`;
* `fecha_inicio`;
* `fecha_fin`;
* `motivo_estado`.

Esta operación continuará disponible aunque la Obra tenga Facturas asociadas, ya que la existencia de Facturas bloquea los datos generales de la Obra pero no su seguimiento de ejecución.

Solo deberán enviarse los campos que se desean modificar.

Después de aplicar los cambios solicitados, el estado resultante de la Obra deberá respetar todas las reglas de coherencia definidas.

En particular:

* `Pendiente` representa una Obra todavía no iniciada y no deberá tener `fecha_inicio` ni `fecha_fin`;
* `En ejecución` requiere `fecha_inicio`;
* `Finalizada` requiere `fecha_inicio` y `fecha_fin`;
* si se informa `fecha_fin`, el estado deberá ser `Finalizada`;
* `fecha_fin` no podrá ser anterior a `fecha_inicio`;
* `Suspendida` requerirá `fecha_inicio` y `motivo_estado`;
* `Cancelada` requerirá `motivo_estado`.

El cambio de estado no deberá borrar automáticamente fechas previamente registradas.

Por lo tanto, no podrá cambiarse una Obra a `Pendiente` mientras conserve `fecha_inicio` o `fecha_fin`. Si se pretende volver válidamente a `Pendiente`, los cambios necesarios deberán enviarse expresamente en la misma operación para que el estado resultante sea coherente.

Si el estado resultante exige un dato que no se encuentra informado, la modificación deberá rechazarse hasta que se proporcione la información necesaria.

Si la Obra indicada por `id_obra` no existe, la API responderá `404 Not Found`.

Los cambios que produzcan una combinación inválida de estado, fechas o campos condicionales responderán `400 Bad Request`.

#### DELETE — Eliminar Obra

Antes de eliminar una Obra deberá comprobarse su existencia y si posee Facturas asociadas.

Si la Obra indicada por `id_obra` no existe, la API responderá `404 Not Found`.

Si la Obra posee al menos una Factura asociada, no podrá eliminarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`La obra no puede eliminarse porque tiene facturas asociadas.`

Si la Obra existe y no posee Facturas asociadas, podrá eliminarse según las convenciones de respuesta definidas para `DELETE`.

### 46.4. Factura

#### POST — Crear Factura

Para crear una Factura serán obligatorios:

* `id_obra`;
* `numero_factura`;
* `fecha_emision`;
* `importe`.

Será opcional:

* `observaciones`.

`id_obra` se obtendrá mediante la selección de una Obra existente en el formulario. No será un dato de carga manual.

Si no existen Obras disponibles, el formulario no dispondrá de opciones para crear una Factura. Esta situación no constituye por sí misma un error de la API.

El backend deberá igualmente validar que el `id_obra` recibido corresponda a una Obra existente, independientemente de las restricciones aplicadas por el frontend.

Antes de crear la Factura deberá validarse que:

* `id_obra` corresponda a una Obra existente;
* `numero_factura` no quede vacío después de aplicar la normalización correspondiente;
* `fecha_emision` sea válida;
* `importe` sea mayor que cero;
* los campos de texto respeten las reglas generales de normalización definidas para el proyecto;
* la suma de los importes de las Facturas ya asociadas a la Obra más el importe de la nueva Factura no supere `monto_contratado`.

La comprobación del total facturado y la inserción de la nueva Factura deberán realizarse dentro de la misma transacción y respetar las reglas definidas en la sección 45.

Dentro de esa transacción, la fila de la Obra correspondiente deberá bloquearse mediante `SELECT ... FOR UPDATE` antes de calcular el total facturado.

Una vez obtenido el bloqueo, el backend deberá:

1. obtener `monto_contratado`;
2. calcular la suma de los importes de las Facturas ya asociadas a la Obra;
3. sumar el importe de la nueva Factura;
4. comprobar que el total resultante no supere `monto_contratado`;
5. insertar la nueva Factura únicamente si la validación resulta correcta.

El bloqueo deberá mantenerse hasta finalizar la transacción.

Si el nuevo total facturado supera `monto_contratado`, la Factura no deberá registrarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`No se puede registrar la factura porque el monto total facturado excede el monto contratado de la obra.`

Los campos obligatorios faltantes o los datos inválidos producirán `400 Bad Request`.

Las validaciones de existencia e integridad deberán mantenerse también en el backend aunque el frontend utilice selects que limiten las opciones disponibles.

#### PUT — Modificar Factura

Una Factura podrá modificarse mediante `PUT` únicamente mientras no tenga un Pago asociado.

La Obra asociada a la Factura quedará fija después de su creación.

Por lo tanto, `id_obra` no será editable mediante `PUT`.

La modificación general permitirá modificar:

* `numero_factura`;
* `fecha_emision`;
* `importe`;
* `observaciones`.

Para la modificación serán obligatorios:

* `numero_factura`;
* `fecha_emision`;
* `importe`.

`observaciones` continuará siendo opcional.

Se aplicarán las mismas reglas de normalización y validación correspondientes a estos campos utilizadas durante la creación.

Si la Factura indicada por `id_factura` no existe, la API responderá `404 Not Found`.

Si la Factura ya posee un Pago asociado, quedará bloqueada para modificación y la API responderá `409 Conflict`.

Mensaje de referencia:

`La factura no puede modificarse porque tiene un pago asociado.`

La modificación deberá respetar las reglas de transacción y atomicidad definidas en la sección 45.

La fila de la Obra asociada a la Factura deberá bloquearse mediante `SELECT ... FOR UPDATE` dentro de la misma transacción antes de validar el nuevo total facturado.

Para realizar esta validación, el backend deberá:

1. obtener y bloquear la Obra asociada a la Factura;
2. obtener su `monto_contratado`;
3. calcular la suma de los importes de las demás Facturas asociadas a esa Obra, excluyendo la Factura que está siendo modificada;
4. sumar el nuevo `importe` de la Factura;
5. comprobar que el total resultante no supere `monto_contratado`;
6. realizar el `UPDATE` únicamente si la validación resulta correcta.

De esta manera, el cálculo no deberá contabilizar simultáneamente el importe anterior y el nuevo importe de la misma Factura.

El bloqueo de la Obra deberá mantenerse hasta finalizar la transacción.

Si el nuevo total facturado supera `monto_contratado`, la modificación no deberá realizarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`No se puede modificar la factura porque el monto total facturado excede el monto contratado de la obra.`

Los campos obligatorios faltantes o los datos inválidos producirán `400 Bad Request`.

Si una Factura fue asociada por error a una Obra incorrecta y todavía no posee un Pago, deberá eliminarse y crearse nuevamente asociándola a la Obra correcta.

#### DELETE — Eliminar Factura

Antes de eliminar una Factura deberá comprobarse su existencia y si posee un Pago asociado.

Si la Factura indicada por `id_factura` no existe, la API responderá `404 Not Found`.

Si la Factura posee un Pago asociado, no podrá eliminarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`La factura no puede eliminarse porque tiene un pago asociado.`

Si la Factura existe y no posee un Pago asociado, podrá eliminarse según las convenciones de respuesta definidas para `DELETE`.

### 46.5. Pago

#### POST — Crear Pago

Para crear un Pago serán obligatorios:

* `id_factura`;
* `fecha_pago`;
* `importe`;
* `medio_pago`.

`observaciones` será opcional, excepto cuando `medio_pago` sea `Otros`, caso en el cual será obligatorio.

`id_factura` se obtendrá mediante la selección de una Factura disponible en el formulario. No será un dato de carga manual.

El frontend deberá utilizar para este selector únicamente Facturas que todavía no posean un Pago asociado.

Si no existen Facturas disponibles, el formulario no dispondrá de opciones para crear un Pago. Esta situación no constituye por sí misma un error de la API.

El backend deberá igualmente validar que:

* `id_factura` corresponda a una Factura existente;
* la Factura todavía no tenga un Pago asociado.

Antes de crear el Pago deberá validarse que:

* `fecha_pago` sea válida;
* `importe` sea mayor que cero;
* `importe` coincida exactamente con el importe total de la Factura;
* `medio_pago` pertenezca a los valores permitidos: `Transferencia`, `Efectivo`, `Cheque`, `Echeq` u `Otros`;
* cuando `medio_pago` sea `Otros`, `observaciones` contenga información después de aplicar la normalización correspondiente;
* los campos de texto respeten las reglas generales de normalización definidas para el proyecto.

Solo se permitirá un Pago por Factura. No se admitirán pagos parciales por Factura.

La comprobación de existencia previa de un Pago y la inserción del nuevo Pago deberán respetar las reglas de consistencia y atomicidad definidas en la sección 45.

Si ya existe un Pago asociado a la Factura, el nuevo Pago no deberá registrarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`Ya existe un pago registrado para esta factura.`

Si el importe informado no coincide exactamente con el importe total de la Factura, el Pago no deberá registrarse y la API responderá `409 Conflict`.

Mensaje de referencia:

`El importe del pago debe coincidir con el importe total de la factura.`

Los campos obligatorios faltantes, fechas inválidas, medios de Pago no permitidos o incumplimientos de las demás validaciones de formato producirán `400 Bad Request`.

Las validaciones de existencia e integridad deberán mantenerse también en el backend aunque el frontend utilice un select que limite las Facturas disponibles.

Después de registrar correctamente el Pago:

* el estado individual derivado de la Factura deberá resultar `Pagada`;
* deberá recalcularse el total cobrado correspondiente a la Obra a través de sus Facturas y Pagos;
* el estado global de cobro derivado de la Obra deberá reflejar la nueva situación.

Si el Pago completa el cobro total de la Obra y esta todavía no se encuentra en estado de ejecución `Finalizada`, el Pago se registrará normalmente con `201 Created`.

La respuesta mantendrá la estructura general de una creación exitosa:

`{"message": "...", "data": ...}`

No se incorporará un campo adicional `warning`.

En este caso, `message` contendrá el mensaje completo de confirmación y advertencia definido en la sección 39:

`Pago registrado correctamente. La obra se encuentra totalmente cobrada. Si la obra ya finalizó, recuerde cambiar su estado a Finalizada e indicar la fecha de finalización.`

`data` contendrá normalmente el Pago creado.

El frontend deberá mostrar este `message` al usuario como resultado de la creación exitosa.

La advertencia no impedirá el registro del Pago, no modificará el código `201 Created` y no será tratada como un error.

El registro del Pago no modificará automáticamente `estado_ejecucion` ni `fecha_fin` de la Obra.

#### PUT/PATCH — Modificación de Pago

Los Pagos no serán editables.

No se implementarán operaciones `PUT` ni `PATCH` para Pago.

Si un Pago fue registrado incorrectamente, deberá eliminarse y posteriormente crearse nuevamente con los datos correctos.

#### DELETE — Eliminar Pago

Un Pago podrá eliminarse porque no posee entidades dependientes posteriores dentro del modelo actual.

Si el Pago indicado por `id_pago` no existe, la API responderá `404 Not Found`.

Si el Pago existe, podrá eliminarse según las convenciones de respuesta definidas para `DELETE`.

La eliminación de un Pago no requerirá actualizar manualmente estados almacenados en Factura u Obra.

Después de eliminarlo:

* la Factura correspondiente volverá a resultar `Pendiente` al calcular su estado derivado;
* deberá recalcularse el total cobrado de la Obra;
* el estado global de cobro derivado de la Obra deberá reflejar automáticamente la nueva situación.

No deberán almacenarse ni modificarse redundantemente estados derivados como consecuencia de eliminar un Pago.

## 47. Datos derivados en las respuestas de la API

Los datos derivados se calcularán a partir de la información almacenada y de las relaciones existentes entre las entidades.

No deberán almacenarse como columnas adicionales en PostgreSQL cuando puedan obtenerse de forma confiable mediante consultas y cálculos sobre los datos existentes.

El backend será responsable de realizar estos cálculos y devolver los resultados correspondientes en las respuestas JSON de la API.

El frontend utilizará los valores derivados recibidos desde la API y no deberá reproducir de manera independiente las reglas de negocio necesarias para calcularlos.

### 47.1. Datos derivados de Obra

Las respuestas de la API correspondientes a Obra deberán incluir los siguientes campos derivados:

* `total_facturado`;
* `saldo_por_facturar`;
* `estado_facturacion`;
* `total_cobrado`;
* `saldo_por_cobrar`;
* `estado_cobro`.

Estos campos no forman parte de las columnas almacenadas de la tabla `obra`.

#### Total facturado

`total_facturado` será la suma de los importes de todas las Facturas asociadas a la Obra.

Conceptualmente:

`total_facturado = SUM(Factura.importe)`

Si la Obra no posee Facturas asociadas:

`total_facturado = 0`

#### Saldo por facturar

`saldo_por_facturar` indicará el monto contratado que todavía no fue facturado.

Conceptualmente:

`saldo_por_facturar = monto_contratado - total_facturado`

Si no existen Facturas, el saldo por facturar será igual a `monto_contratado`.

De acuerdo con las reglas de negocio definidas, `total_facturado` nunca podrá superar `monto_contratado`.

#### Estado de facturación

`estado_facturacion` se determinará comparando `total_facturado` con `monto_contratado`.

Los valores posibles serán:

* `Sin facturar`: `total_facturado = 0`;
* `Facturada parcialmente`: `total_facturado > 0` y `total_facturado < monto_contratado`;
* `Facturada totalmente`: `total_facturado = monto_contratado`.

Este estado será exclusivamente derivado y no deberá almacenarse ni editarse manualmente.

#### Total cobrado

`total_cobrado` será la suma de los importes de los Pagos asociados a las Facturas correspondientes a la Obra.

La relación utilizada para obtener este valor será:

`Obra → Factura → Pago`

Conceptualmente:

`total_cobrado = SUM(Pago.importe)`

considerando únicamente los Pagos correspondientes a Facturas cuyo `id_obra` pertenezca a la Obra consultada.

Si no existen Pagos:

`total_cobrado = 0`

#### Saldo por cobrar

`saldo_por_cobrar` indicará la parte del monto contratado que todavía no fue cobrada.

Conceptualmente:

`saldo_por_cobrar = monto_contratado - total_cobrado`

Si no existen Pagos, el saldo por cobrar será igual a `monto_contratado`.

#### Estado de cobro

`estado_cobro` se determinará comparando `total_cobrado` con `monto_contratado`.

Los valores posibles serán:

* `Adeudada`: `total_cobrado = 0`;
* `Pagada parcialmente`: `total_cobrado > 0` y `total_cobrado < monto_contratado`;
* `Pagada`: `total_cobrado = monto_contratado`.

Este estado será exclusivamente derivado y no deberá almacenarse ni editarse manualmente.

### 47.2. Datos derivados de Factura

Las respuestas de la API correspondientes a Factura deberán incluir:

* `estado_pago`.

`estado_pago` será un dato derivado y no formará parte de las columnas almacenadas de la tabla `factura`.

Su valor se determinará mediante la relación:

`Factura → Pago`

Los valores posibles serán:

* `Pendiente`: no existe un Pago asociado a la Factura;
* `Pagada`: existe un Pago asociado y su importe coincide con el importe de la Factura.

Debido a que cada Factura admite un único Pago y no se permiten pagos parciales por Factura, no se incorporará un estado intermedio de pago para una Factura individual.

### 47.3. Inclusión de los datos derivados en las respuestas

Los campos derivados de Obra deberán incluirse tanto en:

* `GET /api/obras`;
* `GET /api/obras/{id_obra}`.

Cuando una operación `POST`, `PUT` o `PATCH` devuelva en `data` la representación de una Obra, deberá utilizar la misma representación del recurso e incluir sus campos derivados actualizados.

Los campos derivados de Factura deberán incluirse tanto en:

* `GET /api/facturas`;
* `GET /api/facturas/{id_factura}`.

Cuando una operación `POST` o `PUT` devuelva en `data` la representación de una Factura, deberá incluir también su `estado_pago` derivado.

Después de crear o eliminar un Pago, las consultas posteriores de Factura y Obra deberán reflejar automáticamente los nuevos totales, saldos y estados derivados.

### 47.4. Responsabilidad del backend y frontend

El backend será la fuente de verdad para el cálculo de los datos derivados.

Las consultas SQL podrán utilizar las agregaciones y relaciones necesarias para obtener los totales correspondientes.

El frontend no deberá reconstruir estas reglas mediante cálculos propios cuando el dato derivado ya sea proporcionado por la API.

El frontend será responsable únicamente de:

* presentar los valores recibidos;
* aplicar el formato visual correspondiente;
* utilizar los estados derivados para la representación de la interfaz cuando resulte necesario.

De esta manera se evita duplicar reglas de negocio entre Flask y Vue y se mantiene una única lógica de cálculo para los estados y totales económicos del sistema.

## 48. Responsabilidad de las capas del backend

El backend deberá mantener una separación clara de responsabilidades entre `routes`, `controllers`, `models`, `database` y `utils`.

Como principio general, la lógica del mismo tipo y las decisiones que tengan el mismo nivel de impacto deberán concentrarse en la misma capa.

No deberán distribuirse arbitrariamente reglas de negocio, SQL, decisiones HTTP o lógica de infraestructura entre diferentes carpetas.

El flujo general será:

`Route → Controller → Model → PostgreSQL`

La información obtenida desde PostgreSQL regresará a través de las mismas capas hasta construir la respuesta HTTP correspondiente.

### 48.1. Routes

`backend/routes/` será responsable de definir la interfaz HTTP de la API mediante Flask Blueprints.

Cada módulo tendrá sus rutas correspondientes.

Las routes serán responsables de:

* definir los endpoints;
* asociar cada endpoint con su método HTTP;
* obtener identificadores provenientes de la URL;
* obtener parámetros de consulta;
* obtener el cuerpo JSON de la solicitud cuando corresponda;
* delegar la operación al controller correspondiente.

Las routes deberán mantenerse livianas.

No deberán contener:

* consultas SQL;
* acceso directo a PostgreSQL;
* reglas de negocio;
* cálculos económicos;
* validaciones propias de una entidad;
* decisiones sobre integridad entre entidades.

La lógica funcional deberá delegarse al controller correspondiente.

### 48.2. Controllers

`backend/controllers/` será responsable de concentrar la lógica de negocio y coordinar las operaciones de cada módulo.

Los controllers deberán:

* validar los datos recibidos según la operación solicitada;
* aplicar las reglas de negocio definidas en este documento;
* decidir si una operación puede realizarse;
* coordinar las consultas y escrituras necesarias mediante los models;
* interpretar los resultados obtenidos desde los models;
* determinar los códigos HTTP correspondientes;
* construir los mensajes de éxito o error;
* construir la respuesta JSON según el contrato general de la API;
* coordinar las operaciones que requieran una transacción.

Las decisiones funcionales deberán permanecer en esta capa.

Por ejemplo, el controller podrá solicitar al model que compruebe si una Factura posee un Pago asociado.

El model devolverá el resultado de esa consulta.

El controller será responsable de interpretar ese resultado y determinar que, si existe un Pago, la Factura no puede modificarse o eliminarse y corresponde responder `409 Conflict`.

Por lo tanto:

**el model obtiene o modifica datos; el controller interpreta esos datos según las reglas de negocio.**

Los controllers no deberán contener SQL directo.

### 48.3. Models

`backend/models/` será responsable del acceso a los datos y de las operaciones SQL correspondientes a cada entidad.

Los models utilizarán SQL directo mediante `psycopg`.

Serán responsables de:

* ejecutar `SELECT`;
* ejecutar `INSERT`;
* ejecutar `UPDATE`;
* ejecutar `DELETE`;
* realizar `JOIN`;
* realizar agregaciones como `SUM`;
* obtener registros por identificador;
* comprobar existencia de registros y relaciones;
* obtener los datos necesarios para calcular valores derivados;
* ejecutar las operaciones de persistencia solicitadas por los controllers.

Los models podrán responder preguntas sobre el estado de los datos, por ejemplo:

* si existe un Cliente;
* si una Cotización posee una Obra;
* si una Obra posee Facturas;
* si una Factura posee un Pago;
* cuánto se encuentra facturado para una Obra;
* cuánto se encuentra cobrado para una Obra.

Sin embargo, no deberán decidir qué consecuencia funcional tienen esos resultados.

Los models no deberán:

* determinar códigos HTTP;
* construir mensajes destinados al usuario;
* construir respuestas Flask;
* decidir reglas de negocio;
* decidir qué debe mostrarse en la interfaz.

Las consultas necesarias para los datos derivados también pertenecerán a esta capa.

Por ejemplo, el model podrá obtener mediante `SUM` y `JOIN` el total facturado y el total cobrado de una Obra.

La interpretación de esos valores según las reglas definidas para `estado_facturacion` y `estado_cobro` corresponderá al controller.

### 48.4. Database

`backend/database/` concentrará la infraestructura común necesaria para trabajar con PostgreSQL.

Además de contener los archivos destinados a reproducir la base de datos, como:

* `schema.sql`;
* `seed.sql`;

esta capa contendrá la lógica común necesaria para obtener y administrar las conexiones utilizadas por el backend.

La gestión técnica concreta de conexiones y transacciones se define en la sección 49.

`database/` no deberá contener reglas de negocio propias de Cliente, Cotización, Obra, Factura o Pago.

### 48.5. Utils

`backend/utils/` contendrá únicamente funciones auxiliares reutilizables que no pertenezcan naturalmente a una entidad o capa específica.

Podrán ubicarse en esta carpeta, cuando exista reutilización real:

* funciones comunes de normalización;
* validaciones de formato utilizadas por varios módulos;
* otros helpers transversales claramente justificados.

No deberán trasladarse reglas de negocio a `utils` únicamente para reutilizar código.

Una regla que determine si una operación de negocio está permitida continuará perteneciendo al controller correspondiente.

No deberán crearse helpers, archivos o abstracciones en `utils` de manera anticipada si no existe una necesidad concreta.

### 48.6. Principio de separación

La separación deberá respetar como criterio general:

* `routes` → HTTP y enrutamiento;
* `controllers` → lógica y decisiones de negocio;
* `models` → SQL y acceso a datos;
* `database` → infraestructura de PostgreSQL;
* `utils` → lógica auxiliar transversal reutilizable.

Esta distribución deberá mantenerse de forma consistente en todos los módulos del backend.

No deberá trasladarse una misma clase de responsabilidad entre capas diferentes sin una razón técnica concreta.

## 49. Manejo de conexiones y transacciones PostgreSQL

El acceso a PostgreSQL se realizará mediante `psycopg` y deberá mantener una gestión consistente de conexiones, transacciones y errores técnicos.

La infraestructura común de conexión pertenecerá a `backend/database/`.

Los models utilizarán las conexiones para ejecutar SQL, mientras que los controllers coordinarán las operaciones de negocio y determinarán cuándo una transacción puede confirmarse o debe revertirse.

### 49.1. Conexión a PostgreSQL

La configuración de conexión se obtendrá mediante las variables de entorno definidas para el proyecto:

* `DB_HOST`;
* `DB_PORT`;
* `DB_NAME`;
* `DB_USER`;
* `DB_PASSWORD`.

Las credenciales reales no deberán escribirse directamente en el código fuente.

`backend/database/` deberá proporcionar la lógica común necesaria para obtener una conexión a PostgreSQL utilizando esta configuración.

No deberá duplicarse la construcción de conexiones de manera independiente en cada model o controller.

### 49.2. Uso de la conexión

Los models serán responsables de ejecutar las consultas SQL utilizando la conexión correspondiente.

Cuando una operación de negocio requiera varias consultas o escrituras relacionadas, estas deberán poder utilizar la misma conexión para formar parte de una única transacción.

Los models no deberán realizar `commit` de manera independiente cuando formen parte de una operación transaccional coordinada por un controller.

Esto evita confirmar parcialmente una operación antes de comprobar que todas sus partes puedan completarse correctamente.

### 49.3. Control de la transacción

El controller será responsable de coordinar el resultado general de las operaciones de negocio que requieran transacción.

Cuando todas las validaciones y operaciones SQL correspondientes hayan finalizado correctamente:

`commit`

Cuando se produzca un error que impida completar correctamente la operación:

`rollback`

De esta manera, una operación crítica deberá completarse íntegramente o no producir cambios persistentes parciales.

Las operaciones identificadas como críticas deberán respetar además las reglas de atomicidad definidas en la sección 45.

### 49.4. Commit

`commit` deberá realizarse únicamente cuando la operación haya completado correctamente todas las validaciones y escrituras necesarias.

No deberán realizarse confirmaciones intermedias que puedan dejar los datos en un estado parcialmente actualizado.

En operaciones simples que impliquen una única escritura, también deberá garantizarse que la modificación se confirme únicamente después de ejecutarse correctamente.

### 49.5. Rollback

Si se produce una excepción durante una operación que ya haya iniciado modificaciones sobre la base de datos, deberá ejecutarse `rollback` antes de finalizar la operación.

El objetivo será devolver la conexión a un estado consistente y evitar que persistan cambios parciales.

Una operación que falle no deberá dejar modificaciones incompletas en PostgreSQL.

### 49.6. Cierre de conexiones

Toda conexión abierta deberá cerrarse correctamente una vez finalizado su uso, independientemente de que la operación haya terminado con éxito o con error.

El manejo de conexiones deberá garantizar su liberación también cuando se produzcan excepciones.

No deberán quedar conexiones abiertas innecesariamente después de completar una solicitud.

La implementación podrá utilizar los mecanismos provistos por Python y `psycopg` para garantizar el manejo seguro de los recursos, evitando duplicar manualmente lógica de apertura y cierre cuando exista una solución estándar y clara.

### 49.7. Manejo de errores técnicos

Los errores técnicos de PostgreSQL deberán manejarse de manera controlada.

Los detalles internos de una excepción de base de datos no deberán exponerse directamente al frontend.

Cuando se produzca un error inesperado que impida completar una operación:

* deberá realizarse `rollback` cuando corresponda;
* deberá cerrarse correctamente la conexión;
* el backend responderá según la convención `500 Internal Server Error` definida para la API.

La respuesta destinada al frontend utilizará el mensaje genérico definido para errores internos.

Los detalles técnicos podrán utilizarse internamente para diagnóstico durante el desarrollo, pero no deberán formar parte del mensaje presentado al usuario.

### 49.8. Separación de responsabilidades

La gestión de PostgreSQL deberá respetar la siguiente distribución:

* `database` proporciona la infraestructura común para obtener y administrar conexiones;
* `models` ejecutan las consultas y modificaciones SQL;
* `controllers` coordinan las operaciones de negocio y determinan el resultado de las transacciones;
* `routes` no administran conexiones ni ejecutan SQL.

Los models no deberán confirmar unilateralmente partes de una operación que el controller necesite tratar de manera atómica.

Esta separación deberá aplicarse consistentemente en todos los módulos.

## 50. Contrato frontend-backend para formularios y selects

La interacción entre Vue y Flask deberá mantener una separación clara de responsabilidades.

El frontend será responsable de presentar formularios, selects y opciones disponibles para el usuario.

El backend será responsable de validar los datos recibidos y garantizar el cumplimiento de las reglas de negocio, independientemente de las restricciones aplicadas previamente por la interfaz.

Como criterio general:

* los selects que dependan de datos existentes en la base deberán obtener sus opciones mediante la API;
* el backend deberá devolver únicamente las opciones que resulten válidas según las reglas de negocio cuando exista un criterio de disponibilidad;
* el frontend no deberá reconstruir por su cuenta reglas de negocio para determinar qué registros pueden seleccionarse;
* los valores estáticos y predefinidos que no dependan de datos almacenados se definirán directamente en Vue;
* Flask deberá validar igualmente que cualquier valor recibido pertenezca al conjunto permitido.

### 50.1. Select de Cliente para Cotización

Para crear o modificar una Cotización, el Cliente se seleccionará mediante un select construido a partir de Clientes existentes.

El frontend obtendrá los Clientes mediante la API correspondiente.

`id_cliente` no será un dato de escritura manual por parte del usuario.

Si no existen Clientes, el select no dispondrá de opciones y no podrá completarse la creación de una Cotización.

Esta situación no constituye por sí misma un error de la API.

El backend deberá validar igualmente que el `id_cliente` recibido corresponda a un Cliente existente.

### 50.2. Select de Cotización para Obra

Para crear una Obra, el frontend deberá mostrar únicamente Cotizaciones que:

* se encuentren en estado `Aceptada`;
* todavía no hayan originado una Obra.

La consulta utilizará el filtro correspondiente de la API.

El backend será responsable de determinar qué Cotizaciones cumplen estas condiciones y devolver únicamente las opciones válidas.

Si no existen Cotizaciones disponibles, el select permanecerá sin opciones y no podrá completarse la creación de una Obra.

Esta situación no constituye por sí misma un error de la API.

El backend deberá volver a validar las condiciones de la Cotización seleccionada al procesar el `POST` de Obra.

### 50.3. Select de Obra para Factura

Para crear una Factura, el frontend deberá mostrar únicamente Obras que todavía posean saldo por facturar.

Una Obra será seleccionable cuando:

`total_facturado < monto_contratado`

equivalentemente:

`saldo_por_facturar > 0`

Las Obras cuyo estado derivado de facturación sea `Facturada totalmente` no deberán aparecer en el select.

Para este fin se incorporará un filtro sobre el recurso Obras:

`GET /api/obras?con_saldo_por_facturar=true`

Este filtro devolverá únicamente Obras cuyo total facturado sea inferior a `monto_contratado`.

El cálculo de disponibilidad será responsabilidad del backend.

El frontend no deberá descargar todas las Obras y reproducir esta regla para decidir cuáles mostrar.

Si no existen Obras con saldo por facturar, el select permanecerá sin opciones y no podrá completarse la creación de una Factura.

Esta situación no constituye por sí misma un error de la API.

El backend deberá mantener igualmente la validación de sobrefacturación definida en las secciones anteriores.

### 50.4. Select de Factura para Pago

Para crear un Pago, el frontend deberá mostrar únicamente Facturas que todavía no posean un Pago asociado.

La consulta utilizará:

`GET /api/facturas?sin_pago=true`

El backend deberá determinar la disponibilidad comprobando la ausencia de un Pago asociado a cada Factura.

Las Facturas que ya tengan un Pago no deberán aparecer en el select.

Si no existen Facturas disponibles, el select permanecerá sin opciones y no podrá completarse la creación de un Pago.

Esta situación no constituye por sí misma un error de la API.

El backend deberá validar igualmente que la Factura seleccionada todavía no tenga un Pago al procesar el `POST`.

### 50.5. Valores estáticos de los selects

Los valores predefinidos que no dependan de registros almacenados en PostgreSQL se definirán directamente en Vue.

No se crearán endpoints auxiliares destinados únicamente a devolver listas estáticas.

Dentro de este criterio se incluyen, entre otros:

* tipos de Cotización;
* estados de Cotización;
* estados de ejecución de Obra;
* tipos de documento contractual;
* medios de Pago.

Vue utilizará estos valores para construir los selects correspondientes.

Flask mantendrá las mismas listas permitidas para validar los datos recibidos.

La existencia de un select controlado en el frontend no sustituye la validación del backend.

### 50.6. Responsabilidad general

Los selects relacionados con entidades almacenadas seguirán este criterio:

* Cotización → Clientes existentes;
* Obra → Cotizaciones `Aceptada` sin Obra;
* Factura → Obras con saldo por facturar;
* Pago → Facturas sin Pago.

El backend será responsable de determinar la disponibilidad de los registros cuando esta dependa de una regla de negocio.

El frontend será responsable de presentar las opciones recibidas y evitar la entrada manual de identificadores relacionados.

Esta separación permite mantener las reglas de disponibilidad centralizadas en Flask y evita duplicar lógica de negocio en Vue.

## 51. Datos de prueba y `seed.sql`

El archivo:

`backend/database/seed.sql`

deberá contener un conjunto mínimo de datos de prueba suficiente para representar todos los estados funcionales relevantes definidos para los módulos del sistema.

La cantidad de registros no será uniforme entre las tablas. Se utilizará la cantidad estrictamente necesaria para cubrir los estados y escenarios principales sin agregar datos redundantes.

El `seed.sql` deberá respetar:

* claves primarias;
* claves foráneas;
* restricciones de unicidad;
* reglas de negocio;
* reglas de edición y dependencia;
* estados permitidos;
* reglas de facturación;
* reglas de Pago;
* consistencia entre montos relacionados.

Los datos deberán ser coherentes entre sí y permitir comprobar el comportamiento de los estados derivados definidos en este documento.

### 51.1. Cantidad de registros

El seed deberá contener:

* **3 Clientes**;
* **7 Cotizaciones**;
* **5 Obras**;
* **3 Facturas**;
* **2 Pagos**.

Estas cantidades responden a la cantidad mínima necesaria para representar todos los estados relevantes del sistema.

### 51.2. Clientes

Se crearán 3 Clientes.

Los nombres, CUIT/CUIL y datos de contacto podrán definirse libremente siempre que sean realistas, únicos y respeten las validaciones establecidas.

Las 7 Cotizaciones deberán distribuirse entre estos Clientes.

No es necesario que todos los Clientes tengan la misma cantidad de Cotizaciones.

### 51.3. Cotizaciones

Se crearán 7 Cotizaciones.

Deberán distribuirse de la siguiente manera:

* 5 Cotizaciones en estado `Aceptada`;
* 1 Cotización en estado `Presentada`;
* 1 Cotización en estado `Rechazada`.

Las 5 Cotizaciones `Aceptadas` deberán originar exactamente las 5 Obras del seed.

Las Cotizaciones `Presentada` y `Rechazada` no deberán tener Obras asociadas.

Cada Obra deberá originarse en una Cotización `Aceptada` diferente.

Siempre que resulte posible sin aumentar la cantidad de registros, las Cotizaciones deberán aprovecharse para representar variedad entre los tipos definidos:

* `Presupuesto`;
* `Licitación pública`;
* `Licitación privada`;
* `Concurso de precios`;
* `Compra directa`.

Los campos `numero_contratacion` deberán respetar su obligatoriedad según el tipo de Cotización.

Los códigos de Cotización deberán respetar el mecanismo automático definido para el sistema.

### 51.4. Obras

Se crearán exactamente 5 Obras.

Cada una deberá representar uno de los cinco estados de ejecución posibles:

* 1 Obra `Pendiente`;
* 1 Obra `En ejecución`;
* 1 Obra `Finalizada`;
* 1 Obra `Suspendida`;
* 1 Obra `Cancelada`.

Las fechas y campos condicionales deberán respetar las reglas correspondientes a cada estado.

En particular:

* la Obra `Pendiente` no requerirá `fecha_inicio` ni `fecha_fin`;
* la Obra `En ejecución` deberá tener `fecha_inicio`;
* la Obra `Finalizada` deberá tener `fecha_inicio` y `fecha_fin`;
* la Obra `Suspendida` deberá tener `fecha_inicio` y `motivo_estado`;
* la Obra `Cancelada` deberá tener `motivo_estado`.

Las cinco Obras deberán utilizar títulos coherentes con trabajos eléctricos de baja y media tensión y alumbrado público.

Podrán utilizarse, por ejemplo, combinaciones relacionadas con:

* ampliación de redes eléctricas de baja tensión;
* renovación o instalación de alumbrado público;
* extensión o adecuación de redes de media tensión;
* obras combinadas de baja tensión y alumbrado público.

Los nombres concretos podrán definirse libremente siempre que resulten realistas y coherentes con el dominio del sistema.

### 51.5. Distribución de estados económicos de Obra

Las 5 Obras deberán distribuirse de forma que el seed permita visualizar todos los estados derivados de facturación y cobro.

Deberán aparecer al menos una vez los siguientes estados de facturación:

* `Sin facturar`;
* `Facturada parcialmente`;
* `Facturada totalmente`.

También deberán aparecer al menos una vez los siguientes estados de cobro:

* `Adeudada`;
* `Pagada parcialmente`;
* `Pagada`.

Para conseguir esta cobertura con la cantidad mínima de Facturas y Pagos, se utilizará la siguiente estructura conceptual:

#### Obra 1

Estado de ejecución:

`Pendiente`

Situación económica:

* `Sin facturar`;
* `Adeudada`.

No deberá tener Facturas ni Pagos asociados.

#### Obra 2

Estado de ejecución:

`En ejecución`

Situación económica:

* `Facturada parcialmente`;
* `Pagada parcialmente`.

Deberá tener una Factura cuyo importe sea menor que `monto_contratado`.

Dicha Factura deberá tener su Pago correspondiente.

Como el importe total cobrado será mayor que cero pero menor que `monto_contratado`, el estado global de cobro resultará `Pagada parcialmente`.

#### Obra 3

Estado de ejecución:

`Finalizada`

Situación económica:

* `Facturada totalmente`;
* `Pagada`.

Deberá tener una Factura cuyo importe coincida exactamente con `monto_contratado`.

Dicha Factura deberá tener su Pago correspondiente por el mismo importe.

Por lo tanto:

`total_facturado = monto_contratado`

y:

`total_cobrado = monto_contratado`

#### Obra 4

Estado de ejecución:

`Suspendida`

Situación económica:

* `Facturada parcialmente`;
* `Adeudada`.

Deberá tener una Factura cuyo importe sea menor que `monto_contratado`.

Esta Factura no deberá tener ningún Pago asociado.

De esta manera, la Factura permitirá representar también el estado individual:

`Pendiente`

#### Obra 5

Estado de ejecución:

`Cancelada`

Situación económica:

* `Sin facturar`;
* `Adeudada`.

No deberá tener Facturas ni Pagos asociados.

### 51.6. Facturas

Se crearán exactamente 3 Facturas.

Deberán distribuirse de la siguiente manera:

* 1 Factura parcial correspondiente a la Obra `En ejecución`, con Pago asociado;
* 1 Factura total correspondiente a la Obra `Finalizada`, con Pago asociado;
* 1 Factura parcial correspondiente a la Obra `Suspendida`, sin Pago asociado.

Esta distribución deberá permitir visualizar simultáneamente los dos estados individuales posibles de Factura:

* `Pagada`;
* `Pendiente`.

Los importes deberán respetar en todos los casos:

* `importe > 0`;
* la suma de Facturas de una Obra no podrá superar `monto_contratado`.

El número de cada Factura deberá ser único.

### 51.7. Pagos

Se crearán exactamente 2 Pagos.

Los Pagos deberán corresponder a:

* la Factura parcial de la Obra `En ejecución`;
* la Factura total de la Obra `Finalizada`.

Cada Pago deberá:

* corresponder a una Factura distinta;
* utilizar una Factura que todavía no posea otro Pago;
* tener un importe exactamente igual al importe de su Factura;
* respetar las reglas de `fecha_pago`;
* utilizar uno de los medios de Pago permitidos.

Siempre que resulte posible, los dos registros deberán utilizar medios de Pago diferentes para aportar variedad a los datos de prueba.

No será necesario crear un tercer Pago, ya que no permitiría representar un estado adicional del sistema y eliminaría el único caso de Factura `Pendiente`.

### 51.8. Montos de referencia

Los montos concretos podrán definirse libremente siempre que respeten las relaciones necesarias para producir los estados establecidos.

Como criterio de ejemplo, podrán utilizarse valores equivalentes a:

* Obra `Pendiente`: monto contratado 1.000.000;
* Obra `En ejecución`: monto contratado 2.000.000 y Factura de 800.000;
* Obra `Finalizada`: monto contratado 3.000.000 y Factura de 3.000.000;
* Obra `Suspendida`: monto contratado 1.500.000 y Factura de 600.000;
* Obra `Cancelada`: monto contratado 2.500.000.

Los valores definitivos podrán ajustarse durante la creación del `seed.sql` siempre que produzcan exactamente los mismos estados y respeten todas las reglas de negocio.

### 51.9. Estados que deben quedar verificables

Después de ejecutar `seed.sql`, deberá ser posible comprobar directamente en el sistema:

#### Cotización

* `Presentada`;
* `Aceptada`;
* `Rechazada`.

#### Obra — estado de ejecución

* `Pendiente`;
* `En ejecución`;
* `Finalizada`;
* `Suspendida`;
* `Cancelada`.

#### Obra — estado de facturación

* `Sin facturar`;
* `Facturada parcialmente`;
* `Facturada totalmente`.

#### Obra — estado de cobro

* `Adeudada`;
* `Pagada parcialmente`;
* `Pagada`.

#### Factura — estado de Pago

* `Pendiente`;
* `Pagada`.

Los estados económicos deberán resultar de los cálculos definidos en este documento y no deberán insertarse manualmente como datos almacenados.

### 51.10. Criterio de implementación

Codex deberá generar `seed.sql` respetando esta estructura y podrá elegir libremente:

* nombres de Clientes;
* CUIT/CUIL válidos y únicos;
* datos de contacto;
* títulos concretos de Cotizaciones;
* títulos concretos de Obras dentro del dominio eléctrico definido;
* fechas coherentes;
* números de contratación;
* números de Factura;
* datos de documentos contractuales;
* medios de Pago;
* observaciones;
* montos concretos cuando no estén fijados expresamente.

Estas elecciones no deberán alterar:

* la cantidad de registros definida;
* las relaciones establecidas;
* la cobertura de estados requerida;
* las reglas de negocio;
* la coherencia económica entre Obra, Factura y Pago.

El seed deberá poder ejecutarse sobre una base creada mediante `schema.sql` y dejar un conjunto de datos coherente, reproducible y útil tanto para pruebas como para la presentación del sistema.

## 52. Decisiones aprobadas para la implementación inicial

Las siguientes decisiones completan los aspectos de implementación e interfaz que permanecían abiertos:

* se implementará el sistema completo, incluyendo un Dashboard básico posterior a los cinco módulos CRUD;
* el Dashboard consumirá los recursos REST existentes y no incorporará nuevas reglas de negocio ni un endpoint específico;
* las altas y modificaciones utilizarán vistas de formulario separadas de los listados;
* Pinia se organizará mediante un store por recurso;
* la interfaz utilizará una identidad visual industrial sobria, con azul petróleo, gris hormigón y acento ámbar;
* los importes se presentarán visualmente con símbolo `$` y formato numérico argentino, sin incorporar moneda al modelo de datos;
* los listados se ordenarán por identificador descendente, mostrando primero los registros más recientes;
* Axios obtendrá la URL base de la API mediante la variable de entorno `VITE_API_URL`;
* `frontend/.env.example` documentará dicha variable sin contener configuración sensible;
* se incluirán pruebas automatizadas completas del backend utilizando `unittest` de la biblioteca estándar, sin agregar una dependencia de testing adicional;
* `README.md` conservará la consigna original y se ampliará con la guía de instalación, configuración, ejecución y pruebas requerida para reproducir el proyecto.
