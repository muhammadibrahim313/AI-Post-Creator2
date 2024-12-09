import streamlit as st
from utils import load_css, show_error, show_success
from crewai import Crew
from textwrap import dedent
from agents import NewsAgents
from tasks import NewsTasks
from dotenv import load_dotenv

load_dotenv()

class PostCreatorCrew:
    def __init__(self, news_topic, target_audience, platform, tone="", 
                 word_count="", language="English", include_emojis=False, 
                 special_requests=""):
        self.news_topic = news_topic
        self.target_audience = target_audience
        self.platform = platform
        self.tone = tone
        self.word_count = word_count
        self.language = language
        self.include_emojis = include_emojis
        self.special_requests = special_requests

    def run(self):
        agents = NewsAgents()
        tasks = NewsTasks()

        news_retriever = agents.news_retrieval_agent()
        news_validator = agents.news_validator_agent()
        post_creator = agents.post_creator_agent()

        retrieve_news_task = tasks.retrieve_news_task(
            news_retriever,
            self.news_topic
        )
        
        validate_news_task = tasks.validate_and_summarize_task(
            news_validator,
            "{retrieve_news_task.output}",
            self.news_topic
        )
        
        create_post_task = tasks.create_post_task(
            post_creator,
            "{validate_news_task.output}",
            self.target_audience,
            self.platform,
            self.tone,
            self.word_count,
            self.language,
            self.include_emojis,
            self.special_requests
        )

        crew = Crew(
            agents=[news_retriever, news_validator, post_creator],
            tasks=[retrieve_news_task, validate_news_task, create_post_task],
            verbose=True
        )

        result = crew.kickoff()
        return result

# Page Configuration
st.set_page_config(
    page_title="Create Post",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown(load_css(), unsafe_allow_html=True)

# Initialize session state for post history
if 'post_history' not in st.session_state:
    st.session_state.post_history = []

# Title and Introduction
st.markdown("<h1 class='main-title'>Create Your Post ✍️</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Transform news into engaging social media content</p>", unsafe_allow_html=True)

# Information Card
info_card = (
    "<div class='card info-card'>"
    "<h3>How it works</h3>"
    "<p>1. Enter your news topic and target audience</p>"
    "<p>2. Choose your platform and customize settings</p>"
    "<p>3. Get AI-generated content optimized for your needs</p>"
    "<p class='info-text'>Our AI system researches current news and creates engaging posts</p>"
    "</div>"
)
st.markdown(info_card, unsafe_allow_html=True)

# Main Form
with st.form("post_creator_form"):
    # Required Information Section
    st.markdown("<h2 class='sub-title'>Required Information</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        news_topic = st.text_input(
            "News Topic 📰",
            help="Enter the main topic or subject of your post"
        )
    with col2:
        target_audience = st.text_input(
            "Target Audience 👥",
            help="e.g., Professionals, students, tech enthusiasts"
        )
    
    platform = st.selectbox(
        "Platform 🌐",
        ["LinkedIn", "Twitter/X", "Facebook", "Instagram", "Medium", "Other"],
        help="Choose where you'll share this post"
    )

    # Optional Customization Section
    st.markdown("<h2 class='sub-title'>Customize Your Post</h2>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        tone = st.text_input(
            "Tone 🎭",
            help="e.g., Professional, casual, humorous"
        )
    with col2:
        word_count = st.text_input(
            "Length 📏",
            help="Short (<100), Medium (100-300), Long (300+)"
        )
    with col3:
        language = st.text_input(
            "Language 🌍",
            value="English",
            help="e.g., English, Spanish, French"
        )

    include_emojis = st.checkbox(
        "Include Emojis 😊",
        help="Add relevant emojis to make the post more engaging"
    )

    special_requests = st.text_area(
        "Special Requests ✨",
        help="Any specific requirements, hashtags, or formatting preferences"
    )

    # Submit Button
    submit_button = st.form_submit_button(
        "Create Post 🎨", 
        type="primary",
        use_container_width=True
    )

if submit_button:
    if not news_topic or not target_audience:
        show_error("Please fill in all required fields")
    else:
        with st.spinner("🎯 Researching and creating your post..."):
            try:
                creator = PostCreatorCrew(
                    news_topic=news_topic,
                    target_audience=target_audience,
                    platform=platform,
                    tone=tone,
                    word_count=word_count,
                    language=language,
                    include_emojis=include_emojis,
                    special_requests=special_requests
                )
                result = creator.run()
                
                # Add to history
                st.session_state.post_history.append({
                    "topic": news_topic,
                    "platform": platform,
                    "audience": target_audience,
                    "content": result
                })
                
                show_success("Post created successfully!")
                
                # Display Results
                st.markdown("<h2 class='sub-title'>Generated Post</h2>", unsafe_allow_html=True)
                
                # Create tabs for different views
                tab1, tab2 = st.tabs(["📱 Preview", "📝 Raw Text"])
                
                with tab1:
                    preview_card = (
                        f"<div class='card result-card'>"
                        f"<div class='post-metadata'>"
                        f"<span><strong>Topic:</strong> {news_topic}</span> • "
                        f"<span><strong>Platform:</strong> {platform}</span> • "
                        f"<span><strong>Audience:</strong> {target_audience}</span>"
                        f"</div>"
                        f"<hr>"
                        f"<div class='post-content'>{result}</div>"
                        f"</div>"
                    )
                    st.markdown(preview_card, unsafe_allow_html=True)
                
                with tab2:
                    st.code(result, language="markdown")
                
                # Download button
                col1, col2, col3 = st.columns([1,2,1])
                with col2:
                    st.download_button(
                        label="Download Post 📥",
                        data=result,
                        file_name=f"post_{platform.lower().replace('/', '_')}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
            
            except Exception as e:
                show_error(f"Error creating post: {str(e)}")

# Display History
if st.session_state.post_history:
    st.markdown("<h2 class='sub-title'>Recent Posts</h2>", unsafe_allow_html=True)
    for idx, post in enumerate(reversed(st.session_state.post_history[-5:])):
        history_card = (
            f"<div class='card history-card'>"
            f"<h3>Post #{len(st.session_state.post_history) - idx}</h3>"
            f"<div class='post-metadata'>"
            f"<span><strong>Topic:</strong> {post['topic']}</span> • "
            f"<span><strong>Platform:</strong> {post['platform']}</span> • "
            f"<span><strong>Audience:</strong> {post['audience']}</span>"
            f"</div>"
            f"<hr>"
            f"<div class='post-content'>{post['content']}</div>"
            f"</div>"
        )
        st.markdown(history_card, unsafe_allow_html=True)