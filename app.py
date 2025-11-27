import streamlit as st
import pandas as pd
import os
import plotly.express as px

# Настройка многоязычности
if 'language' not in st.session_state:
    st.session_state.language = 'ru'

def get_text(language):
    texts = {
        'ru': {
            'title': "🎬 Анализатор фильмов 2025",
            'filters': "🔧 Фильтры",
            'search_title': "Поиск по названию:",
            'select_language': "Выберите языки:",
            'rating_filter': "Рейтинг (vote_average):",
            'tabs': ["📊 Таблица фильмов", "📈 Визуализации", "🏆 Топ фильмов", "ℹ️ О проекте"],
            'table_title': "📊 Таблица фильмов",
            'stats_title': "📋 Статистика",
            'total_movies': "Всего фильмов",
            'unique_languages': "Уникальных языков",
            'avg_rating': "Средний рейтинг",
            'median_rating': "Медианный рейтинг",
            'avg_popularity': "Средняя популярность",
            'total_votes': "Общее количество голосов",
            'max_rating': "Макс. рейтинг",
            'max_popularity': "Макс. популярность",
            'no_data_stats': "Нет данных для статистики с текущими фильтрами",
            'visualizations': "📈 Визуализации",
            'rating_distribution': "Распределение рейтингов",
            'top_languages': "Топ языков фильмов",
            'popularity_vs_rating': "Популярность vs Рейтинг",
            'votes_by_language': "Общее количество голосов по языкам",
            'no_data_visualizations': "Нет данных для статистики с текущими фильтрами",
            'top_movies': "🏆 Топ фильмов",
            'top_popularity': "📈 Топ по популярности",
            'top_rating': "⭐ Топ по рейтингу",
            'top_votes': "🗳️ Топ по голосам",
            'no_data_tops': "Нет данных для отображения топов с текущими фильтрами",
            'about': "ℹ️ О проекте",
            'about_title': "🎬 Анализатор фильмов 2025",
            'about_description': "**Анализатор фильмов** - это интерактивное веб-приложение для анализа и визуализации данных о фильмах 2025 года.",
            'features_title': "### 📊 Основные возможности:",
            'features': [
                "**Просмотр данных** - полная таблица с информацией о фильмах",
                "**Фильтрация** - поиск по названию, языку и рейтингу",
                "**Визуализация** - графики и диаграммы для анализа данных",
                "**Топ-листы** - рейтинги фильмов по разным критериям"
            ],
            'metrics_title': "### 📈 Доступные метрики:",
            'metrics': [
                "**Рейтинг** - средняя оценка зрителей",
                "**Популярность** - индекс популярности фильма",
                "**Количество голосов** - сколько людей оценило фильм",
                "**Язык оригинала** - язык, на котором снят фильм"
            ],
            'tech_title': "### 🛠️ Технологии:",
            'tech': [
                "**Streamlit** - фреймворк для создания веб-приложений",
                "**Pandas** - обработка и анализ данных",
                "**Plotly** - интерактивная визуализация данных",
                "**Python** - основной язык программирования"
            ],
            'data_source': "### 📁 Источник данных:",
            'data_description': "Данные загружаются из файла `Latest 2025 movies Datasets.csv`, который должен находиться в той же директории, что и приложение.",
            'author': "**Автор проекта:** Scotzz",
            'file_not_found': "Файл не найден!",
            'file_check': "Убедитесь, что файл 'Latest 2025 movies Datasets.csv' находится в той же папке, что и этот скрипт.",
            'switch_to_english': "🇺🇸 Switch to English",
            'switch_to_russian': "🇷🇺 Переключить на русский"
        },
        'en': {
            'title': "🎬 Movie Analyzer 2025",
            'filters': "🔧 Filters",
            'search_title': "Search by title:",
            'select_language': "Select languages:",
            'rating_filter': "Rating (vote_average):",
            'tabs': ["📊 Movies Table", "📈 Visualizations", "🏆 Top Movies", "ℹ️ About"],
            'table_title': "📊 Movies Table",
            'stats_title': "📋 Statistics",
            'total_movies': "Total movies",
            'unique_languages': "Unique languages",
            'avg_rating': "Average rating",
            'median_rating': "Median rating",
            'avg_popularity': "Average popularity",
            'total_votes': "Total votes",
            'max_rating': "Max rating",
            'max_popularity': "Max popularity",
            'no_data_stats': "No data for statistics with current filters",
            'visualizations': "📈 Visualizations",
            'rating_distribution': "Rating distribution",
            'top_languages': "Top languages",
            'popularity_vs_rating': "Popularity vs Rating",
            'votes_by_language': "Total votes by language",
            'no_data_visualizations': "No data for visualizations with current filters",
            'top_movies': "🏆 Top Movies",
            'top_popularity': "📈 Top by popularity",
            'top_rating': "⭐ Top by rating",
            'top_votes': "🗳️ Top by votes",
            'no_data_tops': "No data to display tops with current filters",
            'about': "ℹ️ About",
            'about_title': "🎬 Movie Analyzer 2025",
            'about_description': "**Movie Analyzer** is an interactive web application for analyzing and visualizing 2025 movie data.",
            'features_title': "### 📊 Main Features:",
            'features': [
                "**Data Viewing** - complete table with movie information",
                "**Filtering** - search by title, language and rating",
                "**Visualization** - charts and diagrams for data analysis",
                "**Top Lists** - movie ratings by different criteria"
            ],
            'metrics_title': "### 📈 Available Metrics:",
            'metrics': [
                "**Rating** - average viewer score",
                "**Popularity** - movie popularity index",
                "**Vote Count** - number of people who rated the movie",
                "**Original Language** - language the movie was filmed in"
            ],
            'tech_title': "### 🛠️ Technologies:",
            'tech': [
                "**Streamlit** - web application framework",
                "**Pandas** - data processing and analysis",
                "**Plotly** - interactive data visualization",
                "**Python** - main programming language"
            ],
            'data_source': "### 📁 Data Source:",
            'data_description': "Data is loaded from the `Latest 2025 movies Datasets.csv` file, which should be in the same directory as the application.",
            'author': "**Author:** Scotzz",
            'file_not_found': "File not found!",
            'file_check': "Make sure the 'Latest 2025 movies Datasets.csv' file is in the same folder as this script.",
            'switch_to_english': "🇺🇸 Switch to English",
            'switch_to_russian': "🇷🇺 Переключить на русский"
        }
    }
    return texts[language]

# Функция для переключения языка
def switch_language():
    if st.session_state.language == 'ru':
        st.session_state.language = 'en'
    else:
        st.session_state.language = 'ru'

# Получаем тексты для текущего языка
text = get_text(st.session_state.language)

st.set_page_config(page_title=text['title'], layout="wide")
st.title(text['title'])

# Кнопка переключения языка в сайдбаре
with st.sidebar:
    if st.session_state.language == 'ru':
        if st.button(text['switch_to_english']):
            switch_language()
            st.rerun()
    else:
        if st.button(text['switch_to_russian']):
            switch_language()
            st.rerun()

# Загрузка данных
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "Latest 2025 movies Datasets.csv")

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    # Боковая панель с фильтрами
    with st.sidebar:
        st.header(text['filters'])
        
        search_title = st.text_input(text['search_title'])
        
        selected_language = st.multiselect(
            text['select_language'],
            options=df['original_language'].unique(),
            default=['en']
        )

        # Фильтр по рейтингу
        min_rating, max_rating = st.slider(
            text['rating_filter'],
            min_value=float(df['vote_average'].min()),
            max_value=float(df['vote_average'].max()),
            value=(0.0, 10.0),
            format="%.1f ⭐"
        )

    # Применяем фильтры
    filtered_df = df.copy()

    if selected_language:
        filtered_df = df[df['original_language'].isin(selected_language)]
    else:
        filtered_df = df

    filtered_df = filtered_df[
        (filtered_df['vote_average'] >= min_rating) & 
        (filtered_df['vote_average'] <= max_rating)
    ]
    
    if search_title:
        filtered_df = filtered_df[filtered_df['title'].str.contains(search_title, case=False, na=False)]

    # Создаем вкладки
    tab1, tab2, tab3, tab4 = st.tabs(text['tabs'])
    
    with tab1:
        col1, col2 = st.columns([2, 1])
        with col1:  
            st.header(text['table_title'])
            st.dataframe(
                filtered_df,
                use_container_width=True,
                height=600,
                hide_index=True,
                column_config={
                    "title": "Title" if st.session_state.language == 'en' else "Название",
                    "original_language": "Language" if st.session_state.language == 'en' else "Язык",
                    "vote_average": st.column_config.NumberColumn(
                        "Rating" if st.session_state.language == 'en' else "Рейтинг",
                        format="%.1f ⭐"
                    ),
                    "release_date": "Release Date" if st.session_state.language == 'en' else "Дата выхода",
                    "popularity": st.column_config.NumberColumn(
                        "Popularity" if st.session_state.language == 'en' else "Популярность",
                        format="%.0f"
                    ),
                    "vote_count": "Vote Count" if st.session_state.language == 'en' else "Кол-во голосов",
                    "overview": "Overview" if st.session_state.language == 'en' else "Описание"
                }
            )

        with col2:
            st.header(text['stats_title'])
        
            if len(filtered_df) > 0:
                col1, col2 = st.columns(2)
                with col1:
                    st.metric(text['total_movies'], len(filtered_df))
                    st.metric(text['unique_languages'], filtered_df['original_language'].nunique())
                    st.metric(text['avg_rating'], f"{filtered_df['vote_average'].mean():.2f}")
                    st.metric(text['median_rating'], f"{filtered_df['vote_average'].median():.2f}")

                with col2:
                    st.metric(text['avg_popularity'], f"{filtered_df['popularity'].mean():.2f}")
                    st.metric(text['total_votes'], f"{filtered_df['vote_count'].sum():,}")
                    st.metric(text['max_rating'], f"{filtered_df['vote_average'].max():.2f}")
                    st.metric(text['max_popularity'], f"{filtered_df['popularity'].max():.2f}")
            else:
                st.warning(text['no_data_stats'])

    with tab2:
        st.header(text['visualizations'])

        if len(filtered_df) > 0:
            col1, col2 = st.columns(2)
            with col1:
                # Распределение рейтингов
                fig1 = px.histogram(
                    filtered_df, 
                    x='vote_average', 
                    title=text['rating_distribution'],
                    nbins=20,
                    color_discrete_sequence=['#FF4B4B']
                )
                fig1.update_layout(
                    xaxis_title="Rating" if st.session_state.language == 'en' else "Рейтинг", 
                    yaxis_title="Number of Movies" if st.session_state.language == 'en' else "Количество фильмов"
                )
                st.plotly_chart(fig1, use_container_width=True)

                # Соотношение языков
                lang_counts = filtered_df['original_language'].value_counts().head(10)
                fig3 = px.pie(
                    values=lang_counts.values,
                    names=lang_counts.index, 
                    title=text['top_languages']
                )
                st.plotly_chart(fig3, use_container_width=True)

            with col2:
                # Популярность vs Рейтинг
                fig2 = px.scatter(
                    filtered_df,
                    x='vote_average',
                    y='popularity',
                    size='vote_count',
                    color='original_language',
                    hover_name='title',
                    title=text['popularity_vs_rating'],
                    size_max=20
                )
                fig2.update_layout(
                    xaxis_title="Rating" if st.session_state.language == 'en' else "Рейтинг", 
                    yaxis_title="Popularity" if st.session_state.language == 'en' else "Популярность"
                )
                st.plotly_chart(fig2, use_container_width=True)
                
                # Количество голосов по языкам
                votes_by_lang = filtered_df.groupby('original_language')['vote_count'].sum().nlargest(10)
                fig4 = px.bar(
                    x=votes_by_lang.index,
                    y=votes_by_lang.values,
                    title=text['votes_by_language'],
                    color=votes_by_lang.values,
                    color_continuous_scale='viridis'
                )
                fig4.update_layout(
                    xaxis_title="Language" if st.session_state.language == 'en' else "Язык", 
                    yaxis_title="Vote Count" if st.session_state.language == 'en' else "Количество голосов"
                )
                st.plotly_chart(fig4, use_container_width=True)
        else:
            st.warning(text['no_data_visualizations'])

    with tab3:
        st.header(text['top_movies'])
        if len(filtered_df) > 0:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.subheader(text['top_popularity'])
                top_popular = filtered_df.nlargest(10, 'popularity')[['title', 'popularity', 'vote_average', 'vote_count']]
                st.dataframe(top_popular, use_container_width=True)
            
            with col2:
                st.subheader(text['top_rating'])
                top_rated = filtered_df.nlargest(10, 'vote_average')[['title', 'vote_average', 'popularity', 'vote_count']]
                st.dataframe(top_rated, use_container_width=True)
            
            with col3:
                st.subheader(text['top_votes'])
                top_votes = filtered_df.nlargest(10, 'vote_count')[['title', 'vote_count', 'vote_average', 'popularity']]
                st.dataframe(top_votes, use_container_width=True)
        else:
            st.warning(text['no_data_tops'])
            
    with tab4:
        st.header(text['about'])
        
        st.markdown(f"""
        ## {text['about_title']}
        
        {text['about_description']}
        
        {text['features_title']}
        
        """)
        
        for feature in text['features']:
            st.markdown(f"- {feature}")
        
        st.markdown(f"""
        {text['metrics_title']}
        
        """)
        
        for metric in text['metrics']:
            st.markdown(f"- {metric}")
        
        st.markdown(f"""
        {text['tech_title']}
        
        """)
        
        for tech in text['tech']:
            st.markdown(f"- {tech}")
        
        st.markdown(f"""
        {text['data_source']}
        
        {text['data_description']}
        
        {text['author']}
        ---
        Source: https://github.com/Scotzz/movie-analysis-app
        
        """)
        
else:
    st.error(f"{text['file_not_found']} {file_path}")
    st.info(text['file_check'])

