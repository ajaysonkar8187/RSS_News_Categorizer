import streamlit as st
import pandas as pd
from feed_parser import parse_feeds
import time
import json



# Initialize session state
if 'news_df' not in st.session_state:
    st.session_state.news_df = pd.DataFrame()

def update_news():
    with st.spinner('Fetching and categorizing news articles...'):
        # Get new articles
        new_df = parse_feeds()
        
        if not st.session_state.news_df.empty:
            # Combine with existing articles, drop duplicates
            st.session_state.news_df = pd.concat([st.session_state.news_df, new_df]).drop_duplicates(subset=['title', 'source_url'])
        else:
            st.session_state.news_df = new_df
        
        # Save to JSON
        st.session_state.news_df.to_json('news_data.json', orient='records')

# Streamlit app
st.title('RSS News Categorizer')

# Update button
if st.button('Update News'):
    update_news()

# Display news if available
if not st.session_state.news_df.empty:
    # Display statistics
    st.subheader('Category Statistics')
    category_counts = st.session_state.news_df['category'].value_counts()
    st.bar_chart(category_counts)
    
    # Display articles by category
    st.subheader('News Articles by Category')
    categories = ['terrorism_protest_unrest', 'positive_uplifting', 'natural_disasters', 'others']
    
    for category in categories:
        with st.expander(f"{category.replace('_', ' ').title()} ({len(st.session_state.news_df[st.session_state.news_df['category'] == category])})"):
            category_df = st.session_state.news_df[st.session_state.news_df['category'] == category]
            for _, row in category_df.iterrows():
                st.markdown(f"**{row['title']}**")
                st.markdown(f"*Source: {row['source']}*")
                st.markdown(f"[Read More]({row['source_url']})")
                st.markdown("---")
else:
    st.info('Click "Update News" to fetch and categorize news articles.')