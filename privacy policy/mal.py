import speech_recognition as sr
import nltk
from nltk.tokenize import word_tokenize

# Descarga recursos necesarios de NLTK
nltk.download('punkt')

# Lista de palabras ofensivas (puedes ampliarla)
bad_words = ["palabra1", "palabra2", "palabra3"]

# Inicializa el reconocedor de voz
r = sr.Recognizer()

# Captura el audio desde el micrófono
with sr.Microphone() as source:
    print("Di algo:")
    audio = r.listen(source)

try:
    # Transcribe el audio a texto
    transcript = r.recognize_google(audio, language="es-ES")

    # Tokeniza el texto en palabras
    words = word_tokenize(transcript)

    # Comprueba si se encuentran palabras ofensivas
    for word in words:
        if word.lower() in bad_words:
            print("¡Contenido inapropiado detectado!")
            break
    else:
        print("No se encontraron palabras ofensivas.")

except sr.UnknownValueError:
    print("No se pudo entender el audio.")
except sr.RequestError as e:
    print(f"Error en la solicitud: {e}")
