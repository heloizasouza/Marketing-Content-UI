import streamlit as st

# Configuracoes da pagina
st.set_page_config(
    page_title="DEX-MarktGen",
    page_icon="🎯",  # You can use an emoji or a custom icon
    layout="wide",  # Options: 'centered', 'wide'
    initial_sidebar_state="expanded",  # Options: 'auto', 'expanded', 'collapsed'
    menu_items={
        'Get Help': 'https://docs.streamlit.io/',
        'Report a Bug': 'https://github.com/streamlit/streamlit/issues',
        'About': "This is a sample Streamlit app to demonstrate page configuration."
    }
)

# Configuracoes da barra lateral
st.sidebar.title("Menu")
#st.sidebar.write("Configurações base para o prompt:")
st.sidebar.selectbox("Tipo de publicação", ["Post Instagram", "Stories Instagram", "Post Linkedin", "Roteiro TikTok"])
st.sidebar.radio("Público alvo", ["Todos", "Universitários", "Jovem empreendedor", "Apaixonados por tecnologia"], help="Selecione a persona do público alvo para o qual deseja gerar o conteúdo.")
st.sidebar.color_picker("Pick a color", "#8953F9", help="Escolha a cor base do post.")

# Configuracoes do conteudo principal
st.title("Gerador de conteúdos de Marketing DEX 🤖")
#st.write("Chatbot de geração de conteúdos para mídias sociais DEX.")

# Inicializa o historico do chat
if "messages" not in st.session_state:
    st.session_state.messages = []
# Exibe o historico do chat
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])
# Entrada de mensagem do usuario
if prompt := st.chat_input("Digite sua mensagem:"):
    # Adiciona a mensagem do usuario ao historico
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Exibe a mensagem do usuario
    st.chat_message("user").write(prompt)
    
    # Adiciona a lógica para processar a mensagem e gerar uma resposta
    response = f"Resposta gerada para: {prompt}"  # Simulação de resposta
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Exibe a resposta do assistente
    st.chat_message("assistant").write(response)