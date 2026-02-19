import streamlit as st

# Configuração da aba do navegador
st.set_page_config(
    page_title="Fechamento de Caixa",
    page_icon="💰",
    layout="centered"
)

# Título Principal
st.title("💰 Calculadora de Fechamento")
st.write("Ferramenta para conferência de caixa bancário.")

# --- BARRA LATERAL (MENU) ---
menu = st.sidebar.selectbox("Escolha a Opção", ["Fechar Caixa", "Sobre"])

if menu == "Fechar Caixa":
    st.markdown("---")

    # ENTRADA DE DADOS
    # O Streamlit já trata a vírgula/ponto automaticamente nos number_input
    col1, col2 = st.columns(2)

    with col1:
        inicio = st.number_input("Inicio",
                                 min_value=0.0, step=0.01, format="%.2f")
        relatorio = st.number_input(
            "Fechamento", step=0.01, format="%.2f")

    with col2:
        final = st.number_input(
            "Caixa", min_value=0.0, step=0.01, format="%.2f")

    # BOTÃO DE CALCULAR
    if st.button("Verificar Diferença", type="primary"):

        # LÓGICA MATEMÁTICA
        saldo_esperado = inicio + relatorio
        diferenca = final - saldo_esperado

        # EXIBIÇÃO DO RESULTADO
        st.markdown("### Resultado:")

        # Usamos uma margem de erro muito pequena (0.001) para evitar erros de arredondamento
        if abs(diferenca) < 0.01:
            st.success("✅ CAIXA BATIDO! Parabéns.")
            st.metric(label="Diferença", value="R$ 0.00")

        elif diferenca > 0:
            st.warning("⚠️ SOBRA DE CAIXA (Atenção)")
            st.metric(label="Valor Sobrando", value=f"R$ {diferenca:.2f}")

        else:
            st.error("❌ QUEBRA DE CAIXA (Falta)")
            # Mostra o valor positivo para ficar mais fácil de ler
            st.metric(label="Valor Faltando", value=f"R$ {-diferenca:.2f}")

elif menu == "Sobre":
    st.subheader("Sobre o Projeto")
    st.write(
        "Projeto desenvolvido por estudante de ADS para automação de conferência bancária.")

