import streamlit as st
import pandas as pd

# 1. Configuración de página ultra compacta
st.set_page_config(page_title="Practifacil - Catálogo", layout="wide", initial_sidebar_state="collapsed")

# 2. Inyección de CSS para diseño de fichas Neón y remover espacios muertos
st.markdown("""
    <style>
    .block-container {
        padding-top: 1.5rem !important;
        padding-bottom: 1rem !important;
    }
    .card-producto {
        background-color: #1a1c23;
        border: 2px solid #ffcc00;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 0px 0px 10px rgba(255, 204, 0, 0.2);
        margin-bottom: 5px;
    }
    .titulo-producto {
        color: #ffffff;
        font-size: 15px;
        font-weight: bold;
        height: 45px;
        overflow: hidden;
        margin-top: 10px;
        text-align: center;
    }
    .precio-producto {
        color: #ffcc00;
        font-size: 22px;
        font-weight: bold;
        margin: 5px 0;
        text-align: center;
    }
    .zona-contacto {
        background-color: #1a1c23;
        border: 2px dashed #25D366;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Practifacil - Catálogo Digital")
st.write("Mira nuestros productos disponibles y haz tu pedido directamente por WhatsApp.")

# Base de datos integrada apuntando a los archivos locales
data_productos = {
    "producto": [
        "Reloj Inteligente (Smartwatch) Deportivo Unixes",
        "Reloj Smartwacht Unixes",
        "5-In-1 USB-C SD Card Reader, USB 2.0 Type-C Data",
        "Reloj de Aguja Unixes",
        "Type-C Multi-Function Card Reader, OTG 3-in-1 Adapter"
    ],
    "categoria": ["relojes", "relojes", "conectividad", "relojes", "conectividad"],
    "precio_venta": [18.00, 15.00, 10.00, 12.00, 7.00],
    "imagen_local": [
        "./reloj1.avif",  
        "./reloj2.avif",  
        "./hub1.avif",    
        "./reloj3.avif",  
        "./hub2.avif"     
    ]
}

df_activos = pd.DataFrame(data_productos)

# 3. Sistema de pestañas para los productos
tab_relojes, tab_conectividad = st.tabs(["⌚ Relojes Unixes", "🔌 Conectividad & Adaptadores"])

def generar_grid_productos(dataframe_filtrado):
    columnas = st.columns(3)
    for indice, fila in enumerate(dataframe_filtrado.itertuples()):
        columna_actual = columnas[indice % 3]
        with columna_actual:
            st.markdown('<div class="card-producto">', unsafe_allow_html=True)
            try:
                st.image(fila.imagen_local, use_container_width=True)
            except Exception:
                st.caption("⚠️ Foto no encontrada")
            st.markdown(f'<div class="titulo-producto">{fila.producto}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="precio-producto">${float(fila.precio_venta):,.2f}</div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

# Renderizar cada pestaña según su categoría
with tab_relojes:
    df_relojes = df_activos[df_activos["categoria"] == "relojes"]
    generar_grid_productos(df_relojes)

with tab_conectividad:
    df_conectividad = df_activos[df_activos["categoria"] == "conectividad"]
    generar_grid_productos(df_conectividad)

# 4. RECUADRO DE ATENCIÓN DIRECTA CON COPIADO SEGURO
st.markdown("---")
st.markdown('<div class="zona-contacto">', unsafe_allow_html=True)
st.markdown("<h3 style='color: #25D366; margin-top:0;'>🟢 ¿Cómo hacer tu pedido?</h3>", unsafe_allow_html=True)
st.write("Copia nuestro número oficial aquí abajo con un solo toque para agregarnos o escanea el código QR:")

# Número en texto plano que el usuario puede ver
NUMERO_TELF = "+584144021239"

# Componente de Streamlit nativo para copiar texto al portapapeles sin usar links externos peligrosos
st.text_input("Número de WhatsApp:", value=NUMERO_TELF, disabled=True, label_visibility="collapsed")
st.caption("💡 Mantén presionado el recuadro gris arriba para copiar el número al instante.")

st.markdown("<br>", unsafe_allow_html=True)
st.write("📷 **O escanea el código QR con la cámara de tu teléfono para abrir el chat:**")

# Mostramos el QR que los teléfonos leen directo con la cámara sin pasar por el navegador
st.image("https://qrserver.com", width=140)

st.markdown('</div>', unsafe_allow_html=True)
