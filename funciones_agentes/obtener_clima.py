# funciones_agente/obtener_clima.py
from selenium.webdriver.common.by import By

def obtener_clima(driver, consulta):
    """
    Obtiene el clima actual de una ciudad usando una búsqueda en Google.

    Parámetros
    ----------
    driver : selenium.webdriver.Chrome
        Instancia del WebDriver ya inicializada.
    consulta : str
        Texto que escribió el usuario (por ejemplo: "clima en oaxaca").

    Returns
    -------
    str
        Mensaje con la información del clima o un mensaje de error.
    """
    # Hacemos la búsqueda en Google
    driver.get(f"https://www.google.com/search?q=clima+{consulta}")

    try:
        # Ubicación (por si Google la corrige o la completa)
        ubicacion = driver.find_element(By.ID, "wob_loc").text

        # Temperatura en grados Celsius
        temperatura = driver.find_element(By.ID, "wob_tm").text

        # Descripción del clima (parcialmente nublado, soleado, etc.)
        descripcion = driver.find_element(By.ID, "wob_dc").text

        # Opcional: sensación térmica
        # sensacion = driver.find_element(By.ID, "wob_ttm").text

        return f"El clima en {ubicacion} es de {temperatura}°C, {descripcion.lower()}."
    except Exception:
        return "No se pudo obtener el clima en este momento."
