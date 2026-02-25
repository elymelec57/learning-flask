from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
    # Importar dentro de la función para evitar problemas de importación circular
    try:
        from app import genai_client, model_name
        if genai_client is None:
            return _('Error: the translation service is not configured (missing API key).')
    except ImportError:
        return _('Error: the translation service is not available.')

    if not text:
        return ""
    
    try:
        # Prompt más específico para asegurar que solo devuelva el texto traducido
        prompt = (
            f"Traduce el siguiente texto del idioma con código '{source_language}' "
            f"al idioma con código '{dest_language}'. "
            f"Devuelve únicamente el texto traducido, sin comillas ni explicaciones:\n\n{text}"
        )
        
        if current_app:
            current_app.logger.info(f"Gemini prompt: {prompt}")
        
        # Llamada a la API de Gemini
        response = genai_client.models.generate_content(
            model=model_name,
            contents=prompt
        )
        
        # Verificación de respuesta válida
        if response and response.text:
            return response.text.strip()
        else:
            return _('Error: empty response from translation service.')
            
    except Exception as e:
        if current_app:
            current_app.logger.error(f"Translation error: {str(e)}")
        else:
            print(f"Translation error: {str(e)}")
        return _('Error: the translation service failed.')