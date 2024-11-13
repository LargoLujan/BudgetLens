# BudgetLens

🇪🇸 [Español](#contenido) | 🇬🇧 [English](#contents)

---

---

## Contenido (Español)

1. [Descripción](#descripción)
2. [Tabla de Contenidos](#tabla-de-contenidos)
3. [Instalación](#instalación)
4. [Configuración](#configuración)
5. [Estructura del Proyecto](#estructura-del-proyecto)
6. [Iniciar la Aplicación](#iniciar-la-aplicación)
7. [Endpoints Principales](#endpoints-principales)
8. [Ejemplo de Uso](#ejemplo-de-uso)
9. [Contribuciones](#contribuciones)
10. [Licencia](#licencia)

---

## Descripción

**BudgetLens** es una aplicación diseñada para proporcionar análisis financieros y recomendaciones basadas en datos de ingresos y gastos. La aplicación utiliza el modelo GPT de OpenAI para generar consejos y recomendaciones personalizadas en función del contexto económico de los usuarios. Dependiendo del tipo de usuario configurado en la base de datos, algunos usuarios tendrán acceso a recomendaciones detalladas, mientras que otros verán un mensaje invitándolos a adquirir acceso a funciones avanzadas.

---

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/LargoLujan/BudgetLens
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

---

---

## Contents (English)

1. [Description](#description)
2. [Contents](#contents)
3. [Installation](#installation)
4. [Configuration](#configuration)
5. [Project Structure](#project-structure)
6. [Starting the Application](#starting-the-application)
7. [Key Endpoints](#key-endpoints)
8. [Usage Example](#usage-example)
9. [Contributing](#contributing)
10. [License](#license)

---

## Description

**BudgetLens** is an application designed to provide financial analysis and recommendations based on income and expense data. The app uses OpenAI's GPT model to generate tailored advice and recommendations according to the economic context of users. Depending on the user type configured in the database, some users will have access to detailed recommendations, while others will see a message inviting them to acquire access to advanced features.

---

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/LargoLujan/BudgetLens
   ```

2. Navigate to the project directory:
   ```bash
   cd BudgetLens
   ```

3. Create a virtual environment for the project:
   ```bash
   python -m venv env
   ```

4. Activate the virtual environment:
   - **Windows**:
     ```bash
     .\env\Scripts\activate
     ```
   - **Mac/Linux**:
     ```bash
     source env/bin/activate
     ```

5. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

### Environment Variables

This project uses **dotenv** for managing environment variables, including the OpenAI API key.

1. Create a `.env` file in the `data` folder and include the OpenAI API key and other required values in the following format:

   ```
   OPENAI_API_KEY="your_openai_api_key_here"
   ```

2. The `.env` file will be automatically loaded when starting the application, allowing secure use of environment variables.

---

## Project Structure

Your project structure is as follows:

```plaintext
BudgetLens/
├── config/
│   └── settings.py                # General project configuration
├── data/
│   └── .env                       # Environment variables file
├── src/
│   ├── api/
│   │   ├── endpoints.py           # API endpoints
│   │   └── main.py                # Main file to start the application
│   ├── models/
│   │   ├── data_processing.py     # Data processing logic
│   │   └── recommendation.py      # Financial recommendations logic
│   └── utils/
│       ├── config_loader.py       # Config and API key loader
│       ├── data_validation.py     # Data validation
│       ├── gpt_recommender.py     # GPT connection functions
│       ├── plot_analysis.py       # Financial chart analysis
│       ├── prepare_context.py     # Recommendation context preparation
│       └── user_utils.py          # User role and access utilities
└── tests/
    └── env/                       # Test environment
└── README.md
└── requirements.txt
```

---

## Starting the Application

To run the application in development mode with `Uvicorn`, ensure you’re in the project root and the virtual environment is active. Then, execute:

```bash
uvicorn src.api.main:app --reload
```

This will start the application at `http://127.0.0.1:8000`, and you can access the interactive API documentation at `http://127.0.0.1:8000/docs`.

---

## Key Endpoints

### 1. `/recommendation`
   - **Method**: GET
   - **Description**: Generates financial recommendations based on the user’s income and expense data.
   - **Access**: Access is based on the user type registered in the database. If the user has permission, a GPT-based recommendation is provided; otherwise, a URL is returned directing them to a subscription or product for recommendation access.

---

## Usage Example

### Endpoint `/recommendation`

#### Request
   ```http
   GET /recommendation
   ```

#### Response (User with Access)
   ```json
   {
     "message": "Consider reducing expenses in X category to improve profitability."
   }
   ```

#### Response (User without Access)
   ```json
   {
     "message": "To access personalized recommendations, visit [link]"
   }
   ```

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch for your changes (`git checkout -b feature/new-feature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push your changes (`git push origin feature/new-feature`).
5. Open a Pull Request for review.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
