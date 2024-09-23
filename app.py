import streamlit as st
import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
    st.set_page_config(page_title='Binômio de Newton', page_icon="📐", layout="centered")
    st.title("Binômio de Newton Interativo")

    st.sidebar.title('Navegação')
    options = ["Teoria", "Calculadora", "Coeficientes", "Triângulo de Pascal", "Laboratório",
               "Passo a Passo", "Identificação de Binômios", "Exercícios"]
    choice = st.sidebar.radio("Escolha uma opção", options)

    if choice == "Teoria":
        teoria()
    elif choice == "Calculadora":
        calculadora()
    elif choice == "Coeficientes":
        coeficientes()
    elif choice == "Triângulo de Pascal":
        triangulo_pascal()
    elif choice == "Exercícios":
        exercicios_criativos()
    elif choice == "Laboratório":
        laboratorio_virtual()
    elif choice == "Passo a Passo":
        passo_a_passo()
    elif choice == "Identificação de Binômios":
        identificacao_binomios()
    st.write("Autores: João Renan S. Lopes E Pedro Girotto")
    st.write("Centro Universitário do Pará")

def teoria():
    st.header("Teoria do Binômio de Newton")
    st.subheader("O Básico e aplicações")

    st.write(r"""
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

    st.info("Dica: O Binômio de Newton é uma ferramenta poderosa para simplificar cálculos complexos em várias áreas da matemática e ciências aplicadas.")

def calculadora():
    st.header("Calculadora do Binômio de Newton")
    st.subheader("Expanda binômios interativamente")

    col1, col2 = st.columns(2)

    with col1:
        x = st.text_input("Primeiro termo (ex: x, 2*x, -y)", "x")
        y = st.text_input("Segundo termo (ex: y, 3, 2*z)", "y")
        n = st.slider("Expoente", 0, 10, 2)

    with col2:
        st.write("Expansão:")
        try:
            expansion = sp.expand((sp.sympify(x) + sp.sympify(y)) ** n)
            st.latex(sp.latex(expansion))

            st.write("Termos individuais:")
            terms = expansion.as_ordered_terms()
            for i, term in enumerate(terms):
                st.latex(f"Termo {i + 1}: {sp.latex(term)}")
        except sp.SympifyError:
            st.error("Erro: Um ou mais termos não puderam ser interpretados. Verifique as entradas e tente novamente.")

    st.subheader("Insight")
    st.write(f"A expansão de ({x} + {y})^{n} terá {n + 1} termos.")

def coeficientes():
    st.header("Coeficientes Binomiais")
    st.subheader("Explore os coeficientes do Binômio de Newton")

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

    st.info(f"Interpretação: Existem {coef} maneiras de escolher {k} itens de um conjunto de {n} itens.")

def triangulo_pascal():
    st.header("Triângulo de Pascal - Visualização Ampliada")

    rows = st.slider("Número de linhas", 1, 10, 7)

    triangle = [[1]]
    for i in range(1, rows):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_axis_off()

    for i, row in enumerate(triangle):
        for j, num in enumerate(row):
            ax.text(j - i / 2, -i, str(num), ha='center', va='center', fontweight='bold', fontsize=14)

            if i > 0:
                if j < len(row) - 1:
                    ax.plot([j - i / 2, j - i / 2 - 0.5], [-i, -(i - 1)], color='black', lw=1)
                if j > 0:
                    ax.plot([j - i / 2, j - i / 2 + 0.5], [-i, -(i - 1)], color='black', lw=1)

    plt.title("Triângulo de Pascal", fontsize=18)
    st.pyplot(fig)

    st.subheader("Fatos Curiosos")
    st.write("1. As somas das linhas são potências de 2: 1, 2, 4, 8, 16, 32, ...")
    st.write("2. Os números nas diagonais formam os números de Fibonacci.")
    st.write("3. O triângulo contém padrões fractais como o Triângulo de Sierpinski.")

def exercicios_criativos():
    st.header("Exercícios Criativos")
    st.subheader("Hora da verdade!")

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

    st.success("Parabéns por enfrentar esses desafios! Lembre-se, a prática leva à perfeição em matemática. Abraços do monitor!")

def laboratorio_virtual():
    st.header("Laboratório Virtual")
    st.subheader("Experimente com o Binômio de Newton")

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

    st.subheader("Desafio do Laboratório")
    st.write("Tente ajustar os parâmetros para criar uma função que:")
    challenge = random.choice([
        "Tenha três raízes reais",
        "Seja sempre positiva",
        "Tenha um ponto de inflexão",
        "Seja simétrica em relação ao eixo y"
    ])
    st.info(challenge)

def passo_a_passo():
    st.header("Passo a Passo")
    st.subheader("Como expandir e simplificar um binômio")

    st.write(r"""
    Antes de iniciar a parte interativa, é importante entender detalhadamente como expandir um binômio passo a passo.

    ### Entendendo o Binômio de Newton

    O Binômio de Newton é uma fórmula que permite expandir potências de binômios. A fórmula geral é:

    $$(x + y)^n = \sum_{k=0}^n \binom{n}{k} x^{n-k} y^k$$

    Onde:
    - $n$ é o expoente do binômio
    - $k$ é o índice da soma, variando de 0 a n
    - $\binom{n}{k}$ é o coeficiente binomial, também conhecido como "n escolhe k"

    ### Passo a Passo para Expandir um Binômio

    Utiliza-se o exemplo $(a + b)^3$ para ilustrar o processo:

    1. Identificação dos valores de $n$, $x$, e $y$:
       - $n = 3$
       - $x = a$
       - $y = b$

    2. Aplicação da fórmula para cada valor de $k$ de 0 a $n$:

       - Para $k = 0$: $\binom{3}{0} a^3 b^0 = 1 \cdot a^3 \cdot 1 = a^3$
       - Para $k = 1$: $\binom{3}{1} a^2 b^1 = 3 \cdot a^2 \cdot b = 3a^2b$
       - Para $k = 2$: $\binom{3}{2} a^1 b^2 = 3 \cdot a \cdot b^2 = 3ab^2$
       - Para $k = 3$: $\binom{3}{3} a^0 b^3 = 1 \cdot 1 \cdot b^3 = b^3$

    3. Soma de todos os termos:

       $(a + b)^3 = a^3 + 3a^2b + 3ab^2 + b^3$

    Este é o resultado final da expansão.

    ### Pontos Importantes a Serem Lembrados

    - O número de termos na expansão será sempre $n + 1$.
    - Os expoentes de $x$ diminuem de $n$ até 0, enquanto os de $y$ aumentam de 0 até $n$.
    - Os coeficientes binomiais $\binom{n}{k}$ formam o Triângulo de Pascal.

    Após compreender o processo, pode-se praticar com alguns exemplos interativos.
    """)

    col1, col2 = st.columns(2)

    with col1:
        x = st.text_input("Primeiro termo (ex: x, 2*x, -y)", "x")
        y = st.text_input("Segundo termo (ex: y, 3, 2*z)", "2")
        n = st.slider("Expoente", 1, 5, 3)

    with col2:
        st.write(f"Expandindo: $({x} + {y})^{n}$")

    if st.button("Expandir passo a passo"):
        try:
            x_sym, y_sym = sp.symbols('x y')
            expr = (sp.sympify(x) + sp.sympify(y)) ** n
            expansion = sp.expand(expr)

            st.write("### Passos da expansão:")
            for k in range(n + 1):
                term = sp.binomial(n, k) * sp.sympify(x) ** (n - k) * sp.sympify(y) ** k
                st.latex(rf"\binom{{{n}}}{{{k}}} \cdot ({x})^{{{n - k}}} \cdot ({y})^{{{k}}} = {sp.latex(term)}")

            st.write("### Resultado final:")
            st.latex(sp.latex(expansion))
        except sp.SympifyError:
            st.error(
                "Erro ao processar a expressão. É necessário usar '*' para multiplicação (ex: 2*x em vez de 2x).")

    st.info("Experimente com diferentes termos e expoentes para observar como a expansão se modifica.")

    # Seção de exercícios interativos
    st.subheader("Exercícios Interativos")

    exercise_type = st.radio("Escolha o tipo de exercício:", ["Expansão", "Coeficiente Específico"])

    if exercise_type == "Expansão":
        a, b = random.randint(1, 5), random.randint(1, 5)
        n = random.randint(2, 4)
        expr = sp.expand((a * sp.Symbol('x') + b) ** n)
        st.write('Expanda')
        st.latex(rf"({a}x + {b})^{{{n}}}")
        user_answer = st.text_input("Resposta:")

        if st.button("Verificar"):
            try:
                if sp.expand(sp.sympify(user_answer)) == expr:
                    st.success("Correto! A resposta está precisa.")
                else:
                    st.error("Incorreto. É recomendável tentar novamente.")
            except:
                st.error("Erro ao processar a resposta. Verifique a sintaxe.")

        if st.button("Mostrar solução"):
            st.write("A expansão é:")
            st.latex(sp.latex(expr))

    elif exercise_type == "Coeficiente Específico":
        a, b = random.randint(1, 5), random.randint(1, 5)
        n = random.randint(4, 6)
        k = random.randint(1, n - 1)
        coef = sp.binomial(n, k) * a ** (n - k) * b ** k

        st.write('Qual é o coeficiente de')
        st.latex(rf"x^{{{n - k}}} \text{{ na expansão de }} ({a}x + {b})^{{{n}}}")
        user_answer = st.number_input("Resposta:", step=1)

        if st.button("Verificar"):
            if user_answer == coef:
                st.success("Correto! A resposta está precisa.")
            else:
                st.error("Incorreto. É recomendável tentar novamente.")

        if st.button("Mostrar solução"):
            st.write("O coeficiente é:")
            st.latex(rf"\binom{{{n}}}{{{k}}} \cdot {a}^{{{n - k}}} \cdot {b}^{{{k}}} = {coef}")

def identificacao_binomios():
    st.header("Identificação de Binômios")
    st.subheader("Como identificar binômios de expressões expandidas")

    st.write(r"""
    Antes de praticar a identificação de binômios, é importante entender o processo de como reconhecer um binômio expandido e reduzi-lo à sua forma original.

    ### Processo de Identificação de Binômios

    1. **Observação do grau**: O maior expoente na expressão expandida será o expoente do binômio original.

    2. **Identificação dos termos**: Em um binômio $(ax + b)^n$, encontram-se:
       - Um termo com $x^n$
       - Um termo constante (sem $x$)
       - Termos intermediários com potências de $x$ decrescendo de $n-1$ até 1

    3. **Determinação de $a$ e $b$**:
       - $a$ é a raiz n-ésima do coeficiente de $x^n$
       - $b$ é a raiz n-ésima do termo constante

    4. **Verificação dos coeficientes**: Os coeficientes devem seguir o padrão do Triângulo de Pascal multiplicado por potências de $a$ e $b$.

    ### Exemplo Detalhado

    Identificação do binômio original para a expressão: $x^3 + 6x^2 + 12x + 8$

    1. **Grau**: O maior expoente é 3, então $n = 3$.

    2. **Termos**: Presença de $x^3$, $x^2$, $x$, e um termo constante. A expressão está completa.

    3. **Determinação de $a$ e $b$**:
       - Coeficiente de $x^3$ é 1, então $a = 1$
       - Termo constante é 8, então $b = 2$ (pois $2^3 = 8$)

    4. **Verificação dos coeficientes**:
       - $\binom{3}{0} = 1$ (coeficiente de $x^3$)
       - $\binom{3}{1} \cdot 2 = 3 \cdot 2 = 6$ (coeficiente de $x^2$)
       - $\binom{3}{2} \cdot 2^2 = 3 \cdot 4 = 12$ (coeficiente de $x$)
       - $\binom{3}{3} \cdot 2^3 = 1 \cdot 8 = 8$ (termo constante)

    Portanto, o binômio original é $(x + 2)^3$.

    ### Dicas para Identificação

    - Se o coeficiente de $x^n$ não for 1, divide-se todos os termos por este coeficiente primeiro.
    - Atenção aos sinais: se há alternância de sinais, provavelmente o segundo termo do binômio é negativo.
    - Utiliza-se o Triângulo de Pascal para verificar se os coeficientes seguem o padrão esperado.

    Após compreender o processo de identificação, pode-se praticar com alguns exemplos interativos.
    """)

    # Lista de binômios pré-definidos
    binomios = [
        ("x + 1", 2),
        ("x - 2", 3),
        ("2*x + 3", 2),
        ("3*x - 1", 3),
        ("x + y", 2)
    ]

    # Escolha aleatória de um binômio
    x, y = sp.symbols('x y')
    binomio, expoente = random.choice(binomios)
    try:
        expr = sp.expand((sp.sympify(binomio)) ** expoente)
    except sp.SympifyError:
        st.error("Erro ao processar o binômio. É necessário recarregar a página.")
        return

    st.subheader(f"Identifique o binômio original da expressão:")
    st.latex(sp.latex(expr))

    col1, col2 = st.columns(2)

    with col1:
        user_binomio = st.text_input("Digite o binômio que se acredita ser o correto (ex: x+1)", "")
    with col2:
        user_expoente = st.number_input("Digite o expoente", 1, 5, 2)

    if st.button("Verificar"):
        if user_binomio and user_expoente:
            try:
                user_expr = sp.expand((sp.sympify(user_binomio)) ** user_expoente)
                if user_expr == expr:
                    st.success("Correto! O binômio original foi identificado corretamente.")
                else:
                    st.error("Incorreto. É recomendável tentar novamente.")
                    st.write("Dica: Observe atentamente os coeficientes e os termos constantes.")
            except sp.SympifyError:
                st.error("Erro ao processar a resposta. Verifique a sintaxe e use '*' para multiplicação.")
        else:
            st.warning("É necessário preencher o binômio e o expoente antes de verificar.")

    if st.button("Revelar resposta"):
        st.write("O binômio original era:")
        st.latex(rf"({binomio})^{{{expoente}}}")

    st.success("Continue praticando para aprimorar as habilidades de identificação de binômios.")

    # Seção de exercícios interativos
    st.subheader("Exercícios Interativos de Identificação")

    difficulty = st.radio("Escolha o nível de dificuldade:", ["Nivel 1", "Nivel 2", "Nivel 3"])

    if difficulty == "Nivel 1":
        a, b = random.randint(1, 5), random.randint(1, 5)
        n = 2
    elif difficulty == "Nivel 2":
        a, b = random.randint(1, 10), random.randint(1, 10)
        n = 3
    else:
        a, b = random.randint(1, 15), random.randint(1, 15)
        n = 4

    expr = sp.expand((a * sp.Symbol('x') + b) ** n)

    st.write("Identifique o binômio e o expoente para a seguinte expressão expandida:")
    st.latex(sp.latex(expr))

    col1, col2 = st.columns(2)
    with col1:
        user_a = st.number_input("Coeficiente de x:", step=1)
        user_b = st.number_input("Termo constante:", step=1)
    with col2:
        user_n = st.number_input("Expoente:", min_value=1, step=1)

    if st.button("Verificar identificação"):
        if user_a == a and user_b == b and user_n == n:
            st.success("Correto! O binômio original foi identificado perfeitamente.")
        else:
            st.error("Incorreto. Recomenda-se analisar a expressão mais cuidadosamente.")

    if st.button("Mostrar binômio original"):
        st.write("O binômio original é:")
        st.latex(rf"({a}x + {b})^{{{n}}}")

if __name__ == "__main__":
    main()
