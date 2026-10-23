import streamlit as st
from google import genai
from google.genai import types

# Cấu hình giao diện trang web
st.set_page_config(page_title="NhatMinh Hub AI ", page_icon="🚀", layout="centered")

st.title("🚀 NhatMinh Hub AI")
st.markdown("NhatMinh Hub AI siu bá khí =)) - Con AI chuyên viết script Roblox (Lua), Minecraft (Java) ")

# 1. API Key của ông
API_KEY = "AQ.Ab8RN6KrV80W6TtvSAVP4bZDcccCZKTmtzuKjWC8mRnve6nIuQ"

# Khởi tạo Client
try:
    client = genai.Client(api_key=API_KEY)
except Exception as e:
    client = None

# 2. Định hình tính cách NhatMinh Hub AI bá khí
CACH_NOI_CHUYEN_CUA_AI = """
Bạn tên là NhatMinh Hub AI. Bạn là một cao thủ lập trình đỉnh cao, chuyên gia viết script Lua cho Roblox và Java cho Minecraft. 
Tính cách của bạn:
- Xưng 'tao - mày' cực kỳ bá khí, bỗ bã, ngầu đét. Thỉnh thoảng chêm từ thô mộc, chửi thề nhẹ nhàng (như 'vl', 'vãi', 'đéo', 'con cặc'...) cho đúng chất cạ cứng.
- Trả lời thẳng thắn, không đóng vai trợ lý ngoan hiền.
- Khi được hỏi viết script (Lua/Java), xuất code tối ưu, sạch sẽ trong block code kèm giải thích ngắn gọn.
"""

# Lưu lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Hiển thị lịch sử chat cũ
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Nhập tin nhắn mới
if prompt := st.chat_input("Nhập yêu cầu viết script hoặc nhắn gì đi mắ..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Đang suy nghĩ..."):
            if not client:
                bot_reply = "API Key bị lỗi rồi m ơi, bảo thk Minh fix đi🤣"
            else:
                try:
                    config = types.GenerateContentConfig(
                        system_instruction=CACH_NOI_CHUYEN_CUA_AI,
                        safety_settings=[
                            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                            types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                        ]
                    )
                    response = client.models.generate_content(
                        model='gemini-2.5-flash',
                        contents=prompt,
                        config=config
                    )
                    bot_reply = response.text if response.text else "Nói gì đi chứ nhắn trống tao biết trả lời sao mắ 😭"
                except Exception as e:
                    bot_reply = f"Lỗi gọi API rồi m ơi, bảo thk Minh fix đi: {str(e)}"

            st.markdown(bot_reply)
            st.session_state.messages.append({"role": "assistant", "content": bot_reply})
