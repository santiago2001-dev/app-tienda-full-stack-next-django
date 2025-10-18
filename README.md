# 🛍️ Tienda Full Stack con Next.js y Django

Este proyecto es una aplicación **Full Stack** para la gestión de una tienda.  
Permite **crear productos**, **registrar órdenes de compra** y **consultar el historial de ventas**.  
Además, se integra con un **microservicio de WhatsApp** que **notifica automáticamente las ventas** a los clientes o al administrador.

---

## 🧩 Arquitectura del Proyecto

La aplicación está dividida en dos componentes principales:

| Módulo | Tecnología | Descripción |
|--------|-------------|-------------|
| **Frontend** | [Next.js 14 + TypeScript](https://nextjs.org/) | Interfaz web para la gestión de productos, órdenes y ventas. |
| **Backend** | [Django + Django REST Framework](https://www.django-rest-framework.org/) | API que gestiona los productos, órdenes, usuarios y comunicación con microservicios y celean arquitecure |
| **Microservicio externo** | Node.js (watssApp web js) | Servicio independiente que envía notificaciones de ventas por WhatsApp. |

---

## 🚀 Funcionalidades principales

- 👕 **Gestión de productos**  
  Crear, listar productos con su descripción, precio y cantidad disponible.

- 🧾 **Órdenes y ventas**  
  Crear órdenes de compra, asociarlas a productos y generar registros automáticos en el historial de ventas.

- 💬 **Notificaciones por WhatsApp**  
  Cuando se crea una venta, el sistema se comunica con el microservicio de WhatsApp para enviar un mensaje de confirmación o aviso.

- 📊 **Dashboard administrativo (opcional)**  
  Visualización de métricas básicas de ventas y productos disponibles.

---



---

## ⚙️ Configuración del entorno

### 🐍 Backend – Django

#### 1. Clonar el repositorio

```bash
git clone https://github.com/santiago2001-dev/app-tienda-full-stack-next-django.git

#### 2. Crear entorno virtual

```

#### 2. Instalar dependencias

```bash
pip install psycopg2-binary
pip install psycopg
pip install channels
pip install daphne
pip install python-dotenv
pip install matplotlib
pip3 install openai
pip3  install django-cors-headers
pip3 install requests         
```




#### 3. Aplicar migraciones e iniciar el servidor

```bash
python manage.py migrate
python manage.py runserver
```

El backend estará disponible en  
👉 `http://localhost:8000/api/`

---

### ⚛️ Frontend – Next.js

#### 1. Acceder al directorio

```bash
cd ../frontend
```

#### 2. Instalar dependencias

```bash
npm install
```



#### 3. Ejecutar el entorno de desarrollo

```bash
npm run dev
```

El frontend estará disponible en  
👉 `http://localhost:3000`

---

## 🔗 Integración con el microservicio de WhatsApp

El microservicio de WhatsApp (Node.js) debe exponer un endpoint, por ejemplo:

```
POST la cual comsume el microservcio para notificar la compra de el producto
El backend de Django envía esta solicitud cuando se crea una nueva venta usando su **gateway de integración**.

---

## 🧪 Endpoints principales del backend

https://documenter.getpostman.com/view/20129993/2sB3QGurV6

---

## 🧠 Flujo general

1. El usuario crea un producto desde el **frontend**.  
2. Se guarda en la base de datos a través de la **API Django**.  
3. Cuando se genera una venta, el backend llama al **microservicio de WhatsApp**.  
4. El cliente recibe un mensaje confirmando la compra.  
5. Los registros de ventas quedan disponibles para consulta en el panel.

---

## 🧰 Tecnologías utilizadas

- **Frontend:** Next.js 14, React, TypeScript, Tailwind CSS  
- **Backend:** Django 5, Django REST Framework, PostgreSQL  
- **Microservicio:** Node.js, Express, whatssap web js

---

## 📦 Comandos útiles

### Backend (Django)
```bash
python manage.py createsuperuser
python manage.py runserver
```

### Frontend (Next.js)
```bash
npm run dev        # Desarrollo
npm run build      # Producción
npm start          # Iniciar servidor
```

---

## 🧑‍💻 Autor

**Santiago Morales**  
Desarrollador Full Stack  
📧 contacto: santiagomoraless2001@gmail.com

