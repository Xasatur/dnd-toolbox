import streamlit as st
import requests

st.title("🧙‍♂️ DnD Toolbox")

tool = st.sidebar.selectbox("Wähle ein Tool:", ["Loot Generator", "Zauberbuch"])

if tool == "Loot Generator":
    st.header("🎁 Loot Generator")
    rarity_labels = {"gewöhnlich": "common", "selten": "rare", "episch": "very rare"}
    rarity_display = st.selectbox("Seltenheit", list(rarity_labels.keys()))
    rarity = rarity_labels[rarity_display]
    amount = st.slider("Wie viele Items?", 1, 5, 1)

    if st.button("Loot generieren"):
        response = requests.get(
            "http://localhost:8000/loot", params={"rarity": rarity, "amount": amount}
        )
        data = response.json()
        if response.status_code == 200 and "items" in data:
            st.write(f"**Seltenheit:** {data['rarity']}")
            st.write("**Gegenstände:**")
            for item in data["items"]:
                st.markdown(f"- {item}")
        else:
            st.error("Fehler beim Abrufen des Loots.")

elif tool == "Zauberbuch":
    st.header("📖 Zauberbuch")
    name = st.text_input("Zaubername")

    if st.button("Suchen"):
        response = requests.get("http://localhost:8000/spells", params={"name": name})
        data = response.json()
        if data.get("spells"):
            spell = data["spells"][0]
            st.subheader(spell["name"])
            st.write(f"📘 Schule: {spell['school']}")
            st.write(f"🔢 Level: {spell['level']}")
            st.write(f"⏱ Cast Time: {spell['casting_time']}")
            st.write(f"⏳ Dauer: {spell['duration']}")
            st.write(f"🎯 Reichweite: {spell['range']}")
            st.write("📖 Beschreibung:")
            st.markdown(spell["description"])
        else:
            st.warning("Kein Zauber gefunden.")
