import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dev.Jur OS",
    page_icon="⚖️",
    layout="centered"
)

# --- URL da Imagem de Fundo ---
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop"

# --- INJEÇÃO DE CSS (Visual Matrix Ajustado) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;700&display=swap');

    /* Fundo */
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.9)), url('{BACKGROUND_IMAGE}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Roboto Mono', monospace;
    }}

    /* Textos */
    h1, h2, h3, p, div, span {{
        color: #E2E8F0 !important;
        font-family: 'Roboto Mono', monospace !important;
    }}
    
    .highlight {{
        color: #4ADE80 !important;
        font-weight: bold;
    }}

    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {{
        background-color: transparent !important;
    }}
    
    /* Card Glassmorphism */
    .app-card {{
        background: rgba(30, 41, 59, 0.7);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left: 4px solid #4ADE80;
        padding: 25px;
        margin-bottom: 20px;
        border-radius: 8px;
        transition: transform 0.2s ease;
    }}
    
    .app-card:hover {{
        transform: translateY(-2px);
        border-color: #4ADE80;
    }}

    /* --- AJUSTE CRÍTICO: Estilizando o Link Button --- */
    /* Isso garante que o st.link_button fique igual ao st.button */
    a[data-testid="stLinkButton"] {{
        background-color: transparent !important;
        color: #4ADE80 !important;
        border: 1px solid #4ADE80 !important;
        border-radius: 4px !important;
        font-family: 'Roboto Mono', monospace !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        transition: all 0.3s !important;
        text-decoration: none !important;
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
    }}
    
    a[data-testid="stLinkButton"]:hover {{
        background-color: #4ADE80 !important;
        color: #0F172A !important;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.4) !important;
        border-color: #4ADE80 !important;
    }}
    
    /* Input Senha */
    input {{
        background-color: rgba(0,0,0,0.5) !important;
        color: #4ADE80 !important;
        border: 1px solid #333 !important;
    }}
</style>
""", unsafe_allow_html=True)

# --- Dados dos Apps ---
APPS = [
    {
        "nome": "ARGUS JURÍDICO",
        "url": "https://argus-juridico.vercel.app/",
        "desc": "Sistema de inteligência para Recursos Especiais.",
        "icon": "⚖️"
    }
]

# --- Sistema de Login ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if st.session_state.password_correct:
        return True

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 2.5rem; letter-spacing: 2px;'>DEV.JUR <span class='highlight'>OS</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.6; font-size: 0.8rem;'>SECURE ACCESS TERMINAL</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        password = st.text_input("PASSWORD", type="password", label_visibility="collapsed", placeholder="Insira a chave de acesso...")
        if st.button("AUTHENTICATE", use_container_width=True):
            # Tenta ler do Secrets, se falhar usa admin
            senha_secreta = st.secrets["PASSWORD"] if "PASSWORD" in st.secrets else "admin"
            
            if password == senha_secreta: 
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")
    return False

# --- Renderização do Dashboard ---
if check_password():
    st.markdown(f"""
    <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom: 30px;'>
        <div>
            <span class='highlight'>STATUS:</span> ONLINE<br>
            <span style='font-size: 0.8rem; opacity: 0.7;'>SERVER: CLOUD NODE</span>
        </div>
        <div style='text-align:right;'>
            DEV.JUR<br>
            <span style='font-size: 0.8rem; opacity: 0.7;'>V 2.2</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>SELECIONE O MÓDULO</h3>", unsafe_allow_html=True)

    for app in APPS:
        st.markdown(f"""
        <div class="app-card">
            <div style="font-size: 1.3rem; margin-bottom: 8px;">{app['icon']} <strong>{app['nome']}</strong></div>
            <p style="font-size: 0.9rem; opacity: 0.8; margin-bottom: 0;">{app['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # --- MUDANÇA AQUI: Usando Link Button Nativo ---
        st.link_button(f"INICIAR SISTEMA", app['url'], use_container_width=True)

    st.markdown("<br><br><div style='text-align: center; font-size: 0.7rem; opacity: 0.4; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;'>CURATOR MODULE | DEV.JUR ARCHITECTURE</div>", unsafe_allow_html=True)