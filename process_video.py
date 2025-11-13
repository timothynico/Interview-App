from dotenv import load_dotenv
import os
import google.generativeai as genai
from google.generativeai import types
import mimetypes

load_dotenv()


def analyze_video_confidence(video_path: str):
    """Analisis video untuk mendeteksi apakah seseorang terlihat percaya diri."""

    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

    with open(video_path, "rb") as f:
        video_bytes = f.read()

    mime_type = mimetypes.guess_type(video_path)[0] or "video/webm"

    # Prompt yang diperbagus dan terstruktur
    prompt = """
            Kamu adalah analis komunikasi non-verbal yang menilai kepercayaan diri seseorang dalam interview.
            Analisis berdasarkan ekspresi wajah, kontak mata, gesture, posture, dan intonasi suara (jika ada suara).

            Ikuti format output wajib berikut:
            analisis: [penjelasan lengkap berdasarkan video]
            kesimpulan: [level]

            level ini berupa 0 sampai 100, 0 berarti sangat tidak percaya diri, 100 berarti sangat percaya diri.
            Isi bagian [level] hanya dengan angka.

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
                        mime_type=mime_type
                    )
                ),
                types.Part(text=prompt)
            ]
        )
    )

    return response.text


if __name__ == "__main__":
    video_path = "video_recordings/answer_q1_20251109_145451.webm"
    result = analyze_video_confidence(video_path)
    print(result)