import unicodedata
import re

def sanitizar(texto):
    # Convertir a minúsculas
    texto = texto.lower()

    # Normalizar y eliminar acentos / tildes / diéresis
    texto = unicodedata.normalize('NFD', texto)
    texto = texto.encode('ascii', 'ignore').decode('utf-8')

    # Reemplazar ñ → n (se pierde al eliminar acentos, pero aseguramos)
    texto = texto.replace("ñ", "n")

    # Eliminar caracteres no alfanuméricos, excepto espacios
    texto = re.sub(r'[^a-z0-9\s]', '', texto)

    # Limpiar espacios múltiples
    texto = re.sub(r'\s+', ' ', texto).strip()

    return texto