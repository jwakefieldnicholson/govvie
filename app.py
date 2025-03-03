import streamlit as st
import json
from datetime import datetime
import os

# Set page configuration
st.set_page_config(
    page_title="Government Department Updates",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Function to load content from JSON file
def load_content():
    try:
        with open("content.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading content.json: {str(e)}")
        # Return a default structure if file doesn't exist or is invalid
        return {
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "departments": {}
        }

# Check if content.json exists, if not create a default one
if not os.path.exists("content.json"):
    try:
        default_content = {
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
            "departments": {
                "Department of State": {
                    "bulletins": [
                        "The Department is currently reviewing all diplomatic communications protocols.",
                        "An internal assessment of international agreements is underway.",
                        "Updates to foreign policy frameworks are pending administrative approval.",
                        "Standard diplomatic procedures remain in effect until further notice.",
                        "International relations continue to be a priority for the Department."
                    ]
                }
            }
        }
        with open("content.json", "w") as f:
            json.dump(default_content, f, indent=2)
        print("Created default content.json file")
    except Exception as e:
        print(f"Error creating default content.json: {str(e)}")

# Load the content
content = load_content()

# Add custom CSS for dark mode and sleek design
st.markdown("""
<style>
    /* Dark mode base styles */
    body {
        color: #E0E0E0;
        background-color: #121212;
    }
    
    /* Header styles */
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #FAFAFA;
        text-transform: uppercase;
        letter-spacing: 2px;
        background: linear-gradient(90deg, #000000, #1F1F1F);
        padding: 15px;
        border-radius: 5px;
        text-align: center;
        border-bottom: 3px solid #4CAF50;
    }
    
    .department-header {
        font-size: 1.8rem;
        font-weight: bold;
        margin-top: 1rem;
        color: #FAFAFA;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 10px;
    }
    
    .update-date {
        font-style: italic;
        color: #AAAAAA;
        margin-bottom: 2rem;
        text-align: center;
    }
    
    /* Bulletin styling */
    .bulletin-container {
        background-color: #1E1E1E;
        padding: 25px;
        border-radius: 8px;
        border-left: 5px solid #4CAF50;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
    }
    
    .bulletin-item {
        margin-bottom: 20px;
        line-height: 1.6;
        color: #E0E0E0;
        padding: 10px;
        background-color: #252525;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    
    .bulletin-item:hover {
        background-color: #2C2C2C;
        transform: translateX(5px);
    }
    
    /* Streamlit element overrides */
    .stSelectbox > div > div {
        background-color: #1E1E1E !important;
        color: #E0E0E0 !important;
        border-radius: 5px !important;
        border: 1px solid #444 !important;
    }
    
    /* Footer styling */
    .footer {
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #333;
        text-align: center;
        color: #888;
        font-size: 0.85rem;
    }
    
    /* Badge styling */
    .badge {
        display: inline-block;
        background-color: #4CAF50;
        color: white;
        padding: 4px 8px;
        border-radius: 12px;
        font-size: 0.75rem;
        margin-left: 10px;
        vertical-align: middle;
    }
    
    /* Enhance scrollbar */
    ::-webkit-scrollbar {
        width: 10px;
        background: #121212;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #4CAF50;
        border-radius: 5px;
    }
    
    /* Override default Streamlit theme elements */
    .stApp {
        background-color: #121212;
    }
</style>
""", unsafe_allow_html=True)

# Add a background image effect
st.markdown("""
<div style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; 
    background: linear-gradient(rgba(18, 18, 18, 0.97), rgba(18, 18, 18, 0.97)), 
    url('https://images.unsplash.com/photo-1501504905252-473c47e087f8?auto=format&fit=crop&w=1920&q=80');
    background-size: cover; background-position: center; z-index: -1;"></div>
""", unsafe_allow_html=True)

# Header with government seal-style logo
st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <div style="display: inline-block; width: 70px; height: 70px; margin-right: 15px; vertical-align: middle;
        background: radial-gradient(circle, #4CAF50, #121212); border-radius: 50%; position: relative;">
        <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); 
            color: white; font-size: 30px;">🦅</div>
    </div>
    <div class="main-header" style="display: inline-block; vertical-align: middle;">
        OFFICIAL DEPARTMENT UPDATES
    </div>
</div>
""", unsafe_allow_html=True)

# Date with badge
st.markdown(f"""
<div class="update-date">
    <span>Last Updated: {content["last_updated"]}</span>
    <span class="badge">CLASSIFIED</span>
</div>
""", unsafe_allow_html=True)

# Government departments list
departments = [
    "Department of State",
    "Department of the Treasury",
    "Department of Defense",
    "Department of Justice",
    "Department of the Interior",
    "Department of Agriculture",
    "Department of Commerce",
    "Department of Labor",
    "Department of Health and Human Services",
    "Department of Housing and Urban Development",
    "Department of Transportation",
    "Department of Energy",
    "Department of Education",
    "Department of Veterans Affairs",
    "Department of Homeland Security",
    "Environmental Protection Agency",
    "Federal Communications Commission",
    "Securities and Exchange Commission",
    "National Aeronautics and Space Administration",
    "Federal Trade Commission",
    "Small Business Administration",
    "Nuclear Regulatory Commission",
    "Federal Reserve System",
    "Consumer Financial Protection Bureau",
    "National Science Foundation"
]

# Dropdown for department selection
selected_dept = st.selectbox("Select a Department", departments)

# Display selected department header with decorative elements
st.markdown(f"""
<div style="display: flex; align-items: center; margin: 20px 0;">
    <div style="flex-grow: 1; height: 2px; background: linear-gradient(to right, #121212, #4CAF50); margin-right: 20px;"></div>
    <div class="department-header">{selected_dept}</div>
    <div style="flex-grow: 1; height: 2px; background: linear-gradient(to left, #121212, #4CAF50); margin-left: 20px;"></div>
</div>
""", unsafe_allow_html=True)

# Display department content with enhanced styling
if selected_dept in content.get("departments", {}):
    dept_content = content["departments"][selected_dept]
    
    # Add a subtle animation effect for loading content
    st.markdown("""
    <style>
        @keyframes fadeIn {
          from { opacity: 0; transform: translateY(10px); }
          to { opacity: 1; transform: translateY(0); }
        }
        .animated-container {
          animation: fadeIn 0.5s ease-out;
        }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="bulletin-container animated-container">', unsafe_allow_html=True)
    
    # Add classification header
    st.markdown("""
    <div style="margin-bottom: 15px; border-bottom: 1px solid #333; padding-bottom: 10px;">
        <span style="color: #4CAF50; font-weight: bold;">CLASSIFICATION:</span>
        <span style="color: #FFD700; margin-left: 10px;">FOR UNOFFICIAL USE ONLY</span>
    </div>
    """, unsafe_allow_html=True)
    
    # Show bulletins with icons and improved formatting
    for i, item in enumerate(dept_content["bulletins"]):
        icon = ["🔍", "📊", "🔐", "📝", "⚠️"][i % 5]  # Cycle through different icons
        st.markdown(f'<div class="bulletin-item">{icon} {item}</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
else:
    # Enhanced "no content" message
    st.markdown("""
    <div style="text-align: center; padding: 40px; background-color: #1E1E1E; border-radius: 8px; margin-top: 20px;">
        <div style="font-size: 40px; margin-bottom: 10px;">🔒</div>
        <div style="font-weight: bold; color: #4CAF50; margin-bottom: 10px;">CLASSIFIED</div>
        <div style="color: #AAAAAA;">Updates for this department are currently restricted.</div>
        <div style="color: #888888; font-size: 0.9rem; margin-top: 15px;">Please check back later or contact your supervisor for clearance.</div>
    </div>
    """, unsafe_allow_html=True)
    
# Enhanced Footer with official-looking elements
st.markdown("""
<div class="footer">
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div style="width: 30px; height: 30px; margin: 0 15px; opacity: 0.7;">🦅</div>
        <div style="width: 30px; height: 30px; margin: 0 15px; opacity: 0.7;">⚖️</div>
        <div style="width: 30px; height: 30px; margin: 0 15px; opacity: 0.7;">🏛️</div>
    </div>
    <div style="margin-bottom: 10px; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">
        UNOFFICIAL NON-GOVERNMENT INFORMATION PORTAL
    </div>
    <div style="font-size: 0.8rem; color: #666;">
        All updates are for entertainment purposes only. Classification: FUUO.
    </div>
    <div style="font-size: 0.7rem; color: #555; margin-top: 15px;">
        Form ID: NGOV-UPD-2025-03 | Clearance: L3 | Retention: 7 years
    </div>
</div>
""", unsafe_allow_html=True)

# Add a subtle background pattern
st.markdown("""
<style>
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-image: radial-gradient(#4CAF50 1px, transparent 1px);
        background-size: 50px 50px;
        opacity: 0.03;
        z-index: -1;
        pointer-events: none;
    }
</style>
""", unsafe_allow_html=True)
