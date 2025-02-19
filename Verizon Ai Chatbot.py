import streamlit as st

# Function to generate chatbot responses
def chatbot_response(user_input):
    responses = {
        "billing issue": "I see you're experiencing a billing issue. Would you like to review your latest charges or request a refund?",
        "service outage": "I'm sorry to hear about the service outage. Let me check the outage status in your area.",
        "plan change": "I can help you change your plan. Do you want to upgrade, downgrade, or customize your current plan?",
        "refund request": "I can process a refund request. Could you provide your account details?",
        "agent": "I’m escalating your issue to a customer support agent. Please hold on."
    }

    for key in responses:
        if key in user_input.lower():
            return responses[key]
    
    return "I'm not sure how to help with that. Would you like to speak with an agent?"

# Streamlit UI
st.set_page_config(page_title="Verizon AI Chatbot", page_icon="🤖", layout="centered")

st.title("📡 Verizon AI-Powered Complaint Resolution Chatbot")
st.write("Automated assistance for common Verizon customer service issues. Type your issue below.")

# User input
user_input = st.text_input("How can I assist you today?", key="input")

# Display chatbot response
if user_input:
    response = chatbot_response(user_input)
    st.markdown(f"**Chatbot:** {response}")
