import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
import streamlit as st
import requests
from src.core.combat import load_monsters, MonsterInstance
import uuid

st.title("🧙‍♂️ DnD Toolbox")

tool = st.sidebar.selectbox(
    "Wähle ein Tool:", ["Loot Generator", "Zauberbuch", "Combat Helper"]
)

if tool == "Loot Generator":
    st.header("🎁 Loot Generator")
    rarity_labels = {
        "gewöhnlich": "common",
        "ungewöhnlich": "uncommon",
        "selten": "rare",
        "sehr selten": "very rare",
        "legendär": "legendary",
    }
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

elif tool == "Combat Helper":
    st.header("⚔️ Combat Helper")

    # Initialisiere Combat State
    if "combat_monsters" not in st.session_state:
        st.session_state.combat_monsters = []
    if "battlefield_queue" not in st.session_state:
        st.session_state.battlefield_queue = []
    if "combat_round" not in st.session_state:
        st.session_state.combat_round = 0

    # Neue Runde starten
    if st.button("⏭ Neue Runde starten"):
        st.session_state.combat_round += 1
        st.success(f"➡️ Runde {st.session_state.combat_round}")

        # Aufgeladene Battlefield Actions anzeigen
        to_resolve = [
            bfa for bfa in st.session_state.battlefield_queue
            if bfa["round"] == st.session_state.combat_round
        ]
        if to_resolve:
            st.markdown("### 💥 Battlefield Action Resolution")
            for bfa in to_resolve:
                st.info(
                    f"🌪️ **{bfa['monster_name']} – {bfa['name']}**\n\n"
                    f"🛡 {bfa['neutralize']}\n\n🎇 {bfa['resolution']}"
                )

        # Entferne ausgeführte Aktionen
        st.session_state.battlefield_queue = [
            bfa for bfa in st.session_state.battlefield_queue
            if bfa["round"] > st.session_state.combat_round
        ]

    st.markdown(f"**📆 Aktuelle Runde: {st.session_state.combat_round}**")

    if st.button("🧹 Arena zurücksetzen"):
        st.session_state.combat_monsters = []
        st.session_state.battlefield_queue = []
        st.session_state.combat_round = 0
        st.success("Arena wurde geleert.")

    response = requests.get("http://localhost:8000/monsters")
    if response.status_code == 200:
        monsters = response.json().get("monsters", [])
        if monsters:
            monster_names = [f"{m['icon']} {m['name']}" for m in monsters]
            selection = st.selectbox("Wähle ein Monster:", monster_names)
            st.success(f"Ausgewähltes Monster: {selection}")

            selected_monsters = st.multiselect(
                "Wähle Monster zum Hinzufügen:", monster_names
            )

            if st.button("Monster zur Arena hinzufügen"):
                available = {f"{m['icon']} {m['name']}": m["name"] for m in monsters}
                for label in selected_monsters:
                    name = available[label]
                    monster_class = next(
                        (cls for cls, id in load_monsters() if cls().name == name), None
                    )
                    if monster_class:
                        mid = str(uuid.uuid4())[:4]
                        instance = MonsterInstance(monster_class, mid)
                        st.session_state.combat_monsters.append(instance)

            if st.session_state.combat_monsters:
                st.subheader("🧟 Aktive Monster")
                for m in st.session_state.combat_monsters:
                    st.markdown(f"### {m.icon} {m.name} [ID: {m.id}]")

                    # Normale Actions
                    actions = m.actions()
                    for i, action in enumerate(actions):
                        if st.button(f"{m.id} - {action}"):
                            result = actions[action]()
                            st.success(f"🎯 {action}:\n{result}")

                    # Battlefield Actions
                    battlefield = m.battlefield_actions()
                    if battlefield:
                        st.markdown("#### 🌪️ Battlefield Actions")
                        for bfa in battlefield:
                            label = f"{m.id} - {bfa['name']}"
                            if st.button(label):
                                st.session_state.battlefield_queue.append({
                                    "monster_id": m.id,
                                    "monster_name": m.name,
                                    "name": bfa["name"],
                                    "tell": bfa["tell"],
                                    "neutralize": bfa["neutralize"],
                                    "resolution": bfa["resolution"],
                                    "round": st.session_state.combat_round + 1
                                })
                                st.warning(
                                    f"📣 {bfa['name']} aktiviert! (Wirkung in Runde {st.session_state.combat_round + 1})"
                                )
                                st.info(f"🌀 {bfa['tell']}")
        else:
            st.warning("Keine Monster gefunden.")
    else:
        st.error("Fehler beim Abrufen der Monster.")
