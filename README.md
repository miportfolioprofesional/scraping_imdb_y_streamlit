
# 🎥 IMDb Top 250 Scraper con Streamlit

¡Bienvenido al **IMDb Top 250 Scraper**! Esta aplicación permite extraer información de las 250 mejores películas según IMDb y visualizarla de manera amigable. Además, puedes descargar los datos extraídos en un archivo Excel 📊.

## 📋 Descripción

Esta aplicación web, desarrollada con [Streamlit](https://streamlit.io/), permite a los usuarios introducir la URL de la lista de las 250 mejores películas de IMDb y obtener información detallada de cada película, incluyendo:

- **Título de la película** 🎬
- **Año de lanzamiento** 📅
- **Duración** ⏱️
- **Valoración** ⭐

## 🚀 Funcionalidad

1. **Scraping de Datos**: Utiliza Selenium con un ChromeDriver indetectable para navegar por la página de IMDb y extraer información clave de las películas.
2. **Clasificación y Organización**: Los datos extraídos se clasifican en categorías como 'Año', 'Duración' y 'Valoración'.
3. **Interfaz Amigable**: La aplicación utiliza Streamlit para proporcionar una interfaz de usuario sencilla y moderna.
4. **Exportar a Excel**: Los usuarios pueden descargar la información extraída en formato Excel para su análisis o uso posterior.

## 📚 Fuente de Información

Los datos son extraídos directamente desde la página de [IMDb Top 250](https://www.imdb.com/chart/top/?ref_=nv_mv_250), una de las fuentes más populares y confiables para la información de películas.

## 🎯 Finalidad

La finalidad de esta aplicación es proporcionar una herramienta fácil de usar para cineastas, analistas de datos, y aficionados al cine, que quieran explorar y analizar las mejores películas según IMDb. Ya sea para investigaciones, análisis de tendencias o simplemente por curiosidad, esta herramienta facilita el acceso a datos estructurados de alta calidad.

## 🛠️ Cómo Usar

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/tu_usuario/scraping_imdb_y_streamlit.git
    cd scraping_imdb_y_streamlit
    ```

2. **Instalar las dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Ejecutar la aplicación**:
    ```bash
    streamlit run app.py
    ```

4. **Introducir la URL de IMDb** en la interfaz de Streamlit y presionar el botón "Scrapear".

## 📦 Requerimientos

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [Undetected ChromeDriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

## 📧 Contacto

Para más información, problemas o sugerencias, por favor contacta a [matiasjavierendrek@gmail.com](mailto:tuemail@example.com).

¡Disfruta explorando el maravilloso mundo del cine con esta herramienta! 🎉🎬
