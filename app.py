# 核心大腦
import streamlit as st
import yt_dlp
import os

st.set_page_config(page_title="影音 App", page_icon="🎬")
st.title("🎬 萬能影音下載器")

# 廣告欄位
st.markdown("<div style='background:#2a2a2a;padding:10px;text-align:center;color:#ff4757;border-radius:5px;'><b>【廣告贊助商版位】</b></div>", unsafe_allow_html=True)

url = st.text_input("📌 請貼上影片網址:")
if url:
    st.success("讀取成功！")
    try:
        st.video(url)
    except:
        st.warning("此網站不支援直接播放，但仍可嘗試在下方下載。")
        
    if st.button("🚀 開始解析並下載"):
        with st.spinner("解析中..."):
            try:
                opts = {'format': 'best', 'outtmpl': 'downloads/%(title)s.%(ext)s'}
                with yt_dlp.YoutubeDL(opts) as ydl:
                    info = ydl.extract_info(url, download=True)
                    name = ydl.prepare_filename(info)
                with open(name, "rb") as f:
                    st.download_button("💾 點我儲存檔案", data=f.read(), file_name=os.path.basename(name))
                if os.path.exists(name): os.remove(name)
            except Exception as e:
                st.error("解析失敗，可能該網站有防爬蟲限制。")
