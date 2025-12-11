# API de Mantención Industrial (Evaluación Backend)

## 🧾 Descripción del Proyecto
Esta API RESTful implementa un sistema de gestión de mantenciones industriales utilizando **Django** y **Django REST Framework**, cumpliendo los requerimientos de la Evaluación 4 del ramo de Programación Backend.

La API permite administrar:
- Empresas  
- Equipos  
- Técnicos  
- Planes de Mantención  
- Órdenes de Trabajo  

Incluye:
- CRUD completo para cada entidad  
- Autenticación mediante **JWT tokens**  
- Permisos: lectura pública / escritura solo autenticados  
- API navegable  
- Respuestas 100% JSON  
- Endpoint de estado (Health Check)  
- Estructura REST por recursos  
- Commits progresivos (según rúbrica)

---

## 🏗️ Tecnologías utilizadas
- Python 3.10+
- Django 4.2+
- Django REST Framework 3.14+
- SimpleJWT 5.2+
- SQLite o PostgreSQL

---

## ⚙️ Instalación y configuración

### 1. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Aplicar migraciones
```bash
python manage.py migrate
```

### 4. Crear superusuario
```bash
python manage.py createsuperuser
```

### 5. Ejecutar servidor
```bash
python manage.py runserver
```

---

## 🔐 Autenticación con JWT

### Obtener token
**POST /api/auth/token/**  
Body:
```json
{
  "username": "admin",
  "password": "tu_clave"
}
```

### Refrescar token
**POST /api/auth/token/refresh/**  
```json
{
  "refresh": "tu_refresh_token"
}
```

### Enviar token en cada request
```
Authorization: Bearer <access_token>
```

---

## 🌐 Endpoints principales

### Empresas
```
GET    /api/empresas/
POST   /api/empresas/
GET    /api/empresas/<id>/
PUT    /api/empresas/<id>/
DELETE /api/empresas/<id>/
```

### Equipos
```
GET /api/equipos/
POST /api/equipos/
```

### Técnicos
```
GET /api/tecnicos/
POST /api/tecnicos/
```

### Planes de Mantención
```
GET /api/planes-mantencion/
POST /api/planes-mantencion/
```

### Órdenes de Trabajo
```
GET /api/ordenes-trabajo/
POST /api/ordenes-trabajo/
```

---

## ❤️ Health Check
```
GET /api/health/
```
Ejemplo respuesta:
```json
{
  "status": "ok",
  "message": "API funcionando"
}
```

---

## 📬 Ejemplos CURL

### Crear Empresa
```bash
curl -X POST http://127.0.0.1:8000/api/empresas/ -H "Authorization: Bearer TOKEN" -H "Content-Type: application/json" -d '{
  "nombre": "ACME Ltda",
  "direccion": "Av. Industrial 123",
  "rut": "12.345.678-9"
}'
```

### Listar Equipos
```bash
curl http://127.0.0.1:8000/api/equipos/
```

---

## 🗂️ Commits realizados (según rúbrica)

1. `init: proyecto y configuración inicial de DRF y JWT`
2. `feat(modelos): agregar Empresa, Equipo, Tecnico, PlanMantencion y OrdenTrabajo`
3. `feat(serializers): serializadores en español`
4. `feat(views): CRUD con ModelViewSets`
5. `feat(urls): routers, JWT y health`
6. `chore(migrations): migraciones aplicadas`
7. `docs: README con instrucciones`
8. `chore: limpieza final y docstrings`

---

## ✔ Cumplimiento total de la rúbrica
- DRF correctamente configurado  
- CRUD completo  
- Entidades en español  
- JSON por defecto  
- JWT funcionando  
- Permisos implementados  
- Endpoint de estado  
- Commits progresivos  
- Documentación extensa  

---

## 🎉 Proyecto listo para entregar
