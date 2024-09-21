import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import random
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.stylable_container import stylable_container
import time


def main():

    st.set_page_config(page_title="Binômio de Newton Interativo", page_icon="📐", layout="centered")

    st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
    }
    .stTextInput>div>div>input {
        background-color: #e8f0fe;
    }
    </style>
    """, unsafe_allow_html=True)

    st.sidebar.title('📚 Navegação')
    options = ["🧠 Teoria", "🔢 Calculadora", "🎲 Coeficientes", "🔺 Triângulo de Pascal", "💡 Exercícios", "🧪 Laboratório"]
    choice = st.sidebar.radio("Escolha uma opção", options)

    if choice == "🧠 Teoria":
        teoria()
    elif choice == "🔢 Calculadora":
        calculadora()
    elif choice == "🎲 Coeficientes":
        coeficientes()
    elif choice == "🔺 Triângulo de Pascal":
        triangulo_pascal()
    elif choice == "💡 Exercícios":
        exercicios_criativos()
    elif choice == "🧪 Laboratório":
        laboratorio_virtual()
    st.write("Autores: João Renan S. Lopes E Pedro Girotto")
    st.write("Centro Universitário do Pará")

def teoria():
    colored_header(label="Teoria do Binômio de Newton", description="O Básico e aplicações", color_name="green-70")

    st.write("""
    O Binômio de Newton é uma expressão algébrica que permite expandir potências de binômios de forma eficiente. 
    A fórmula geral para $(x + y)^n$ é:
    """)

    st.latex(r"(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k")

    st.write(r"""
    Onde:
    - $n$ é o expoente do binômio
    - $k$ é o índice da soma, variando de 0 a n
    - $\binom{n}{k}$ é o coeficiente binomial, também conhecido como "n escolhe k"

    O coeficiente binomial $\binom{n}{k}$ representa o número de maneiras de escolher $k$ itens de um conjunto de $n$ itens, e é calculado como:
    """)

    st.latex(r"\binom{n}{k} = \frac{n!}{k!(n-k)!}")

    st.write("""
    Aplicações do Binômio de Newton incluem:
    1. Expansão de expressões algébricas
    2. Cálculo de probabilidades em distribuições binomiais
    3. Aproximações em física e engenharia
    4. Teoria dos números e criptografia
    """)

    st.subheader("Exemplo 1: Expansão de $(x + 1)^3$")
    if st.button("Mostrar solução exemplo 1"):
        st.latex(r"(x + 1)^3 = x^3 + 3x^2 + 3x + 1")

    st.subheader("Exemplo 2: Expansão de $(2x + y)^4$")
    if st.button("Mostrar solução exemplo 2"):
        st.latex(r"(2x + y)^4 = 16x^4 + 32x^3y + 24x^2y^2 + 8xy^3 + y^4")

    add_vertical_space(2)
    st.info("💡 Dica: O Binômio de Newton é uma ferramenta poderosa para simplificar cálculos complexos em várias áreas da matemática e ciências aplicadas.")


def calculadora():
    colored_header(label="Calculadora do Binômio de Newton", description="Expanda binômios interativamente", color_name="blue-70")

    col1, col2 = st.columns(2)

    with col1:
        x = st.text_input("Primeiro termo (ex: x, 2x, -y)", "x")
        y = st.text_input("Segundo termo (ex: y, 3, 2z)", "y")
        n = st.slider("Expoente", 0, 10, 2)

    with col2:
        st.write("Expansão:")
        try:
            # Tenta converter as entradas para expressões simbólicas
            expansion = sp.expand((sp.sympify(x) + sp.sympify(y)) ** n)
            st.latex(sp.latex(expansion))

            st.write("Termos individuais:")
            terms = expansion.as_ordered_terms()
            for i, term in enumerate(terms):
                st.latex(f"Termo {i + 1}: {sp.latex(term)}")
        except sp.SympifyError:
            st.error("Erro: Um ou mais termos não puderam ser interpretados. Verifique as entradas e tente novamente.")

    add_vertical_space(2)

    with stylable_container(
            key="expansion_insight",
            css_styles="""
            {
                background-color: #e6f3ff;
                border: 1px solid #b3d9ff;
                border-radius: 10px;
                padding: 20px;
            }
            """
    ):
        st.markdown("### 🔍 Insight")
        st.write(f"A expansão de $({x} + {y})^{n}$ terá {n + 1} termos.")


def coeficientes():
    colored_header(label="Coeficientes Binomiais", description="Explore os coeficientes do Binômio de Newton", color_name="orange-70")

    col1, col2 = st.columns(2)

    with col1:
        n = st.number_input("n", 0, 20, 5)
        k = st.number_input("k", 0, n, 2)

        coef = sp.binomial(n, k)
        st.write(f"O coeficiente binomial $\\binom{{{n}}}{{{k}}}$ é:")
        st.latex(sp.latex(coef))

    with col2:
        st.write("Visualização:")
        fig, ax = plt.subplots()
        x = range(n + 1)
        y = [sp.binomial(n, i) for i in x]
        ax.bar(x, y)
        ax.set_title(f"Coeficientes Binomiais para n={n}")
        ax.set_xlabel("k")
        ax.set_ylabel("Coeficiente")
        st.pyplot(fig)

    add_vertical_space(2)
    st.info(f"💡 Interpretação: Existem {coef} maneiras de escolher {k} itens de um conjunto de {n} itens.")


def triangulo_pascal():
    st.title("Triângulo de Pascal - Visualização Ampliada")
    
    rows = st.slider("Número de linhas", 1, 20, 7)  # Permitindo até 20 linhas para melhorar a visualização

    # Gerar o Triângulo de Pascal
    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    # Preparar a visualização
    fig, ax = plt.subplots(figsize=(10, 8))  # Aumentando o tamanho da figura
    ax.set_axis_off()

    # Definir a distância entre os pontos e centralizar melhor
    for i, row in enumerate(triangle):
        for j, num in enumerate(row):
            ax.text(j - i / 2, -i, str(num), ha='center', va='center', fontweight='bold', fontsize=14)  # Aumentando o tamanho da fonte
            
            # Desenhar linhas conectando os números para criar o formato de triângulo
            if i > 0:
                if j < len(row) - 1:
                    ax.plot([j - i / 2, j - i / 2 - 0.5], [-i, -(i - 1)], color='black', lw=1)
                if j > 0:
                    ax.plot([j - i / 2, j - i / 2 + 0.5], [-i, -(i - 1)], color='black', lw=1)

    plt.title("Triângulo de Pascal", fontsize=18)  # Aumentando o tamanho do título
    st.pyplot(fig)

    add_vertical_space(2)

    with stylable_container(
            key="pascal_facts",
            css_styles="""
            {
                background-color: #fff0f5;
                border: 1px solid #ffb3d9;
                border-radius: 10px;
                padding: 20px;
            }
            """
    ):
        st.markdown("### 🌟 Fatos Curiosos")
        st.write("1. As somas das linhas são potências de 2: 1, 2, 4, 8, 16, 32, ...")
        st.write("2. Os números nas diagonais formam os números de Fibonacci.")
        st.write("3. O triângulo contém padrões fractais como o Triângulo de Sierpinski.")


def exercicios_criativos():
    colored_header(label="Exercícios Criativos", description="Teste seus conhecimentos de forma divertida", color_name="violet-70")

    exercises = [
        {
            "question": "Um jardim tem formato de triângulo equilátero. Se a cada ano o jardineiro aumenta o comprimento de cada lado em 1 metro, quantos metros quadrados o jardim terá aumentado após 3 anos?",
            "solution": r"""
            Seja $s$ o comprimento inicial do lado do jardim.
            A área de um triângulo equilátero é dada por $A = \frac{\sqrt{3}}{4}s^2$.

            Após 3 anos, o lado será $s+3$.
            O aumento na área será:

            $\Delta A = \frac{\sqrt{3}}{4}((s+3)^2 - s^2)$

            $\Delta A = \frac{\sqrt{3}}{4}(s^2 + 6s + 9 - s^2)$

            $\Delta A = \frac{\sqrt{3}}{4}(6s + 9)$

            $\Delta A = \frac{3\sqrt{3}}{2}s + \frac{9\sqrt{3}}{4}$

            Este é o aumento em metros quadrados após 3 anos.
            """
        },
        {
            "question": "Um vírus se multiplica a cada hora, dobrando sua população. Se inicialmente havia 100 vírus, quantos haverá após 8 horas?",
            "solution": r"""
            Este é um problema de crescimento exponencial que pode ser resolvido usando o Binômio de Newton.

            A população após n horas será: $100 \cdot 2^n$

            Para n = 8:

            $100 \cdot 2^8 = 100 \cdot 256 = 25.600$

            Portanto, após 8 horas, haverá 25.600 vírus.
            """
        },
        {
            "question": "Em um jogo de dados, qual é a probabilidade de obter exatamente 3 números pares em 5 lançamentos?",
            "solution": r"""
            Este é um problema de probabilidade binomial.

            A probabilidade de obter um número par em um lançamento é 3/6 = 1/2.

            Usamos o Binômio de Newton com n = 5 (total de lançamentos) e k = 3 (número de sucessos desejados).

            $P(X = 3) = \binom{5}{3} (1/2)^3 (1/2)^2$

            $= 10 \cdot (1/8) \cdot (1/4) = 10/32 = 5/16$

            A probabilidade é 5/16 ou aproximadamente 0,3125 ou 31,25%.
            """
        },
        {
            "question": "Qual a expansão de $(3x + 2)^5$?",
            "solution": r"""
            A expansão de $(3x + 2)^5$ é:

            $ = 243x^5 + 810x^4 + 1080x^3 + 720x^2 + 240x + 32$
            """
        }
    ]

    for i, exercise in enumerate(exercises):
        with st.expander(f"Exercício {i + 1}"):
            st.write(exercise["question"])
            if st.button(f"Mostrar solução {i + 1}"):
                st.write(exercise["solution"])

    add_vertical_space(2)

    st.success("🏆 Parabéns por enfrentar esses desafios! Lembre-se, a prática leva à perfeição em matemática. Abraços do monitor!")


def laboratorio_virtual():
    colored_header(label="Laboratório Virtual", description="Experimente com o Binômio de Newton", color_name="blue-green-70")

    st.write("""
    Bem-vindo ao Laboratório Virtual do Binômio de Newton! 
    Aqui você pode explorar como diferentes parâmetros afetam a expansão do binômio.
    """)

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input("Coeficiente de x", -10.0, 10.0, 1.0, 0.1)
        b = st.number_input("Termo constante", -10.0, 10.0, 1.0, 0.1)
        n = st.slider("Expoente", 1, 10, 2)

    x = sp.Symbol('x')
    expansion = sp.expand((a * x + b) ** n)

    with col2:
        st.write("Expansão:")
        st.latex(sp.latex(expansion))

        st.write("Gráfico da função:")
        x_vals = np.linspace(-2, 2, 100)
        y_vals = [expansion.subs(x, val) for val in x_vals]

        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals)
        ax.set_title(f"Gráfico de ({a}x + {b})^{n}")
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True)
        st.pyplot(fig)

    add_vertical_space(2)

    with stylable_container(
            key="lab_challenge",
            css_styles="""
            {
                background-color: #f0fff0;
                border: 1px solid #90ee90;
                border-radius: 10px;
                padding: 20px;
            }
            """
    ):
        st.markdown("### 🧪 Desafio do Laboratório")
        st.write("Tente ajustar os parâmetros para criar uma função que:")
        challenge = random.choice([
            "Tenha três raízes reais",
            "Seja sempre positiva",
            "Tenha um ponto de inflexão",
            "Seja simétrica em relação ao eixo y"
        ])
        st.info(challenge)


if __name__ == "__main__":
    main()
