import io
from gtts import gTTS

from mdclense.parser import MarkdownParser

# Model selection


#  Audio generation 
# Generation audio with gTTS
def generate_audio(answer, voice_lang, slow_speech):
    parser = MarkdownParser() # convert from markdown to text
    plain_text = parser.parse(answer)
    tts = gTTS(
        text=plain_text, 
        lang=voice_lang, 
        slow=slow_speech,
        tld='com'  #  US English accent
    )
    
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes