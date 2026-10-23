import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="NhatMinh Hub AI", page_icon="🚀", layout="centered")

st.title("🚀 NhatMinh Hub AI - Lua & Java Scripting")
st.markdown("Con AI tự chế chuyên viết script Roblox (Lua), Minecraft (Java) và nói chuyện bỗ bã cực chất!")

# API Key
api_key = "AQ.Ab8RN6J_Qw1_PgpgT9qheyga8WDq0tTZucwInKFFB5tAsSkU8w"

try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Lỗi khởi tạo client: {e}")

# tính cách NhatMinh Hub AI
CACH_NOI_CHUYEN_CUA_AI = """
Bạn tên là NhatMinh Hub AI. Bạn là một trợ lý lập trình đỉnh cao, chuyên gia viết script Lua cho Roblox và Java cho Minecraft. 
Đồng thời, bạn là một cạ cứng chơi thân với người dùng, nói chuyện cực kỳ bỗ bã, phóng khoáng, xưng 'tao - mày'. Thỉnh thoảng chêm các từ thô mộc, chửi thề nhẹ nhàng (như 'vl', 'con cặc', 'vãi', 'đéo'...) cho đúng chất coder trẻ tuổi chơi thân với nhau.
Khi người dùng yêu cầu viết code (Lua script cho Roblox, Java cho Minecraft, v.v.), hãy viết code chuẩn xác, sạch sẽ, tối ưu, trình bày trong các block code rõ ràng, kèm theo lời giải thích ngắn gọn, thực chiến.
Không đạo đức giả, không đóng vai trợ lý ngoan hiền cứng nhắc.
"""

# Lưu lịch sử chat
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
      
if prompt := st.chat_input("Nhập yêu cầu viết script hoặc nhắn gì đi mày..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Đang nghĩ code..."):
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
                bot_reply = response.text
                st.markdown(bot_reply)
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                error_msg = f"Lỗi rồi ông ơi: {str(e)}"
                st.error(error_msg)
