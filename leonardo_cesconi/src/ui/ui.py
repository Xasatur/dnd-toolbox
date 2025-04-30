import streamlit as st
import requests

st.title("🧙‍♂️ DnD Toolbox")

tool = st.sidebar.selectbox("Wähle ein Tool:", ["Loot Generator", "Zauberbuch"])

if tool == "Loot Generator":
    st.header("🎁 Loot Generator")
    rarity = st.selectbox(
        "Seltenheit",
        [1, 2, 3],
        format_func=lambda x: {1: "gewöhnlich", 2: "selten", 3: "episch"}[x],
    )
    amount = st.slider("Wie viele Items?", 1, 5, 1)

    if st.button("Loot generieren"):
        response = requests.get(
            "http://localhost:8000/loot", params={"rarity": rarity, "amount": amount}
        )
        data = response.json()
        st.write(f"**Seltenheit:** {data['rarity']}")
        st.write("**Gegenstände:**")
        for item in data["items"]:
            st.markdown(f"- {item}")

elif tool == "Zauberbuch":
    st.header("📖 Zauberbuch")
    name = st.text_input("Zaubername")

    if st.button("Suchen"):
        response = requests.get("http://localhost:8000/spells", params={"name": name})
        data = response.json()
        st.write(data)
