import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Harshal Panchal's App Showcase",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App title and description
st.title("Harshal Panchal's App Showcase")
st.subheader("Explore the collection of apps built by Harshal Panchal")

# List of apps with their descriptions and links
apps = [
    {
        "name": "VizFlex",
        "description": "An intuitive data visualization tool that allows users to upload CSV files and create various plots.",
        "link": "https://vizflex.streamlit.app/"
    },
    {
        "name": "AnalyzeKit - Because Life's Too Short for Mundane Analysis!",
        "description": "AnalyseKit is a web application designed to provide automated exploratory data analysis (EDA) for CSV datasets. It allows users to quickly understand their dataset by visualizing key insights and statistical summaries.",
        "link": "https://analyzekit.streamlit.app/"
    },
    {
        "name": "Dork's Data Digest - Navigating the Literary Universe to Find Your Perfect Match!",
        "description": "Dork's Data Digest is your ultimate guide to the world of data science literature. Our platform utilizes advanced algorithms to deliver personalized recommendations, ensuring you discover the most relevant and insightful reads. Say goodbye to aimless browsing and let us streamline your journey to becoming a data science aficionado!",
        "link": "https://dorksdataaadigest.streamlit.app/"
    }
    # Add more apps as needed
]

# Display each app with its description and link
for app in apps:
    st.markdown(f"### [{app['name']}]({app['link']})")
    st.markdown(f"*{app['description']}*")

# Footer
st.markdown(
    """
    <div style='text-align: center; padding: 10px 0;'>
        <p>Built by <a href="https://www.linkedin.com/in/harshal-panchal/" target="_blank">Harshal Panchal</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
