from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()

def analyze_video_confidence(video_path: str):
    """Analisis video untuk mendeteksi apakah seseorang terlihat percaya diri."""

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    with open(video_path, "rb") as f:
        video_bytes = f.read()

    # Prompt yang diperbagus dan terstruktur
    prompt = """
            Kamu adalah analis komunikasi non-verbal yang menilai kepercayaan diri seseorang dalam interview.
            Analisis berdasarkan ekspresi wajah, kontak mata, gesture, posture, dan intonasi suara (jika ada suara).

            Ikuti format output wajib berikut:
            analisis: [penjelasan lengkap berdasarkan video]
            kesimpulan: [ya/tidak]

            Aturan:
            - "ya" berarti orang tersebut percaya diri
            - "tidak" berarti orang tersebut tidak percaya diri
            - Tidak boleh memberikan jawaban selain "ya" atau "tidak" pada bagian kesimpulan
            """

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=types.Content(
            parts=[
                types.Part(
                    inline_data=types.Blob(
                        data=video_bytes,
                        mime_type="video/mp4"
                    )
                ),
                types.Part(text=prompt)
            ]
        )
    )

    return response.text