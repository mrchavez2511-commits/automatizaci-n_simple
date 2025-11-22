from selenium.webdriver.common.by import By

def obtener_precio_accion(driver, consulta):

    # Search en Google
    driver.get(f"https://www.google.com/search?q=precio+acción+{consulta}")

    try:
        # Nombre de la empresa
        empresa = driver.find_element(
            By.CSS_SELECTOR,
            "div.PZPZlf.ssJ7i.B5dxMb"
        ).text

        # Precio
        precio = driver.find_element(
            By.CSS_SELECTOR,
            "span[jsname='vWLAgc']"
        ).text

        # Divisa (USD, MXN, EUR…)
        divisa = driver.find_element(
            By.CSS_SELECTOR,
            "span.knFDje"
        ).text

        # Ticker (AAPL, MSFT, TSLA…)
        ticker = driver.find_element(
            By.CSS_SELECTOR,
            "div.HfMth"
        ).text

        return f"{empresa} [{ticker}]  ${precio} {divisa.upper()}."

    except Exception:
        return "No se pudo obtener el precio de la acción en este momento."
