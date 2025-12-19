import streamlit as st
import os
from openai import OpenAI

# --- OpenAI клиентін жасау ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# --- Бастапқы бет ---
st.title("AI Learning Assistant 🤖")

# Режим таңдау
mode = st.selectbox("Режимді таңдаңыз:", ["Оқушы режимі", "Мұғалім режимі"])

# --- Оқушы режимі ---
if mode == "Оқушы режимі":
    st.subheader("Оқушы режимі")
    grade = st.selectbox("Сыныпты таңдаңыз:", ["7-сынып", "8-сынып", "9-сынып"])
    topic = st.text_input("Түсінбеген тақырыпты немесе тақырыпша енгізіңіз:")

    if st.button("Тапсырма жасау"):
        if topic.strip() == "":
            st.warning("Тақырып енгізіңіз!")
        else:
            prompt = f"Сынып: {grade}\nТақырып: {topic}\nОқушыға түсінікті тілмен түсіндіріп, қарапайым тапсырма және шешу жолын көрсетіңіз."
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
            except Exception as e:
                st.error(f"Қате шықты: {e}")

# --- Мұғалім режимі ---
elif mode == "Мұғалім режимі":
    st.subheader("Мұғалім режимі")
    grade = st.selectbox("Сыныпты таңдаңыз:", ["7-сынып", "8-сынып", "9-сынып"])
    topic = st.text_input("Тақырыпты енгізіңіз:")
    difficulty = st.selectbox("Тапсырманың күрделілігі:", ["Жеңіл", "Орташа", "Күрделі"])

    if st.button("Тапсырма құрастыру"):
        if topic.strip() == "":
            st.warning("Тақырып енгізіңіз!")
        else:
            prompt = f"Сынып: {grade}\nТақырып: {topic}\nКүрделілік: {difficulty}\nМұғалімге арналған тапсырма дайындаңыз, жауаптары мен мысалдарымен."
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7
                )
                answer = response.choices[0].message.content
                st.markdown(answer)
            except Exception as e:
                st.error(f"Қате шықты: {e}")
