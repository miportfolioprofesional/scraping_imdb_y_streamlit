import streamlit as st
import pandas as pd
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
import random

# Definir los valores únicos para cada categoría
años_unicos = ['1994', '1972', '2008', '1974', '1957', '1993', '2003', '2001', '1966', '2002', '1999', '2010', '1980', '1990', '1975', '2014', '1995', '1946', '1954', '1991', '1998', '1997', '1977', '1985', '2019', '1960', '2000', '2023', '2024', '2006', '1988', '1962', '1942', '2011', '1936', '1968', '1979', '1931', '2012', '1981', '1950', '2018', '1940', '1986', '2009', '2017', '1984', '1964', '2016', '1963', '1952', '1983', '2004', '1992', '1959', '1941', '1944', '1958', '1987', '1971', '1973', '1989', '2007', '1927', '1948', '2020', '1976', '2005', '1965', '2013', '1921', '1961', '2022', '1982', '1939', '2015', '1996', '2021', '1925', '1978', '1926', '1924', '1953', '1949', '1928']
valoraciones_unicas = ['13', '18', 'A', '12', '14', '16', '7', 'PG-13', '(Banned)', 'PG', 'Approved', 'A/i', 'T', '7/i', 'Not Rated']

def classify_entry(entry):
    if entry in años_unicos:
        return 'Año'
    elif re.match(r'\d+h\s*\d*m|\d+m|Apta para mayores', entry):
        return 'Duración'
    elif entry in valoraciones_unicas or re.match(r'\d+', entry):
        return 'Valoración'
    else:
        return 'Desconocido'

def scrape_imdb(url):
    # Configuración del WebDriver
    options = uc.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')

    driver = uc.Chrome(options=options)

    try:
        driver.get(url)
        time.sleep(random.uniform(8, 12))
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'h3.ipc-title__text')))
        titles = driver.find_elements(By.CSS_SELECTOR, 'h3.ipc-title__text')
        movie_titles = [title.text for title in titles]
        df1 = pd.DataFrame(movie_titles, columns=['peliculas'])

        # Extraer los metadatos
        elements = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span.sc-b189961a-8.hCbzGp.cli-title-metadata-item")))
        data = [element.text for element in elements]

        df2 = pd.DataFrame({'Metadata': data})
        df2['Tipo'] = df2['Metadata'].apply(classify_entry)

        df_final = pd.DataFrame({
            'Año': df2[df2['Tipo'] == 'Año']['Metadata'].reset_index(drop=True),
            'Duración': df2[df2['Tipo'] == 'Duración']['Metadata'].reset_index(drop=True),
            'Valoración': df2[df2['Tipo'] == 'Valoración']['Metadata'].reset_index(drop=True)
        })

        df1['titulo'] = df1['peliculas'].str.extract(r'\d+\.\s(.+)$', expand=False)
        df1 = df1.dropna().reset_index(drop=True)
        titulos = df1['titulo'].tolist()

        if len(df_final) == len(titulos):
            df_final['titulo'] = titulos
        else:
            df_final = df_final.iloc[:len(titulos)]
            df_final['titulo'] = titulos

        mejores_peliculas = pd.merge(df1, df_final, on='titulo', how='left')

        return mejores_peliculas

    except Exception as e:
        driver.save_screenshot('error_screenshot.png')
        print(driver.page_source)
        print(e)
        raise

    finally:
        driver.quit()

st.title('IMDb Scraper')
st.write("Introduce la URL de IMDb Top 250 para obtener la información en un archivo Excel.")

url = st.text_input('URL de IMDb')

if st.button('Scrapear'):
    with st.spinner('Scrapeando la página...'):
        try:
            df = scrape_imdb(url)
            st.success('Scraping completado con éxito!')
            st.write(df)
            df.to_excel("mejores_peliculas.xlsx", index=False)
            st.download_button(label="Descargar Excel", data=open("mejores_peliculas.xlsx", "rb"), file_name="mejores_peliculas.xlsx")
        except Exception as e:
            st.error(f"Error durante el scraping: {e}")