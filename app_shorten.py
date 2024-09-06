# Librerias y Recursos
import streamlit as st
import requests
import pyshorteners
import json
from st_social_media_links import SocialMediaIcons

# Función para acortar URL
def shorten_url_isgd(original_url, custom_name):
    base_url = "https://is.gd/create.php"
    parameters = {
        "format": "json",
        "url": original_url,
        "shorturl": custom_name
    }
    response = requests.get(base_url, params=parameters)
    response_data = response.json()
    if "shorturl" in response_data:
        shorted_url = response_data["shorturl"]
        return shorted_url
    else:
        st.error("Error al acortar la URL")
        if "errormessage" in response_data:
            st.error("Mensaje de error:", response_data["errormessage"])
        return None

# Configuración de la página
st.set_page_config(page_title="Acortador de Enlaces Personalizado", page_icon=":link:")

# Título y logo
st.title("ACORTADOR DE URL PERSONALIZADO")
st.image("https://elnuevoempresario.com/wp-content/uploads/2019/04/acortar-url.-herramientas-para-acortar-enlaces.jpg", width=100)

# Entrada de URL original
original_url = st.text_input("Ingresa la URL original:")

# Entrada de nombre personalizado
custom_name = st.text_input("Ingresa el nombre personalizado para la URL:")

# Botón para acortar URL
if st.button("Acortar URL"):
    if not original_url:
        st.warning("Por favor, ingrese una URL.")
    else:
        shortened_url = None
        attempt = 1
        while not shortened_url and attempt <= 5:
            shortened_url = shorten_url_isgd(original_url, custom_name)
            if not shortened_url:
                if custom_name:
                    custom_name = f"{custom_name}_{attempt}"
                else:
                    custom_name = f"short_{attempt}"
                attempt += 1

        if shortened_url:
            st.success(f"Original URL: {original_url}")
            st.success(f"URL acortada y personalizada: {shortened_url}")
        else:
            st.error("Error al acortar la URL después de varios intentos")

# Pie de página con información del desarrollador y logos de redes sociales
st.markdown("""
---
**Desarrollador:** Edwin Quintero Alzate<br>
**Email:** egqa1975@gmail.com<br>
""")

social_media_links = [
    "https://www.facebook.com/edwin.quinteroalzate",
    "https://www.linkedin.com/in/edwinquintero0329/",
    "https://github.com/Edwin1719"
]

social_media_icons = SocialMediaIcons(social_media_links)
social_media_icons.render()