import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

# Configurações de tema para o app
st.set_page_config(page_title="Teste de Nível de Inglês", page_icon="🌍", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
        }
    </style>
    """, unsafe_allow_html=True)

# Código CSS para adicionar o background
st.markdown(
    """
    <style>
    .stApp {
        background-image: url('https://github.com/sid-almeida/english_test/blob/main/englishbackground.png?raw=true');
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Logo da Igreja (adicione a imagem da logo na mesma pasta do código) centralizado
logo = "https://github.com/sid-almeida/english_test/blob/main/ldslogo22.png?raw=true"
st.image(logo, width=350)


# Inicializar estado da sessão para gerenciar respostas
if "responses" not in st.session_state:
    st.session_state.responses = {i: None for i in range(1, 19)}  # Ajustado para 18 perguntas
if "locked" not in st.session_state:
    st.session_state.locked = {i: False for i in range(1, 19)}  # Ajustado para 18 perguntas
if "test_completed" not in st.session_state:
    st.session_state.test_completed = False


def main():

    st.markdown("<h1 style='text-align: center;'>Teste de Nível de Inglês</h1>", unsafe_allow_html=True)

    # Sessão para inserir o nome do aluno
    aluno_nome = st.text_input("Por favor, insira seu nome:", key="aluno_nome")

    if aluno_nome:
        st.write(
            f"Bem-vindo, {aluno_nome}! Este teste contém 18 perguntas. Leia cada questão, selecione a resposta correta e clique em 'Responder' para enviar. Após concluir todas as questões, clique em 'Concluir' no final do teste.")

        # Variável de pontuação
        score = 0

        # Função para criar uma pergunta
        def create_question(q_num, question, options, correct_option):
            # Exibe a pergunta
            st.write(f"**Pergunta {q_num}:** {question}")
            if st.session_state.locked[q_num]:
                st.write(f"Resposta enviada: {st.session_state.responses[q_num]}")
            else:
                # Exibe as opções
                selected_option = st.radio(
                    f"Selecione uma resposta para a pergunta {q_num}:",
                    options,
                    index=options.index(st.session_state.responses[q_num]) if st.session_state.responses[q_num] else 0,
                    key=f"q_{q_num}"
                )

                # Botão "Responder"
                if st.button(f"Responder Pergunta {q_num}", key=f"btn_q{q_num}"):
                    st.session_state.responses[q_num] = selected_option
                    st.session_state.locked[q_num] = True
                    st.success(f"Resposta da Pergunta {q_num} enviada com sucesso!")

        # Perguntas de Gramática
        st.header("Gramática")
        create_question(1, "Complete a frase: She ___ to the store every day.", ["go", "goes", "going"], "goes")
        create_question(2, "Escolha a frase correta: Ele não gosta de pizza.",
                        ["He don't like pizza.", "He doesn't like pizza."], "He doesn't like pizza.")
        create_question(3, "Complete a frase: They ___ playing soccer now.", ["is", "are", "am"], "are")
        create_question(4, "Escolha a frase correta: Eu vi ele todos os dias.",
                        ["I seen him yesterday.", "I saw him yesterday."], "I saw him yesterday.")
        create_question(5, "Complete: If I ___ you, I would go.", ["was", "were", "am"], "were")
        create_question(6, "Qual é a pergunta correta: Ela pode cantar?", ["Can she sing?", "She can sing?"],
                        "Can she sing?")
        create_question(7, "Complete: I have lived here ___ five years.", ["since", "for", "from"], "for")
        create_question(8, "Escolha a frase correta: Ela tem um carro novo.",
                        ["She has a new car.", "She have a new car."],
                        "She has a new car.")

        # Perguntas de Vocabulário
        st.header("Vocabulário")
        create_question(9, "Qual é o oposto de 'happy'?", ["Sad", "Angry", "Excited"], "Sad")
        create_question(10, "Escolha a palavra que significa 'rápido':", ["Slow", "Fast", "Lazy"], "Fast")
        create_question(11, "Qual palavra é uma fruta?", ["Carrot", "Apple", "Lettuce"], "Apple")
        create_question(12, "O que significa 'bookstore' em português?", ["Biblioteca", "Livraria", "Papelaria"],
                        "Livraria")
        create_question(13, "Escolha a tradução correta para 'janela':", ["Door", "Window", "Roof"], "Window")
        create_question(14, "O que significa 'to run' em português?", ["Caminhar", "Pular", "Correr"], "Correr")

        # Perguntas de Compreensão de Leitura
        st.header("Compreensão de Leitura")
        st.write("Leia o texto e responda as perguntas:")
        texto = """
        Mary loves reading books. Every weekend, she goes to the library to find new stories. 
        Her favorite genre is mystery, and she enjoys solving puzzles along with the characters.
        """
        st.write(texto)
        create_question(15, "O que a Mary ama fazer?", ["Write books", "Read books", "Watch movies"], "Read books")
        create_question(16, "Onde a Mary vai todo fim de semana?",
                        ["To the bookstore", "To the library", "To the park"],
                        "To the library")
        create_question(17, "Qual o gênero favorito de Mary?", ["Romance", "Mystery", "Science fiction"], "Mystery")
        create_question(18, "O que ela gosta de fazer com os personagens?",
                        ["Solving puzzles", "Falling in love", "Traveling"], "Solving puzzles")

        # Botão "Concluir"
        if not st.session_state.test_completed:
            if st.button("Concluir Teste", key="concluir_btn", use_container_width=True):
                st.session_state.test_completed = True
                # Calcular pontuação
                for i, correct_answer in zip(range(1, 19), [
                    "goes", "He doesn't like pizza.", "are", "I saw him yesterday.", "were", "Can she sing?",
                    "for", "She has a new car.", "Sad", "Fast", "Apple", "Livraria", "Window", "Correr",
                    "Read books", "To the library", "Mystery", "Solving puzzles"]):
                    if st.session_state.responses[i] == correct_answer:
                        score += 1

                # Nível baseado na pontuação
                if score >= 18:
                    nivel = "Intermediário (B1/B2)"
                elif score >= 12:
                    nivel = "Básico (A2)"
                else:
                    nivel = "Iniciante (A1)"

                st.success(f"Teste concluído! Seu nível é {nivel}. Pontuação: {score}/18")

                # Gerar imagem com o resultado
                img = Image.new("RGB", (500, 300), color="white")
                draw = ImageDraw.Draw(img)
                font = ImageFont.load_default()
                draw.text((20, 20), f"Resultado do Teste de Ingles", fill="black")
                draw.text((20, 50), f"Nome: {aluno_nome}", fill="black")
                draw.text((20, 80), f"Pontuacao: {score}/18", fill="black")
                draw.text((20, 110), f"Nivel: {nivel}", fill="black")
                buffer = io.BytesIO()
                img.save(buffer, format="PNG")
                st.image(img, caption="Resultado")
                st.download_button("Baixar Resultado", data=buffer.getvalue(),
                                   file_name=f"resultado_teste_ingles_{aluno_nome}.png",
                                   mime="image/png")


main()
