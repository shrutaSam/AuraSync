import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="AuraSync",
    page_icon="🌌",
    layout="centered"
)

page_style = """
<style>
body {
    background: #e0f2fe;
}
.stApp {
    min-height: 100vh;
    color: #0f172a;
    background: radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.65), transparent 22%),
                radial-gradient(circle at 85% 10%, rgba(191, 219, 254, 0.35), transparent 18%),
                linear-gradient(180deg, #dbeafe 0%, #bae6fd 35%, #93c5fd 70%, #bae6fd 100%);
    background-attachment: fixed;
    overflow: hidden;
    position: relative;
}

.stApp::after {
    content: "";
    position: absolute;
    inset: 0;
    background-image: radial-gradient(circle at 50% 0%, rgba(255,255,255,0.55), transparent 12%),
                      radial-gradient(circle at 15% 85%, rgba(255,255,255,0.22), transparent 10%),
                      radial-gradient(circle at 80% 70%, rgba(255,255,255,0.18), transparent 8%);
    pointer-events: none;
}

h1 {
    text-align: center;
    color: #1d4ed8;
    font-size: 64px !important;
    letter-spacing: 0.08em;
    text-shadow: 0 0 18px rgba(37, 99, 235, 0.3);
}

h2, h3 {
    color: #1e40af;
}

p, label {
    color: #0f172a;
}

.stButton>button {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.95), rgba(147, 197, 253, 0.95));
    color: #0f172a;
    border-radius: 22px;
    height: 3.4em;
    width: 100%;
    font-size: 18px;
    border: none;
    box-shadow: 0 18px 40px rgba(59, 130, 246, 0.18);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 22px 45px rgba(59, 130, 246, 0.25);
}

.stTextInput>div>input,
.stSlider>div>div>input,
.stSelectbox>div>div>div>select {
    border-radius: 18px;
    background: rgba(255,255,255,0.8);
    border: 1px solid rgba(147, 197, 253, 0.6);
    color: #0f172a;
}

.css-12oz5g7 {
    background: rgba(255,255,255,0.72);
    border-radius: 24px;
    padding: 1.4rem;
    box-shadow: 0 24px 60px rgba(59, 130, 246, 0.12);
}

.card {
    background: rgba(255,255,255,0.85);
    border-radius: 22px;
    padding: 1.1rem;
    box-shadow: 0 18px 35px rgba(15, 23, 42, 0.08);
    border: 1px solid rgba(255,255,255,0.6);
}

.card-title {
    margin-bottom: 0.6rem;
    color: #1d4ed8;
}

.result-box {
    background: rgba(255,255,255,0.9);
    border-radius: 24px;
    padding: 1.4rem;
    box-shadow: 0 20px 50px rgba(15, 23, 42, 0.1);
    border: 1px solid rgba(255,255,255,0.75);
}

.small-note {
    color: #1e3a8a;
    opacity: 0.84;
}
</style>
"""

st.markdown(page_style, unsafe_allow_html=True)

def get_zodiac_sign(birthdate):
    if birthdate is None:
        return None
    month = birthdate.month
    day = birthdate.day
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    return None

zodiac_predictions = {
    "Aquarius": "Today, embrace innovation and think outside the box. Your unique ideas will shine, and unexpected opportunities may arise. Stay open to new perspectives.",
    "Pisces": "Your intuition is strong today. Trust your feelings and let your creativity flow. It's a good day for artistic pursuits or helping others.",
    "Aries": "Energy and enthusiasm are on your side. Take initiative on projects and don't be afraid to lead. Your boldness will inspire those around you.",
    "Taurus": "Focus on stability and practicality. Ground yourself in what feels secure. Enjoy simple pleasures and build towards long-term goals.",
    "Gemini": "Communication is key today. Share your thoughts and ideas freely. You may learn something new or connect with interesting people.",
    "Cancer": "Nurture your emotions and care for loved ones. Your sensitivity is a strength. Create a cozy environment and listen to your inner voice.",
    "Leo": "Shine brightly and express yourself confidently. Your charisma draws people in. Use your creativity to make a positive impact.",
    "Virgo": "Attention to detail will serve you well. Organize and refine your plans. Small improvements can lead to big results today.",
    "Libra": "Seek balance and harmony in your interactions. Your diplomatic nature helps resolve conflicts. Focus on relationships and fairness.",
    "Scorpio": "Dive deep into matters that intrigue you. Your intensity brings transformation. Trust your instincts and embrace change.",
    "Sagittarius": "Adventure calls! Explore new ideas or places. Your optimism and curiosity will guide you to exciting discoveries.",
    "Capricorn": "Discipline and perseverance pay off. Work steadily towards your ambitions. Your determination inspires respect from others."
}

st.markdown(
    """
    <div class='card'>
        <h1>🌌 AuraSync</h1>
        <p style='font-size:1.2rem; margin-top:-0.5rem;'>Your Digital Human Vibe Analyzer</p>
        <div style='text-align:center; margin-top:0.6rem; font-size:1.4rem;'>💖 🌈 ✨ 🌿 🎶 🌟</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("Analyze mood, sleep, music, and energy to discover your emotional vibe.")

with st.container():
    left, right = st.columns([2, 1])
    with left:
        birthdate = st.date_input("📅 Birthdate (for zodiac prediction)", value=None, min_value=datetime(1900, 1, 1), max_value=datetime(2100, 12, 31))
        sleep = st.slider("😴 Sleep Hours", 0, 12, 7)
        mood = st.selectbox(
            "😊 Mood Check-In",
            ["Happy", "Calm", "Stressed", "Tired", "Sad", "Excited", "Anxious"]
        )
        music = st.selectbox(
            "🎵 Music Preference",
            ["Lo-fi", "Pop", "Sad Songs", "Classical", "Rock", "Chill", "Energetic"]
        )
        energy = st.slider("⚡ Energy Level", 0, 100, 50)
    with right:
        st.markdown(
            """
            <div class='card'>
                <h3 class='card-title'>Today's Mini Summary</h3>
                <p><strong>Sleep:</strong> Restorative habits matter.</p>
                <p><strong>Mood:</strong> Your feelings guide your day.</p>
                <p><strong>Music:</strong> Pick vibes that match your flow.</p>
                <p class='small-note'>Use the button below to reveal your aura.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

def compute_vibe(sleep, mood, energy, music, birthdate):
    aura = "✨ Reflective Aura"
    quote = "Your emotions are valid. Your vibe matters."
    recommendation = "Pay attention to your needs and create a gentle routine."
    song = "Calm Playlist / Lo-fi Beats"
    vibe = "Your emotional energy feels thoughtful and reflective today."

    if mood == "Happy":
        if energy > 80:
            aura = "🌟 Radiant Aura"
            quote = "You are glowing with positive energy today."
            recommendation = "Use this momentum for creative projects and social connection."
        elif energy > 50:
            aura = "🌈 Bright Aura"
            quote = "Your joy is steady and warm."
            recommendation = "Keep the flow going with light movement and uplifting music."
        else:
            aura = "☀️ Warm Aura"
            quote = "Your happiness feels calm and gentle."
            recommendation = "Enjoy the small moments and stay present."
    elif mood == "Calm":
        aura = "🌙 Peaceful Aura"
        quote = "Peace is powerful."
        recommendation = "Keep your mind steady with slow breathing and grounding music."
        if energy > 70:
            aura = "🌿 Balanced Aura"
            quote = "You feel centered and capable today."
            recommendation = "Maintain your calm by focusing on mindful tasks."
    elif mood == "Stressed":
        if sleep < 5 or energy < 40:
            aura = "🔥 Tense Aura"
            quote = "It’s okay to rest when your mind feels overwhelmed."
            recommendation = "Take a pause, breathe deeply, and reduce your workload for a while."
        else:
            aura = "⚡ Focused Aura"
            quote = "You can turn this pressure into clear action if you stay kind to yourself."
            recommendation = "Break tasks into smaller steps and reward yourself with calm breaks."
    elif mood == "Tired":
        aura = "🌫️ Rest-Seeking Aura"
        quote = "Rest is not optional — it is how you restore your power."
        recommendation = "Try a gentle nap, warm tea, or a soothing playlist before you do more."
        if sleep >= 8:
            aura = "🌥️ Soft Glow Aura"
            quote = "You are healing as you slow down."
            recommendation = "Listen to the body’s signals and honor your pace."
    elif mood == "Sad":
        aura = "💧 Soft Aura"
        quote = "It’s okay to feel. Your emotions are part of your strength."
        recommendation = "Reach out to someone you trust, and choose comforting music."
    elif mood == "Excited":
        aura = "⚡ Electric Aura"
        quote = "Your energy is buzzing with possibility."
        recommendation = "Channel your excitement into a project or fresh adventure."
    elif mood == "Anxious":
        aura = "🌊 Sensitive Aura"
        quote = "You don’t have to solve everything right now. Slow down."
        recommendation = "Try grounding music, breathing exercises, or a short walk outside."

    if sleep < 5:
        vibe = f"You are running low on rest today. {quote}"
        song = "Soft Instrumentals / Gentle Piano"
    elif sleep <= 7:
        vibe = f"Your sleep was a bit light. {quote}"
        song = "Lo-fi / Chill Beats"
    else:
        if mood == "Happy":
            vibe = "You woke up refreshed and ready to shine."
        elif mood == "Calm":
            vibe = "You feel composed, rested, and emotionally steady."
        elif mood == "Stressed":
            vibe = "You are handling tension with awareness today."
        elif mood == "Tired":
            vibe = "Your energy is gentle, and your body may still need rest."
        elif mood == "Sad":
            vibe = "You are moving through soft emotions with care."
        elif mood == "Excited":
            vibe = "You feel energized and ready for new experiences."
        elif mood == "Anxious":
            vibe = "Your mind is alert, and you may need more calm support."

    music_map = {
        "Lo-fi": {
            "Happy": "Daydream - Lofi Hip Hop",
            "Calm": "Snowfall - Lofi Chill",
            "Stressed": "Midnight Focus - Lofi Beats",
            "Tired": "Late Night Study - Soft Lofi",
            "Sad": "Rainy Window - Melancholy Lofi",
            "Excited": "City Lights - Upbeat Lofi",
            "Anxious": "Soft Clouds - Relaxing Lofi"
        },
        "Pop": {
            "Happy": "Good as Hell - Lizzo",
            "Calm": "Sunflower - Rex Orange County",
            "Stressed": "Fight Song - Rachel Platten",
            "Tired": "Blinding Lights - The Weeknd",
            "Sad": "Someone Like You - Adele",
            "Excited": "Can’t Stop the Feeling - Justin Timberlake",
            "Anxious": "All Too Well - Taylor Swift"
        },
        "Sad Songs": {
            "Happy": "The Night We Met - Lord Huron",
            "Calm": "Holocene - Bon Iver",
            "Stressed": "I See Fire - Ed Sheeran",
            "Tired": "Skinny Love - Birdy",
            "Sad": "Lost Cause - Billie Eilish",
            "Excited": "Chasing Cars - Snow Patrol",
            "Anxious": "Breathe Me - Sia"
        },
        "Classical": {
            "Happy": "Spring from Vivaldi’s Four Seasons",
            "Calm": "Clair de Lune - Debussy",
            "Stressed": "Air on the G String - Bach",
            "Tired": "Gymnopédie No.1 - Satie",
            "Sad": "Adagio for Strings - Barber",
            "Excited": "Ride of the Valkyries - Wagner",
            "Anxious": "Nocturne Op.9 No.2 - Chopin"
        },
        "Rock": {
            "Happy": "Don’t Stop Me Now - Queen",
            "Calm": "Everlong - Foo Fighters",
            "Stressed": "Under Pressure - Queen & David Bowie",
            "Tired": "Numb - Linkin Park",
            "Sad": "Fix You - Coldplay",
            "Excited": "Thunderstruck - AC/DC",
            "Anxious": "Comfortably Numb - Pink Floyd"
        },
        "Chill": {
            "Happy": "Sunset Lover - Petit Biscuit",
            "Calm": "Weightless - Marconi Union",
            "Stressed": "Electric Feel - MGMT",
            "Tired": "Night Owl - Galimatias",
            "Sad": "Retrograde - James Blake",
            "Excited": "Taro - alt-J",
            "Anxious": "Cold Little Heart - Michael Kiwanuka"
        },
        "Energetic": {
            "Happy": "Can’t Hold Us - Macklemore",
            "Calm": "Pompeii - Bastille",
            "Stressed": "Believer - Imagine Dragons",
            "Tired": "High Hopes - Panic! At The Disco",
            "Sad": "Some Nights - fun.",
            "Excited": "Uptown Funk - Bruno Mars",
            "Anxious": "Radioactive - Imagine Dragons"
        }
    }

    if music in music_map:
        song = music_map[music].get(mood, song)

    if energy < 30:
        recommendation += " Add a restful break, warm drink, or calm stretch session."
    elif energy > 80:
        recommendation += " Try a brisk walk, creative burst, or high-energy playlist."
    else:
        recommendation += " Balance movement with rest and soothing music."

    sign = get_zodiac_sign(birthdate)
    zodiac_pred = zodiac_predictions.get(sign, "") if sign else ""

    return {
        "vibe": vibe,
        "quote": quote,
        "recommendation": recommendation,
        "song": song,
        "aura": aura,
        "zodiac": zodiac_pred,
        "sign": sign
    }

if st.button("✨ Analyze My Vibe"):
    report = compute_vibe(sleep, mood, energy, music, birthdate)

    st.markdown(
        f"""
        <div class='result-box'>
            <h2>✨ Today's Vibe Prediction</h2>
            <p style='font-size:1.05rem;'>{report['vibe']}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if report['sign']:
        st.markdown(
            f"""
            <div class='result-box'>
                <h3>🔮 Zodiac Prediction for {report['sign']}</h3>
                <p>{report['zodiac']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='card'><h3 class='card-title'>🔮 Aura Type</h3><p>{report['aura']}</p></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><h3 class='card-title'>🎧 Song Suggestion</h3><p>{report['song']}</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='card'><h3 class='card-title'>💡 Motivation Quote</h3><p>{report['quote']}</p></div>", unsafe_allow_html=True)
        st.markdown(f"<div class='card'><h3 class='card-title'>🧠 Self-Care Tip</h3><p>{report['recommendation']}</p></div>", unsafe_allow_html=True)

    st.subheader("📊 Daily Emotional Report")
    st.write(f"😴 Sleep Hours: {sleep}")
    st.write(f"😊 Mood: {mood}")
    st.write(f"🎵 Music Preference: {music}")
    st.write(f"⚡ Energy Level: {energy}/100")

    if birthdate:
        st.write(f"📅 Birthdate: {birthdate.strftime('%B %d, %Y')}")
    if report['sign']:
        st.write(f"🔮 Zodiac Sign: {report['sign']}")

    st.progress(energy)
    st.divider()
    st.caption("🌌 AuraSync — Your Digital Emotional Companion")
