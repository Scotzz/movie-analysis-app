# movie-analysis-app

# 🇷🇺 RUS 

# 🎬 Анализатор фильмов 2025

Интерактивное веб-приложение для анализа и визуализации данных о фильмах 2025 года.

## 📊 О датасете

Датасет содержит информацию о фильмах 2025 года, включая:
- Название фильма
- Язык оригинала
- Рейтинг (vote_average)
- Популярность
- Количество голосов
- Дата выхода
- Описание

**Источник данных:** [Kaggle - Latest Movies Dataset](https://www.kaggle.com/datasets/praveensoni06/1500-latest-movies-datasets-2025)

## 🚀 Запуск приложения

Приложение развернуто на Streamlit Cloud и доступно по ссылке:
👉 **[https://your-username-movie-analysis-app.streamlit.app/](https://your-username-movie-analysis-app.streamlit.app/)**

## 🛠️ Локальный запуск

1. Клонируйте репозиторий:
```bash
git clone https://github.com/your-username/movie-analysis-app.git
cd movie-analysis-app
```
2. Установите зависимости:
```bash
pip install -r requirements.txt
```
3. Запустите streamlit:
```bash
streamlit run app.py
```


## 📈 Функциональность

    📊 Таблица фильмов - просмотр всех данных с фильтрацией

    📈 Визуализации - графики распределения рейтингов, популярности и т.д.

    🏆 Топ фильмов - рейтинги по разным критериям

    🔧 Фильтры - поиск по названию, языку, рейтингу

## 👨‍💻 Автор

Scotzz

    GitHub: @Scotzz
    tg: @sc0tzz

## 📄 Лицензия

Этот проект распространяется под лицензией MIT. Подробнее см. в файле LICENSE.

# 🇺🇸 ENG

# 🎬 Movie Analyzer 2025

Interactive web application for analyzing and visualizing 2025 movie data.

## 📊 About the Dataset

The dataset contains information about movies from 2025, including:
- Movie title
- Original language
- Rating (vote_average)
- Popularity
- Vote count
- Release date
- Description

**Data Source:** [Kaggle - Latest Movies Dataset](https://www.kaggle.com/datasets/praveensoni06/1500-latest-movies-datasets-2025)

## 🚀 Live Application

The application is deployed on Streamlit Cloud and available at:
👉 **[https://your-username-movie-analysis-app.streamlit.app/](https://your-username-movie-analysis-app.streamlit.app/)**

## 🛠️ Local Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/movie-analysis-app.git
cd movie-analysis-app

    Install dependencies:

bash

pip install -r requirements.txt

    Run the application:

bash

streamlit run app.py

📈 Features

    📊 Movies Table - View all data with filtering capabilities

    📈 Visualizations - Charts showing rating distributions, popularity, etc.

    🏆 Top Movies - Rankings based on different criteria

    🔧 Filters - Search by title, language, rating

    🌍 Multi-language - Support for English and Russian interfaces

🎯 Key Functionality
Data Analysis

    Interactive data table with sorting and filtering

    Statistical overview with key metrics

    Real-time data filtering

Visualizations

    Rating distribution histogram

    Popularity vs Rating scatter plot

    Language distribution pie chart

    Votes by language bar chart

Top Lists

    Top 10 movies by popularity

    Top 10 movies by rating

    Top 10 movies by vote count

👨‍💻 Author

Scotzz

    GitHub: @Scotzz

    Telegram: @sc0tzz

🛠️ Technologies Used

    Streamlit - Web application framework

    Pandas - Data processing and analysis

    Plotly - Interactive data visualization

    Python - Main programming language

## 3. .gitignore
```gitignore
# Streamlit
.streamlit/

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual Environment
venv/
env/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Data files (опционально, если данные большие)
*.csv
*.json
*.xlsx
