import streamlit as st

# Defina a senha
senha_correta = "COMPARTILHEOSITE"

# Solicita a senha ao usuário
senha_digitada = st.text_input("Digite a senha:", type="password")

# Verifica se a senha está correta e libera o acesso
if senha_digitada == senha_correta:
    st.write("Senha correta. Você pode acessar o site.")
    # Restante do código do seu site
    st.title('CALCULOS DE TEORIA DE CONUNTO USANDO A FORMULA(A UNIAO B) #A+#B+#C+# (A INTERSEÇAO B) ')


    def conjunto():
        n = st.number_input('Número total de pessoas:', min_value=0)
        a = st.number_input('Número de pessoas que fazem uma coisa(A):', min_value=0, max_value=n)
        b = st.number_input('Número de pessoas que fazem outra coisa(B):', min_value=0, max_value=n)
        c = st.number_input('Número de pessoas que fazem algumas coisas(C):', min_value=0, max_value=n)

        # Cálculo da fórmula principal
        intersection = a + b + c - n

        # Cálculo de pessoas que fazem apenas uma coisa (A)
        a_only = a - intersection

        # Cálculo de pessoas que fazem outras coisas (B)
        b_only = b - intersection

        # Cálculo de pessoas que fazem algumas coisas (C)
        c_only = c - intersection

        # Apresentando os resultados
        st.write('O número de pessoas que fazem as duas coisas é:', intersection)
        st.write('O número de pessoas que fazem apenas uma coisa (A) é:', a_only)
        st.write('O número de pessoas que fazem outras coisas (B) é:', b_only)
        st.write('O número de pessoas que fazem algumas coisas (C) é:', c_only)
        st.write('---')


    # Chamada da função para o site Streamlit
    conjunto()

    st.write(
        'SE A PERGUNTA DO SEU CALCULO CONTER 4 VALORES,TOTAL,QUE FAZEM 1 COISA(A), OUTRA COISA(B),E ALGUMAS COISAS(C),'
        'PODE INSERIR O VALOR DE C, SE SO TIVER 3 VALORES INSIRA OS ATE O VALOR DE B E O VALOR DE C DEIXE NO 0,E TIRE '
        'SOMENTE O VALOR DE A E B DOS RESULTADOS')

else:
    st.write("Senha incorreta. Acesso negado.")
