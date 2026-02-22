import streamlit as st

st.set_page_config(page_title="Fitness AI Coach", page_icon="🏋️")

st.title("🏋️ Instant Physical Fitness Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []


def fitness_reply(question):
    q = question.lower()

    if "weight" in q and "loss" in q:
        return "For weight loss: do cardio 30 minutes daily, eat high-protein food, and reduce sugar."

    elif "muscle" in q or "gain" in q:
        return "For muscle gain: strength training 4–5 days/week, eat protein-rich foods like eggs, chicken, and lentils."

    elif "abs" in q:
        return "For abs: plank, leg raises, crunches, and maintain a low body fat diet."

    elif "diet" in q:
        return "Healthy diet includes protein, vegetables, fruits, whole grains, and plenty of water."

    elif "exercise" in q:
        return "Daily exercise: 10 min warm-up, 20 min cardio, 15 min strength training, stretching."

    elif "hello" in q or "hi" in q:
        return "Hello! I am your fitness coach. Ask me anything about workouts or diet."

    else:
        return "Stay active, eat healthy, sleep well, and stay consistent for good fitness."


# Chat display
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Ask your fitness question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    reply = fitness_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)