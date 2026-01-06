import streamlit as st
import webbrowser

# --- Configuração da Página (OBRIGATÓRIO SER A PRIMEIRA LINHA) ---
st.set_page_config(
    page_title="Dev.Jur OS",
    page_icon="⚖️",
    layout="centered"
)

# --- URL da Imagem de Fundo ---
# Você pode trocar esse link por qualquer imagem que gostar da internet
BACKGROUND_IMAGE = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?q=80&w=2072&auto=format&fit=crop"

# --- INJEÇÃO DE CSS (Design Sofisticado) ---
st.markdown(f"""
<style>
    /* Importando fonte tecnológica limpa */
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;700&display=swap');

    /* Configuração do Fundo com Imagem + Máscara Escura */
    .stApp {{
        /* A primeira parte é um gradiente preto semi-transparente para escurecer a imagem */
        background-image: linear-gradient(rgba(15, 23, 42, 0.9), rgba(15, 23, 42, 0.9)), url('{BACKGROUND_IMAGE}');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Roboto Mono', monospace;
    }}

    /* Títulos e Textos */
    h1, h2, h3, p, div, span {{
        color: #E2E8F0 !important; /* Cinza claro, quase branco, mais suave que branco puro */
        font-family: 'Roboto Mono', monospace !important;
    }}
    
    /* Destaque Verde (Mais sutil e elegante agora) */
    .highlight {{
        color: #4ADE80 !important; /* Um verde mais pastel/suave, menos neon agressivo */
        font-weight: bold;
    }}

    /* Remove fundos padrões do Streamlit */
    div[data-testid="stVerticalBlock"] > div[style*="background-color"] {{
        background-color: transparent !important;
    }}
    
    /* Card com Efeito de Vidro (Glassmorphism) */
    .app-card {{
        background: rgba(30, 41, 59, 0.7); /* Cinza azulado transparente */
        backdrop-filter: blur(10px); /* O desfoque que cria o efeito de vidro */
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-left: 4px solid #4ADE80;
        padding: 25px;
        margin-bottom: 20px;
        border-radius: 8px;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }}
    
    .app-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.3);
        border-color: #4ADE80;
    }}

    /* Estilização dos Botões */
    .stButton button {{
        background-color: transparent;
        color: #4ADE80;
        border: 1px solid #4ADE80;
        border-radius: 4px;
        font-family: 'Roboto Mono', monospace;
        letter-spacing: 1px;
        transition: all 0.3s;
    }}
    .stButton button:hover {{
        background-color: #4ADE80;
        color: #0F172A; /* Cor escura do fundo */
        box-shadow: 0 0 10px rgba(74, 222, 128, 0.4);
    }}
    
    /* Input de Senha */
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

    # Tela de Login Minimalista
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown(f"<div style='text-align: center; font-size: 2.5rem; letter-spacing: 2px;'>DEV.JUR <span class='highlight'>OS</span></div>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; opacity: 0.6; font-size: 0.8rem;'>SECURE ACCESS TERMINAL</p>", unsafe_allow_html=True)
    
    # Colunas para centralizar o input
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        password = st.text_input("PASSWORD", type="password", label_visibility="collapsed", placeholder="Insira a chave de acesso...")
        if st.button("AUTHENTICATE", use_container_width=True):
            if password == "admin": 
                st.session_state.password_correct = True
                st.rerun()
            else:
                st.error("ACCESS DENIED")
    return False

# --- Renderização do Dashboard ---
if check_password():
    # Cabeçalho
    st.markdown(f"""
    <div style='display:flex; justify-content:space-between; align-items:center; margin-bottom: 30px;'>
        <div>
            <span class='highlight'>STATUS:</span> ONLINE<br>
            <span style='font-size: 0.8rem; opacity: 0.7;'>SERVER: LOCALHOST</span>
        </div>
        <div style='text-align:right;'>
            DEV.JUR<br>
            <span style='font-size: 0.8rem; opacity: 0.7;'>V 2.1</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<h3 style='text-align: center; margin-bottom: 30px;'>SELECIONE O MÓDULO</h3>", unsafe_allow_html=True)

    for app in APPS:
        # Card Visual
        st.markdown(f"""
        <div class="app-card">
            <div style="font-size: 1.3rem; margin-bottom: 8px;">{app['icon']} <strong>{app['nome']}</strong></div>
            <p style="font-size: 0.9rem; opacity: 0.8; margin-bottom: 0;">{app['desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Botão Funcional
        if st.button(f"INICIAR SISTEMA", key=app['nome'], use_container_width=True):
             webbrowser.open_new_tab(app['url'])

    # Rodapé
    st.markdown("<br><br><div style='text-align: center; font-size: 0.7rem; opacity: 0.4; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 20px;'>CURATOR MODULE | DEV.JUR ARCHITECTURE</div>", unsafe_allow_html=True)