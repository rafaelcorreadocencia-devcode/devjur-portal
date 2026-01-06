import streamlit as st

# --- Configuração da Página ---
st.set_page_config(
    page_title="Dev.Jur OS",
    page_icon="⚖️",
    layout="centered"
)

# --- URL da Imagem de Fundo ---
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop"

# --- INJEÇÃO DE CSS (Correção Definitiva de Cores) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;700&display=swap');

    /* --- FUNDO GERAL --- */
    .stApp {{
        background-image: linear-gradient(rgba(15, 23, 42, 0.95), rgba(15, 23, 42, 0.95)), url('{BACKGROUND_IMAGE}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Roboto Mono', monospace;
    }}

    /* --- TEXTOS --- */
    h1, h2, h3, p, div, span, label {{
        color: #E2E8F0 !important;
        font-family: 'Roboto Mono', monospace !important;
    }}
    
    .highlight {{
        color: #4ADE80 !important;
        font-weight: bold;
    }}

    /* Remove fundos extras do Streamlit */
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {{
        background-color: transparent !important;
    }}
    
    /* --- CARDS --- */
    .app-card {{
        background: rgba(30, 41, 59, 0.6);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(74, 222, 128, 0.2);
        border-left: 4px solid #4ADE80;
        padding: 25px;
        margin-bottom: 20px;
        border-radius: 8px;
        transition: all 0.3s ease;
    }}
    .app-card:hover {{
        transform: translateY(-3px);
        border-color: #4ADE80;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}

    /* --- CSS NUCLEAR PARA OS BOTÕES (Login e Link) --- */
    
    /* 1. Alvo: Botão Normal (button) E Botão de Link (a) */
    .stButton > button, 
    a[data-testid="stLinkButton"],
    a[data-testid="stLinkButton"]:visited,
    a[data-testid="stLinkButton"]:active,
    a[data-testid="stLinkButton"]:focus {{
        background-color: transparent !important;
        background: transparent !important;
        color: #4ADE80 !important; /* Verde Neon */
        border: 1px solid #4ADE80 !important;
        border-radius: 4px !important;
        
        font-family: 'Roboto Mono', monospace !important;
        font-weight: 700 !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        text-decoration: none !important;
        
        box-shadow: none !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        
        /* Centralizar */
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important; /* Garante largura total no card */
    }}

    /* 2. Garante que o texto interno não mude de cor */
    .stButton > button *, a[data-testid="stLinkButton"] * {{
         color: #4ADE80 !important;
         text-decoration: none !important;
    }}
    
    /* 3. Efeito HOVER (Mouse em cima) - Fica Verde Cheio */
    .stButton > button:hover, 
    a[data-testid="stLinkButton"]:hover {{
        background-color: #4ADE80 !important;
        color: #0F172A !important; /* Texto Escuro */
        border-color: #4ADE80 !important;
        box-shadow: 0 0 20px rgba(74, 222, 128, 0.6) !important;
        transform: scale(1.02);
    }}

    /* 4. Texto escuro no Hover */
    .stButton > button:hover *, a[data-testid="stLinkButton"]:hover * {{
         color: #0F172A !important;
    }}
    
    /* --- INPUT SENHA --- */
    input {{
        background-color: rgba(15, 23, 42, 0.8) !important;
        color: #4ADE80 !important;
        border: 1px solid rgba(74, 222, 128, 0.3) !important;
    }}
    input:focus {{
        border-color: #4ADE80 !important;
        box-shadow: 0 0 10px rgba(74, 222, 128, 0.2) !important;
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
    st.markdown(f"<div style='text-align: center; font-size: 2.5rem; letter-spacing: 2px; text-shadow: 0 0 10px rgba(74,222,128,0.3);'>DEV.JUR <span class='highlight'>OS</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.6; font-size: 0.8rem; letter-spacing: 1px;'>SECURE ACCESS TERMINAL // V2.4</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        password = st.text_input("PASSWORD", type="password", label_visibility="collapsed", placeholder=">> INSIRA A CHAVE <<")
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Botão de Login (st.button)
        if st.button("AUTHENTICATE", use_container_width=True):
            senha_secreta = st.secrets["PASSWORD"] if "PASSWORD" in st.secrets else "admin"
            
            if password == senha_secreta: 
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("ACCESS DENIED // TENTATIVA REGISTRADA")
    return False

# --- Renderização do Dashboard ---
if check_password():
    st.markdown(f"""
    <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom: 30px; border-bottom: 1px solid rgba(74,222,128,0.2); padding-bottom: 10px;'>
        <div>
            <span class='highlight'>STATUS:</span> <span style='text-shadow: 0 0 5px rgba(74,222,128,0.5);'>ONLINE</span><br>
            <span style='font-size: 0.7rem; opacity: 0.7; letter-spacing: 1px;'>SERVER: CLOUD NODE JS-1</span>
        </div>
        <div style='text-align:right;'>
            DEV.JUR<br>
            <span style='font-size: 0.7rem; opacity: 0.7; letter-spacing: 1px;'>V 2.4 STABLE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; margin-bottom: 30px; letter-spacing: 2px;'>SELECIONE O MÓDULO</h3>", unsafe_allow_html=True)

    for app in APPS:
        st.markdown(f"""
        <div class="app-card">
            <div style="font-size: 1.3rem; margin-bottom: 8px; display: flex; align-items: center;">
                <span style="margin-right: 10px;">{app['icon']}</span> 
                <strong style="letter-spacing: 1px;">{app['nome']}</strong>
            </div>
            <p style="font-size: 0.9rem; opacity: 0.8; margin-bottom: 20px; line-height: 1.4;">{app['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão de Link (st.link_button) - Agora estilizado igual
        st.link_button(f"INICIAR SISTEMA", app['url'], use_container_width=True)
        st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<br><div style='text-align: center; font-size: 0.7rem; opacity: 0.4; border-top: 1px solid rgba(74,222,128,0.1); padding-top: 20px; letter-spacing: 1px;'>CURATOR MODULE | DEV.JUR ARCHITECTURE | ENCRYPTED</div>", unsafe_allow_html=True)