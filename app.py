import streamlit as st
import os
import zipfile
import base64
from utils import extract_text_from_file
import evori

# 1. SETUP PAGE
st.set_page_config(page_title="Academic Dashboard", layout="wide", page_icon="📚")

# 2. CONFIGURE FOLDERS
KB_DIR = "knowledge_base"
if not os.path.exists(KB_DIR):
    os.makedirs(KB_DIR)

# 3. SIDEBAR CONTROLS
with st.sidebar:
    st.header("📚 Academic Library")
    
    app_theme = st.selectbox("App Theme", ["Evori Neon (Pink)", "Evori Neon (Purple)", "Evori Neon (Green)", "Evori Neon (Orange)", "Light Mode"])
    cat_mode = st.selectbox("Evori Role", ["Default", "Strategist", "Finance", "CEO", "Examiner"])
    is_equipped = st.toggle("🐱 Equip Evori Familiar", value=True)
    
    st.markdown("---")
    
    # Legacy Zip Upload (for quick temporary files)
    uploaded_zip = st.file_uploader("Upload temporary .zip", type="zip")
    if uploaded_zip:
        with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
            zip_ref.extractall(KB_DIR)
        st.success("Extracted to library!")
        
    st.markdown("---")

# 4. READ FILES FROM REPOSITORY
library_files = []
file_paths = {}

for root, dirs, files in os.walk(KB_DIR):
    for file in files:
        if not file.startswith('.'):  # Ignore hidden GitHub files like .keep
            full_path = os.path.join(root, file)
            library_files.append(file)
            file_paths[file] = full_path

# 5. EVORI DEEP-LINK ROUTER & SELECTOR
with st.sidebar:
    st.subheader("Available Documents")
    if library_files:
        # Check if Evori clicked a link to automatically open a specific document
        query_params = st.query_params
        doc_param = query_params.get("doc", None)
        
        default_index = 0
        if doc_param and doc_param in library_files:
            default_index = library_files.index(doc_param) + 1
            
        options = ["-- Select --"] + library_files
        selected_theory = st.selectbox("Select a document to read:", options, index=default_index)
    else:
        st.warning("No documents found in knowledge_base/")
        selected_theory = "-- Select --"

# 6. MAIN DASHBOARD VIEWER
st.title("Academic Dashboard")

if selected_theory != "-- Select --":
    file_path = file_paths[selected_theory]
    
    if selected_theory.lower().endswith('.txt'):
        st.subheader(f"Viewing: {selected_theory}")
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            st.text_area("Document Content", f.read(), height=600)
            
    elif selected_theory.lower().endswith('.pdf'):
        with open(file_path, "rb") as f:
            pdf_bytes = f.read()
        
        col1, col2 = st.columns([3, 1])
        with col1: 
            st.markdown(f"### 📄 {selected_theory}")
        with col2: 
            st.download_button(label="📥 Download File", data=pdf_bytes, file_name=selected_theory, mime='application/pdf', use_container_width=True)
        
        # Cloud-safe PDF Embed
        base64_pdf = base64.b64encode(pdf_bytes).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800" type="application/pdf">'
        st.markdown(pdf_display, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("#### 📝 Raw Text Preview (What Evori reads)")
        try:
            preview = extract_text_from_file(file_path)
            if preview: 
                st.text_area("Extracted Text", preview, height=250)
            else: 
                st.warning("No readable text found. If this is a scanned document, Evori will not be able to read the words inside it.")
        except Exception as e:
            st.error(f"Could not extract text from this file.")
    
    else:
        # Fallback for Word/Excel/PowerPoint
        st.subheader(f"Viewing: {selected_theory}")
        with open(file_path, "rb") as f:
            file_bytes = f.read()
        st.download_button(label="📥 Download File", data=file_bytes, file_name=selected_theory)
        st.info("Direct browser preview is not available for this file type. Please download it to view.")
        
else:
    st.info("👈 Select a document from the sidebar or ask Evori to search for one!")

# 7. INITIALIZE EVORI
evori.apply_theme_and_cat(app_theme, cat_mode, is_equipped, library_files)
