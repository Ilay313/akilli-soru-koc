import streamlit as st
import openai

st.set_page_config(page_title="Akıllı Soru Koçu", page_icon="🧠")

st.title("🧠 Akıllı Soru Koçu")
st.write("Yapay zekâ destekli açıklamalı soru çözüm asistanına hoş geldiniz!")

api_key = st.secrets["openai"]["api_key"]

question = st.text_area("Sormak istediğiniz soruyu yazın:")

if st.button("Soruyu Açıkla"):
    if question.strip() == "":
            st.warning("Lütfen bir soru girin.")
                else:
                        with st.spinner("Cevaplanıyor..."):
                                    try:
                                                    openai.api_key = api_key
                                                                    response = openai.ChatCompletion.create(
                                                                                        model="gpt-4",
                                                                                                            messages=[
                                                                                                                                    {"role": "system", "content": "Sen bir eğitim koçusun. Karmaşık soruları sade ve adım adım açıklarsın."},
                                                                                                                                                            {"role": "user", "content": question}
                                                                                                                                                                                ]
                                                                                                                                                                                                )
                                                                                                                                                                                                                answer = response.choices[0].message.content
                                                                                                                                                                                                                                st.success("Cevap:")
                                                                                                                                                                                                                                                st.markdown(answer)
                                                                                                                                                                                                                                                            except Exception as e:
                                                                                                                                                                                                                                                                            st.error(f"Hata oluştu: {e}")