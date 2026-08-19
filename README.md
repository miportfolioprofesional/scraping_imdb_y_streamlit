
# 🎥 IMDb Top 250 Scraper with Streamlit

Welcome to the **IMDb Top 250 Scraper**! This app lets you extract information from the top 250 movies according to IMDb and view it in a user-friendly way. Plus, you can download the extracted data in an Excel file 📊.

## 📋 Description

This web application, developed with [Streamlit](https://streamlit.io/),allows users to enter the URL of the IMDb Top 250 movies list and get detailed information about each movie, including:

- **Movie Title** 🎬
- **Release Year** 📅
- **Duration** ⏱️
- **Rating** ⭐

## 🚀 Functionality

1. **Data Scraping**: Uses Selenium with an undetectable ChromeDriver to navigate the IMDb page and extract key information about the movies.
2. **Sorting and Organization**: The extracted data is sorted into categories like 'Year', 'Duration', and 'Rating'.
3. **User-Friendly Interface**: The app uses Streamlit to provide a simple and modern user interface.
4. **Export to Excel**: Users can download the extracted information in Excel format for further analysis or use.

## 📚 Information Source

The data is extracted directly from the page [IMDb Top 250](https://www.imdb.com/chart/top/?ref_=nv_mv_250), one of the most popular and reliable sources for movie information.

## 🎯 Purpose

The purpose of this application is to provide an easy-to-use tool for filmmakers, data analysts, and movie enthusiasts who want to explore and analyze the best movies according to IMDb. Whether for research, trend analysis, or just out of curiosity, this tool makes accessing high-quality structured data easy.

## 🛠️ How to Use

1. **Clone the repository**:
    ```bash
    git clone https://github.com/tu_usuario/scraping_imdb_y_streamlit.git
    cd scraping_imdb_y_streamlit
    ```

2. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the app**:
    ```bash
    streamlit run app.py
    ```

4. **Enter the IMDb URL** in the Streamlit interface and press the "Scrape" button.

## 📦 Requirements

- Python 3.7+
- [Streamlit](https://streamlit.io/)
- [Selenium](https://www.selenium.dev/)
- [Undetected ChromeDriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver)

## 📧 Contact

For more information, issues, or suggestions, please contact [matiasjavierendrek@gmail.com](mailto:tuemail@example.com).

Enjoy exploring the wonderful world of cinema with this tool! 🎉🎬
