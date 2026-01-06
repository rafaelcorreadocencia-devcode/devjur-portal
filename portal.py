import streamlit as st

# --- Configuração da Página ---
# Layout "wide" para ocupar a tela toda
st.set_page_config(
    page_title="Dev.Jur OS",
    page_icon="⚖️",
    layout="wide" 
)

# --- IMAGENS ---
# Imagem de Fundo (Tecnologia/Dados)
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop"

# --- CORREÇÃO AQUI: Imagem Estável (Circuitos Verdes/Cyberpunk) ---
# Link direto e público do Unsplash (não expira)
CARD_HEADER_IMAGE = "https://images.unsplash.com/photo-1518770660439-4636190af475?q=80&w=1740&auto=format&fit=crop"

# --- INJEÇÃO DE CSS (V3.2 - Estável) ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;700&display=swap');

    /* --- HEADER TRANSPARENTE --- */
    header[data-testid="stHeader"] {{
        background-color: transparent !important;
        background: transparent !important;
        box-shadow: none !important;
    }}
    header[data-testid="stHeader"] * {{
        color: #E2E8F0 !important;
    }}
    .block-container {{
        padding-top: 1rem !important;
        padding-bottom: 5rem !important;
    }}

    /* --- FUNDO E TIPOGRAFIA --- */
    .stApp {{
        background-image: linear-gradient(rgba(10, 15, 30, 0.92), rgba(10, 15, 30, 0.92)), url('{BACKGROUND_IMAGE}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Roboto Mono', monospace;
    }}

    h1, h2, h3, p, div, span, label, b, strong {{
        color: #E2E8F0 !important;
        font-family: 'Roboto Mono', monospace !important;
    }}
    
    .highlight {{
        color: #4ADE80 !important;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(74, 222, 128, 0.4);
    }}

    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {{
        background-color: transparent !important;
    }}
    
    /* --- CARDS TECNOLÓGICOS --- */
    .tech-card {{
        background: rgba(20, 30, 50, 0.6);
        backdrop-filter: blur(15px);
        border: 2px solid #4ADE80;
        box-shadow: 0 0 15px rgba(74, 222, 128, 0.2), inset 0 0 15px rgba(74, 222, 128, 0.1);
        border-radius: 12px;
        overflow: hidden;
        transition: all 0.3s ease;
        height: 100%;
        display: flex;
        flex-direction: column;
        margin-bottom: 20px;
    }}
    
    .tech-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 0 30px rgba(74, 222, 128, 0.5), inset 0 0 20px rgba(74, 222, 128, 0.2);
    }}

    .card-image-container {{
        height: 160px;
        overflow: hidden;
        position: relative;
        border-bottom: 1px solid rgba(74, 222, 128, 0.3);
    }}
    
    .card-image {{
        width: 100%;
        height: 100%;
        object-fit: cover;
        opacity: 0.8;
        transition: opacity 0.3s, transform 0.5s;
    }}
    .tech-card:hover .card-image {{
        opacity: 1;
        transform: scale(1.05);
    }}
    
    .card-content {{
        padding: 20px;
        flex-grow: 1;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
    }}

    /* --- BOTÃO NEON --- */
    .neon-button {{
        background: transparent;
        color: #4ADE80;
        border: 2px solid #4ADE80;
        border-radius: 6px;
        padding: 12px 24px;
        font-family: 'Roboto Mono', monospace;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        cursor: pointer;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 20px;
        text-decoration: none;
        display: inline-block;
        text-align: center;
        box-shadow: 0 0 10px rgba(74, 222, 128, 0.2);
    }}
    
    .neon-button:hover {{
        background: #4ADE80;
        color: #0A0F1E;
        box-shadow: 0 0 30px rgba(74, 222, 128, 0.7);
    }}

    /* --- INPUT SENHA --- */
    input[type="password"] {{
        background-color: rgba(15, 23, 42, 0.9) !important;
        color: #4ADE80 !important;
        border: 2px solid rgba(74, 222, 128, 0.4) !important;
        text-align: center;
        letter-spacing: 3px;
        font-weight: bold;
    }}
    input[type="password"]:focus {{
        border-color: #4ADE80 !important;
        box-shadow: 0 0 20px rgba(74, 222, 128, 0.4) !important;
        outline: none;
    }}

    /* --- BOTÃO LOGIN (CSS FORCE) --- */
    div[data-testid="stFormButton"] > button {{
        background-color: transparent !important;
        color: #4ADE80 !important;
        border: 2px solid #4ADE80 !important;
        border-radius: 4px !important;
        font-family: 'Roboto Mono', monospace !important;
        font-weight: 700 !important;
        letter-spacing: 2px !important;
        text-transform: uppercase !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 10px rgba(74, 222, 128, 0.2) !important;
    }}

    div[data-testid="stFormButton"] > button:hover {{
         background-color: #4ADE80 !important;
         color: #0A0F1E !important;
         box-shadow: 0 0 30px rgba(74, 222, 128, 0.6) !important;
    }}
    
    div[data-testid="stFormButton"] > button:active,
    div[data-testid="stFormButton"] > button:focus {{
        background-color: transparent !important;
        color: #4ADE80 !important;
        border-color: #4ADE80 !important;
    }}
    div[data-testid="stFormButton"] > button * {{
         color: inherit !important;
    }}

</style>
""", unsafe_allow_html=True)

# --- INVENTÁRIO DE APPS ---
APPS = [
    {
        "nome": "ARGUS JURÍDICO",
        "url": "https://argus-juridico.vercel.app/",
        "desc": "Inteligência artificial para Geração de Recursos Especiais.",
        "icon": "⚖️"
    },
    {
        "nome": "Prof.Rafael.AI",
        "url": "https://rafael-ai-app-grtjcshxodhf7uwnrv4utw.streamlit.app/",
        "desc": "Sistema Neural para Artigos, Aulas e TCC's.",
        "icon": "📚"
    },
]

# --- Sistema de Login ---
def check_password():
    if "password_correct" not in st.session_state:
        st.session_state.password_correct = False

    if st.session_state.password_correct:
        return True

    col_spacer_l, col_login, col_spacer_r = st.columns([1.5, 1, 1.5])
    with col_login:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(f"<div style='text-align: center; font-size: 3rem; letter-spacing: 4px; text-shadow: 0 0 20px rgba(74,222,128,0.5);'>DEV.JUR <span class='highlight'>OS</span></div>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center; opacity: 0.8; font-size: 0.9rem; letter-spacing: 2px; margin-bottom: 40px;'>SECURE ACCESS TERMINAL // V3.2</p>", unsafe_allow_html=True)
        
        with st.form("login_form"):
            password = st.text_input("SENHA", type="password", label_visibility="collapsed", placeholder=">> INSERIR CHAVE DE ACESSO <<")
            submitted = st.form_submit_button("AUTENTICAR SISTEMA", use_container_width=True)
            
            if submitted:
                senha_secreta = st.secrets["PASSWORD"] if "PASSWORD" in st.secrets else "admin"
                if password == senha_secreta: 
                    st.session_state.password_correct = True
                    st.rerun()
                else:
                    st.error("ERRO: ACESSO NEGADO")
    return False

# --- Dashboard ---
if check_password():
    st.markdown(f"""
    <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom: 40px; border-bottom: 2px solid rgba(74,222,128,0.3); padding-bottom: 15px;'>
        <div>
            <span class='highlight' style="font-size: 1.2rem;">STATUS: ONLINE</span><br>
            <span style='font-size: 0.8rem; opacity: 0.8; letter-spacing: 1px;'>REDE NEURAL CONECTADA</span>
        </div>
        <div style='text-align:right;'>
            <strong style="font-size: 1.2rem;">DEV.JUR CORE</strong><br>
            <span style='font-size: 0.8rem; opacity: 0.8; letter-spacing: 1px;'>V 3.2 STABLE</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h2 style='text-align: center; margin-bottom: 40px; letter-spacing: 3px; text-transform: uppercase;'>Módulos Disponíveis</h2>", unsafe_allow_html=True)

    for i in range(0, len(APPS), 2):
        cols = st.columns(2)
        for j in range(2):
            if i + j < len(APPS):
                app = APPS[i+j]
                with cols[j]:
                    st.markdown(f"""
                    <div class="tech-card">
                        <div class="card-image-container">
                            <img src="{CARD_HEADER_IMAGE}" class="card-image">
                        </div>
                        <div class="card-content">
                            <div>
                                <div style="font-size: 1.4rem; margin-bottom: 10px; display: flex; align-items: center;">
                                    <span style="margin-right: 12px; filter: drop-shadow(0 0 5px rgba(74,222,128,0.7));">{app['icon']}</span> 
                                    <strong style="letter-spacing: 1px; color: #4ADE80 !important;">{app['nome']}</strong>
                                </div>
                                <p style="font-size: 1rem; opacity: 0.9; line-height: 1.5;">{app['desc']}</p>
                            </div>
                            <a href="{app['url']}" target="_blank" style="text-decoration: none;">
                                <button class="neon-button">INICIAR SISTEMA</button>
                            </a>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)

    st.markdown("<br><br><div style='text-align: center; font-size: 0.8rem; opacity: 0.6; border-top: 1px solid rgba(74,222,128,0.2); padding-top: 30px; letter-spacing: 2px;'>DEV.JUR ARCHITECTURE | SECURE QUANTUM LINK</div>", unsafe_allow_html=True)