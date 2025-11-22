import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
import streamlit as st

# 環境変数の読み込み
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LangChainの設定
llm = ChatOpenAI(openai_api_key=api_key, temperature=0.7)

def get_llm_response(input_text, expert_type):
    """
    入力テキストと専門家の種類を基にLLMからの応答を取得する関数。

    Args:
        input_text (str): ユーザーが入力したテキスト。
        expert_type (str): 選択された専門家の種類。

    Returns:
        str: LLMからの応答。
    """
    system_message = f"あなたは{expert_type}の専門家です。ユーザーの質問に対して的確かつ簡潔に回答してください。"
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=input_text)
    ]
    response = llm.invoke(messages)
    return response.content

# Streamlitアプリの設定
st.title("LangChainを使ったLLMアプリ")

st.write("このアプリでは、以下の手順でLLMを利用できます：")
st.write("1. 専門家の種類を選択します。")
st.write("2. 入力フォームに質問を入力し、送信します。")
st.write("3. LLMからの回答が画面に表示されます。")

# 専門家の種類を選択
expert_type = st.radio(
    "専門家の種類を選択してください：",
    ["医療", "料理", "教育"]
)

# 入力フォーム
input_text = st.text_area("質問を入力してください：")

# 実行ボタン
if st.button("送信"):
    if input_text:
        try:
            # LLMからの応答を取得
            response = get_llm_response(input_text, expert_type)
            st.write("### 回答:")
            st.write(response)
        except Exception as e:
            st.error(f"エラーが発生しました: {e}")
    else:
        st.error("質問を入力してください！")