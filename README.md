# BudgetLens

## Descripción

**BudgetLens** es una aplicación diseñada para proporcionar análisis financieros y recomendaciones basadas en datos de ingresos y gastos. La aplicación utiliza el modelo GPT de OpenAI para generar consejos y recomendaciones personalizadas en función del contexto económico de los usuarios. Dependiendo del tipo de usuario configurado en la base de datos, algunos usuarios tendrán acceso a recomendaciones detalladas, mientras que otros verán un mensaje invitándolos a adquirir acceso a funciones avanzadas.

---

## Tabla de Contenidos

1. [Instalación](#instalación)
2. [Configuración](#configuración)
3. [Estructura del Proyecto](#estructura-del-proyecto)
4. [Iniciar la Aplicación](#iniciar-la-aplicación)
5. [Endpoints Principales](#endpoints-principales)
6. [Ejemplo de Uso](#ejemplo-de-uso)
7. [Contribuciones](#contribuciones)
8. [Licencia](#licencia)

---

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/LargoLujan/budgetlens
   ```

2. Accede al directorio del proyecto:
   ```bash
   cd BudgetLens
   ```

3. Crea un entorno virtual para el proyecto:
   ```bash
   python -m venv env
   ```

4. Activa el entorno virtual:
   - En **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - En **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```

5. Instala las dependencias del proyecto:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuración

### Variables de Entorno

Este proyecto utiliza **dotenv** para la gestión de variables de entorno, incluida la clave de API de OpenAI.

1. Crea un archivo `.env` en la carpeta `data` y asegúrate de incluir la clave API de OpenAI y otros valores requeridos en el siguiente formato:

   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

2. El archivo `.env` se cargará automáticamente al iniciar la aplicación, permitiendo el uso seguro de las variables de entorno.

---

## Estructura del Proyecto

La estructura de tu proyecto es la siguiente:

```plaintext
BudgetLens/
├── config/
│   └── settings.py                # Configuración general del proyecto
├── data/
│   └── .env                       # Archivo de variables de entorno
├── src/
│   ├── api/
│   │   ├── endpoints.py           # Endpoints de la API
│   │   └── main.py                # Archivo principal para iniciar la aplicación
│   ├── models/
│   │   ├── data_processing.py     # Lógica de procesamiento de datos
│   │   └── recommendation.py      # Lógica para recomendaciones basadas en datos financieros
│   └── utils/
│       ├── config_loader.py       # Carga de configuración y claves API
│       ├── data_validation.py     # Validaciones de datos
│       ├── gpt_recommender.py     # Funciones para conectar con GPT
│       ├── plot_analysis.py       # Análisis de gráficos financieros
│       ├── prepare_context.py     # Preparación de contexto para recomendaciones
│       └── user_utils.py          # Utilidades para gestión de roles de usuario
└── tests/
    └── env/                       # Entorno de pruebas
└── README.md
└── requirements.txt
```

---

## Iniciar la Aplicación

Para ejecutar la aplicación en modo de desarrollo con `Uvicorn`, asegúrate de estar en la raíz del proyecto y de que el entorno virtual esté activado. Luego, ejecuta:

```bash
uvicorn src.api.main:app --reload
```

Esto iniciará la aplicación en `http://127.0.0.1:8000`, y podrás acceder a la documentación interactiva en `http://127.0.0.1:8000/docs`.

---

## Endpoints Principales

### 1. `/recommendation`
   - **Método**: GET
   - **Descripción**: Genera recomendaciones financieras basadas en los datos de ingresos y gastos del usuario.
   - **Acceso**: Depende del tipo de usuario registrado en la base de datos. Si el usuario tiene permisos, se proporciona una recomendación de GPT; de lo contrario, se devuelve una URL para obtener una suscripción o producto de recomendación.

---

## Ejemplo de Uso

### Endpoint `/recommendation`

#### Solicitud
   ```http
   GET /recommendation
   ```

#### Respuesta
   ```json
   {
     "message": "Se recomienda reducir gastos en X categoría para mejorar la rentabilidad."
   }
   ```

### Caso sin Permiso para Recomendación
   ```json
   {
     "message": "Para acceder a recomendaciones personalizadas, visita [enlace]"
   }
   ```

---

## Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y commitea (`git commit -m 'Añade nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request para revisar tus cambios.

---

## Licencia

Este proyecto está bajo la licencia MIT. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles.
