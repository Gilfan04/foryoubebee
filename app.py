import streamlit as st
import streamlit.components.v1 as components
import time
import random

# ============================================================================
# PAGE CONFIG
# ============================================================================

st.set_page_config(
    page_title="Happy Anniversary ❤️",
    page_icon="💐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================================
# SESSION STATE
# ============================================================================

if "open_letter" not in st.session_state:
    st.session_state.open_letter = False

if "typed_complete" not in st.session_state:
    st.session_state.typed_complete = False

if "final_text" not in st.session_state:
    st.session_state.final_text = ""

# ============================================================================
# CSS
# ============================================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@300;400;500;700&family=Great+Vibes&display=swap');

html, body, [class*="css"] {
    font-family: 'Cormorant Garamond', serif;
}

.stApp {
    background: linear-gradient(to bottom, #f6e9da, #f9efe4);
    overflow-x: hidden;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

.title {
    font-family: 'Great Vibes', cursive;
    text-align: center;
    color: #7a4b47;
    animation: float 4s ease-in-out infinite;
}

.subtitle {
    text-align: center;
    font-size: 28px;
    color: #5c3b37;
    line-height: 2;
}

.paper {
    background: rgba(255,255,255,0.45);
    padding: 45px;
    border-radius: 35px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15);
    border: 1px solid #d7bfa7;
}

.glass {
    background: rgba(255,255,255,0.25);
    backdrop-filter: blur(12px);
    border-radius: 35px;
    padding: 35px;
    border: 1px solid rgba(255,255,255,0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.15);
}

.letter {
    font-size: 28px;
    line-height: 2.2;
    color: #4d3633;
    white-space: pre-wrap;
}

.center {
    text-align: center;
}

.flower {
    position: fixed;
    top: -10px;
    animation: fall linear infinite;
    z-index: 999;
    opacity: 0.8;
}

@keyframes fall {

    0% {
        transform: translateY(-10vh) rotate(0deg);
    }

    100% {
        transform: translateY(110vh) rotate(360deg);
    }

}

@keyframes float {

    0%,100% {
        transform: translateY(0px);
    }

    50% {
        transform: translateY(-10px);
    }

}

</style>
""", unsafe_allow_html=True)

# ============================================================================
# FLOWERS
# ============================================================================

flowers_html = ""

# bunga hanya sebelum surat dibuka
if not st.session_state.open_letter:

    for _ in range(45):

        left = random.randint(0, 100)
        duration = random.randint(8, 18)
        delay = random.randint(0, 10)
        size = random.randint(20, 45)

        flowers_html += f"""
        <div class="flower"
            style="
                left:{left}%;
                animation-duration:{duration}s;
                animation-delay:{delay}s;
                font-size:{size}px;
            ">
            🌸
        </div>
        """

    st.markdown(flowers_html, unsafe_allow_html=True)

# ============================================================================
# HERO
# ============================================================================

st.markdown("""
<div class='glass center'>

<div style='font-size:100px;'>
💐
</div>

<div class='title' style='font-size:95px;'>
Happy 1st Anniversary
</div>

<div class='subtitle'>
Satu tahun penuh cerita, tawa, tangis, dan rasa sayang yang terus tumbuh.
</div>

</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

# ============================================================================
# MUSIC
# ============================================================================

st.markdown("""
<div class='glass center'>

<div style='font-size:70px; margin-bottom:10px;'>
💌
</div>

<h1 style='
    font-size:65px;
    color:#7a4b47;
    font-family: Great Vibes, cursive;
'>
Sebelum Membaca...
</h1>

<p style='
    font-size:30px;
    color:#5c3b37;
    line-height:2;
'>
baca ini sambil denger lagu ini ya sayang 🎵
</p>

</div>
""", unsafe_allow_html=True)

spotify_html = """
<div style="
    border-radius:25px;
    overflow:hidden;
    box-shadow:0 10px 30px rgba(0,0,0,0.15);
">
<iframe
    style="border-radius:25px"
    src="https://open.spotify.com/embed/track/1dGr1c8CrMLDpV6mPbImSI?utm_source=generator&theme=0"
    width="100%"
    height="152"
    frameBorder="0"
    allowfullscreen=""
    allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
    loading="lazy">
</iframe>
</div>
"""

components.html(spotify_html, height=180)

# ============================================================================
# OPEN LETTER
# ============================================================================

st.write("")
st.write("")

if not st.session_state.open_letter:

    st.markdown("""
    <div class='glass center'>

    <div style='font-size:120px; animation: float 3s ease-in-out infinite;'>
    💌
    </div>

    <h1 style='
        font-size:65px;
        color:#7a4b47;
        font-family: Great Vibes, cursive;
    '>
    Ada Surat Untuk Kamu
    </h1>

    <p style='
        font-size:28px;
        color:#5c3b37;
    '>
    pencet amplopnya ya sayang ✨
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("💌 Buka Surat", use_container_width=True):

        st.session_state.open_letter = True
        st.rerun()

# ============================================================================
# LETTER
# ============================================================================

if st.session_state.open_letter:

    st.write("")
    st.write("")

    st.markdown(
        "<div class='title' style='font-size:80px;'>Surat Untuk Kamu 💌</div>",
        unsafe_allow_html=True
    )

    letter = '''Salam sayang,

‎Haiii Nurul inii akuu Gilfan, orang yang mungkin kamu gapernah kepikiran bisa ngabisin waktu satu tahun bareng, ahahahaa kalau dipikir-pikir lucu juga yaa  kita rul bisa sampai selama ini, jujur satu tahun itu emang bukan waktu yang lama, tapi waktu yang sebentar buat ngabisin waktu kita bersama. Jujur sedih dan bahagianya pasti ada aja di hubungan kita bedua ini, semakin lama semakin aku berusaha buat mahamin gimana kamu dan apa yang kamu ingin. Jujur aku belum bisa menuhin semua wishlist kamu. Tapi, percayalah aku bakal berusaha buat menuhin itu satu-persatu. Jodoh gaada yang tau dan gaada yang bisa memprediksi, aku hari ini blom tentu sama dengan aku hari esok. Tapi, yang perlu kamu tau, aku selalu sayang dan cinta sama kamu dan aku bakal terus berusaha jadi yang terbaik buat kamu. Aku tau aku bukan yang pertama ada di hati kamu, aku juga tau aku bukan orang yang sangat kamu nanti-nantikan. Aku cuman mau kamu tau, kalau banyak hal, banyak kejadian, banyak masalah atau bahkan kebahagiaan yang kamu bawa ke aku, dan aku sangat bersyukur bisa jadi pasangan kamu saat ini. Entah apa yang ada dipikiranku saat ini dan tulisan ini, tapi yang ada di otak aku saat nulis ini cuman satu sayang, dan kamu harus tau itu. Apa yang aku pikir cuman "Aku sayang sama kamu". Mungkin pikiranku terlalu sempit buat nampung perasaanku yang sangat luas ini. Entah kata-kata apalagi yang harus aku keluarin, tapi jujur aku sangat suka kalau kamu lagi tersenyum dan jadi diri kamu sendiri. Semoga kita bisa bersama terus dan saling sayang. Kalaupun kita tidak ditakdirkan bersama aku tetap bersyukur aku bisa sayang sama kamu, aku harap itu tidak terjadi dan semoga kedepannya banyak hal baik yang menimpa kita ya sayang. Semoga semua berjalan lancar dan bahagia.

‎Salam hangat,
‎Gilfan'''

    container = st.empty()

    if not st.session_state.typed_complete:

        typed_text = ""

        for char in letter:

            typed_text += char

            container.markdown(
                f"""
                <div class='paper'>
                    <div class='letter'>{typed_text}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            time.sleep(0.05)

        st.session_state.final_text = typed_text
        st.session_state.typed_complete = True

    else:

        container.markdown(
            f"""
            <div class='paper'>
                <div class='letter'>{st.session_state.final_text}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
