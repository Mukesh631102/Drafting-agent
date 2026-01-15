import streamlit as st
import os
import groq
from fpdf import FPDF
from src.agents.drafting_agent import DraftingAgent

# 1. Page Configuration
st.set_page_config(
    page_title="EduFinance | Official Drafting",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. PDF Helper Function with Unicode Sanitization
def convert_to_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    
    # Cleaning the Unicode characters first
    safe_text = text.replace('\u202f', ' ').replace('\u2013', '-').replace('\u2019', "'").replace('\u2018', "'")
    safe_text = safe_text.encode('latin-1', 'replace').decode('latin-1')
    
    # Split text into lines to apply formatting
    lines = safe_text.split('\n')
    
    for line in lines:
        if not line.strip(): # Skip empty lines
            pdf.ln(5)
            continue
            
        # 1. Handle Headers (Lines starting with #)
        if line.startswith('#'):
            pdf.set_font("Helvetica", 'B', size=14)
            clean_line = line.lstrip('#').strip()
            pdf.multi_cell(0, 10, txt=clean_line)
            pdf.set_font("Helvetica", size=11) # Reset to normal
            
        # 2. Handle Bold Keywords or Subheaders (Lines starting with ** or ALL CAPS)
        elif line.startswith('**') or (line.isupper() and len(line) < 50):
            pdf.set_font("Helvetica", 'B', size=11)
            clean_line = line.replace('**', '').strip()
            pdf.multi_cell(0, 8, txt=clean_line)
            pdf.set_font("Helvetica", size=11)
            
        # 3. Handle Normal Text / Tables
        else:
            pdf.set_font("Helvetica", size=11)
            pdf.multi_cell(0, 8, txt=line)
            
    return bytes(pdf.output())
# 3. Custom CSS
st.markdown("""
    <style>
        header {visibility: hidden;}
        footer {visibility: hidden;}
        #MainMenu {visibility: hidden;}
        
        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
            background-color: #F8FAFC;
        }

        .doc-paper {
            background-color: #FFFFFF !important;
            color: #0F172A !important; 
            padding: 50px !important;
            border: 1px solid #CBD5E1 !important;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1) !important;
            min-height: 700px;
            line-height: 1.6;
            overflow-wrap: break-word;
        }

        .doc-paper h1, .doc-paper h2, .doc-paper h3, .doc-paper p, .doc-paper li {
            color: #0F172A !important;
        }

        .stButton button {
            background-color: #0F172A !important;
            color: white !important;
            border-radius: 8px !important;
            height: 3em !important;
            width: 100%;
            font-weight: 600 !important;
        }
    </style>
""", unsafe_allow_html=True)

# 4. Main Logic
def main():
    st.title("🏦 EduFinance Drafting System")
    st.markdown("##### Professional Financial Document Automation")
    st.write("")

    agent = DraftingAgent()

    col_work, col_view = st.columns([1, 2], gap="large")

    with col_work:
        st.subheader("🛠️ Workspace")
        task = st.selectbox("Select Process", ["Reconciliation", "Audit-Ready Report", "Approval Memo"])
        user_input = st.text_area("Input Financial Data/Context", height=300, placeholder="Enter budget data...")
        
        process_btn = st.button("Generate Document")

        if process_btn:
            if user_input:
                with st.spinner("Processing through GPT OSS 120B..."):
                    try:
                        file_path = agent.run(task, user_input)
                        with open(file_path, "r", encoding="utf-8") as f:
                            st.session_state['draft_content'] = f.read()
                            # Clean filename logic
                            base_name = os.path.basename(file_path).replace(".md", "")
                            st.session_state['file_name_base'] = base_name
                            
                        st.success("Draft Complete.")
                    except Exception as e:
                        st.error(f"System Error: {e}")
            else:
                st.warning("Please provide data before generating.")

    with col_view:
        st.subheader("📄 Document Preview")
        
        if 'draft_content' in st.session_state:
            # Preview on screen
            st.markdown(f'<div class="doc-paper">{st.session_state["draft_content"]}</div>', unsafe_allow_html=True)
            
            st.write("")
            down_col1, down_col2 = st.columns(2)
            
            with down_col1:
                # Use the new safe PDF conversion
                try:
                    pdf_data = convert_to_pdf(st.session_state['draft_content'])
                    st.download_button(
                        label="📥 Download Official PDF",
                        data=pdf_data,
                        file_name=f"{st.session_state['file_name_base']}.pdf",
                        mime="application/pdf"
                    )
                except Exception as pdf_err:
                    st.error(f"PDF Error: {pdf_err}")
            
            with down_col2:
                if st.button("🗑️ Clear Workspace"):
                    del st.session_state.draft_content
                    st.rerun()
        else:
            st.info("Drafted content will appear here.")

if __name__ == "__main__":
    main()
    
    