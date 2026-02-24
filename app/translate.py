from flask_babel import _
from app import genai_client, model_name

def translate(text, source_language, dest_language):
    if not text:
        return ""
    try:
        # Prompt en español para la traducción
        prompt = (
            f"Actúa como un traductor experto. Traduce el siguiente texto del idioma '{source_language}' al idioma '{dest_language}'. "
            f"Devuelve únicamente la traducción, sin comentarios adicionales: '{text}'"
        )
        # Usando el nuevo cliente y método de generación
        response = genai_client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"Translation error: {str(e)}") # Útil para depuración
        return _('Error: the translation service failed.')