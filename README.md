# 🤖 **Agente Corporativo de Inteligencia Artificial - Challenge Alura Latam**

Proyecto diseñado como un **Agente Inteligente Corporativo** capaz de procesar documentos internos y responder consultas de los colaboradores en lenguaje natural utilizando la arquitectura **RAG (Retrieval-Augmented Generation)**. El objetivo principal es centralizar la base de conocimiento de la organización y ofrecer respuestas rápidas y confiables con citación de fuentes[cite: 3].

Este desafío forma parte del programa **Oracle Next Education (ONE) - Alura Latam** y abarca desde la recolección y estructuración de documentos hasta la implementación y registro en la nube de **Oracle Cloud Infrastructure (OCI)**[cite: 3].

---

### 🚀 **Funcionalidades Principales**
Nuestra solución corporativa permite gestionar el conocimiento interno de forma eficiente:

* **Ingesta y Extracción de Documentos:** Procesamiento de bases de conocimiento y políticas en formato estructurado (`politicas_tienda.csv`)[cite: 3].
* **Capa de Recuperación RAG:** Búsqueda semántica y contextual para localizar la respuesta exacta en la documentación[cite: 3].
* **Citación de Fuentes:** Transparencia y trazabilidad indicando el documento de origen en cada respuesta entregada[cite: 3].
* **Control de Alucinaciones (Fallback):** Respuesta clara indicando falta de información cuando la consulta no se encuentra en la base de datos[cite: 3].
* **Interfaz Web Conversacional:** Chat funcional desarrollado en Streamlit para facilitar el acceso de los colaboradores[cite: 3].

---

### 🛠️ **Arquitectura y Tecnologías**
* **Lenguaje:** Python 3 🐍[cite: 3]
* **Procesamiento de Datos:** Pandas[cite: 3]
* **Interfaz de Usuario:** Streamlit[cite: 3]
* **Infraestructura Cloud:** Oracle Cloud Infrastructure (OCI Compute / Container Instances) ☁️[cite: 3]
* **Control de Versiones:** Git & GitHub[cite: 3]

---

### 📋 **Etapas del Proyecto (Pipeline Agente IA)**
1. **Colecta y Organización:** Definición del dominio (E-commerce) y preparación de la base de políticas corporativas[cite: 3].
2. **Extracción y Limpieza:** Normalización de datos y adecuación para búsquedas contextuales[cite: 3].
3. **Indexación y Capa RAG:** Lógica de búsqueda semántica por coincidencia de términos e intenciones[cite: 3].
4. **Validación y Fuentes:** Generación de respuestas con verificación de origen y prevención de falsos positivos[cite: 3].
5. **Despliegue y Ejecución en OCI:** Publicación e integración de la solución dentro del entorno de **Oracle Cloud Infrastructure**[cite: 3].

---

### 💻 **Instrucciones para Ejecución Local**
1. Clonar el repositorio:
   ```bash
   git clone [https://github.com/Jebareiro/agente-corporativo-ch-alura.git](https://github.com/Jebareiro/agente-corporativo-ch-alura.git)

