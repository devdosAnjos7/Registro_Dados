import streamlit as st
import datetime

# Configuração da página
st.title('Registro de Dados Pessoais')
st.write('Preencha as informações abaixo para registrar seus dados pessoais.')

# Data de hoje
hoje = datetime.date.today()
# Limite de 100 anos atrás (considerando anos bissextos corretamente)
min_date = hoje.replace(year=hoje.year - 100)
# Máximo é hoje (não pode escolher no futuro)
max_date = hoje

# Campos de entrada para os dados pessoais
nome = st.text_input('Digite seu Nome')
endereco = st.text_input('Digite seu Endereço')
dt_nascimento = st.date_input(
    'Escolha a Data de Nascimento',
    min_value=min_date,
    max_value=max_date
)

sexo = st.selectbox('Selecione o Sexo', ['Masculino', 'Feminino', 'Outro'])
telefone = st.text_input('Digite seu Telefone')
email = st.text_input('Digite seu Email')

# Verificação de campos obrigatórios
if nome and endereco and dt_nascimento and sexo and telefone and email:
    # Exibir mensagem de sucesso    
    st.success('Todos os campos foram preenchidos corretamente!')
else:
    # Exibir mensagem de erro    
    st.error('Por favor, preencha todos os campos obrigatórios.')   

# Botão para salvar os dados   
salvar_dados = st.button('Salvar Dados')
if salvar_dados:
    with open('dados_pessoais.txt', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'Nome: {nome}, Endereço: {endereco}, Data de Nascimento: {dt_nascimento}, Sexo: {sexo}, Telefone: {telefone}, Email: {email}\n')
    # Exibir mensagem de sucesso
    st.success('Dados salvos com sucesso!')
# Instruções para rodar o app
#Para rodar este app, execute o seguinte comando no terminal
# streamlit run app.py,ou, pyhton -m streamlit run app.py
# Certifique-se de que o Streamlit está instalado no seu ambiente Python.
# Você pode instalar o Streamlit usando o comando: pip install streamlit

