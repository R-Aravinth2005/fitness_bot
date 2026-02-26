
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="Flexa", page_icon="💪")

# ---------------- BACKGROUND STYLE ----------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    }

    h1, h3 {
        color: white;
        text-align: center;
        text-shadow: 2px 2px 6px rgba(0,0,0,0.7);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE ----------------
st.markdown("<h1>🏋️ Flexa</h1>", unsafe_allow_html=True)
st.markdown("<h3>Your Fitness Companion 💪</h3>", unsafe_allow_html=True)

st.divider()

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- BOT LOGIC ----------------
def fitness_reply(question):
    q = question.lower()

    if "weight" in q and "loss" in q:
        return "For weight loss: Do cardio 30 minutes daily, eat high-protein food, and reduce sugar."

    elif "muscle" in q or "gain" in q:
        return "For muscle gain: Strength training 4–5 days/week and eat protein-rich foods."

    elif "abs" in q:
        return "For abs: Plank, leg raises, crunches, and maintain low body fat with proper diet."

    elif "diet" in q:
        return "Healthy diet includes protein, vegetables, fruits, whole grains, and plenty of water."

    elif "exercise" in q:
        return "Daily exercise: 10 min warm-up, 20 min cardio, 15 min strength training, and stretching."

    elif "hello" in q or "hi" in q:
        return "Hello! I am Flexa — Your Fitness Companion 💪. Ask me anything about workouts or diet."

    else:
        return "Stay active, eat healthy, sleep well, and stay consistent for good fitness."


# ---------------- QUICK BUTTONS ----------------
st.subheader("⚡ Quick Options")

col1, col2, col3, col4 = st.columns(4)

if col1.button("Weight Loss"):
    st.session_state.messages.append({"role": "assistant", "content": fitness_reply("weight loss")})

if col2.button("Muscle Gain"):
    st.session_state.messages.append({"role": "assistant", "content": fitness_reply("muscle gain")})

if col3.button("Diet Plan"):
    st.session_state.messages.append({"role": "assistant", "content": fitness_reply("diet")})

if col4.button("Exercise"):
    st.session_state.messages.append({"role": "assistant", "content": fitness_reply("exercise")})

st.divider()

# ---------------- BMI CALCULATOR ----------------
st.subheader("📊 BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=1.0)
height = st.number_input("Enter your height (meters)", min_value=0.5)

if st.button("Calculate BMI"):
    bmi = weight / (height ** 2)

    if bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal weight"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"

    st.success(f"Your BMI: {bmi:.2f} — {result}")

st.divider()

# ---------------- CHAT DISPLAY ----------------
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("💬 Ask Flexa about workouts, diet, or fitness...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.chat_message("user").write(user_input)

    reply = fitness_reply(user_input)

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.chat_message("assistant").write(reply)
