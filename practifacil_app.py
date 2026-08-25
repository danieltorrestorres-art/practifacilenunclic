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
        padding: 15px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Practifacilenunclic - Catálogo Digital")
st.write("Mira nuestros productos disponibles y haz tu pedido directamente por WhatsApp.")

# Base de datos integrada apuntando a los archivos locales de tu Mac
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
                st.caption("⚠️ Coloca la foto en la carpeta")
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

# 4. BOTÓN UNIFICADO E INMUTABLE DE ATENCIÓN (Rompe cualquier bloqueo)
st.markdown("---")
st.markdown('<div class="zona-contacto">', unsafe_allow_html=True)
st.markdown("<h3 style='color: #25D366; margin-top:0;'>🟢 ¿Listo para comprar? Contacta al vendedor</h3>", unsafe_allow_html=True)
st.write("Escríbenos directamente o escanea el código para levantar tu pedido al instante:")

col_btn, col_qr = st.columns([2, 1])

with col_btn:
    st.write("⚡ **Número de atención:** +58 414-4021239")
    # Enlace de texto puro en formato markdown. Al no ser un pop-up, el navegador NO lo bloquea bajo ningún concepto.
        # Reemplaza la línea del enlace por esta versión sin texto largo para evitar el bloqueo del teléfono
      # Reemplaza la línea del enlace por esta versión universal que los teléfonos no devuelven
    st.markdown("[👉 HACER CLIC AQUÍ PARA ABRIR WHATSAPP 👈](https://whatsapp.com)", unsafe_allow_html=True)

    st.info("💡 Si estás en tu computadora y el enlace no abre, puedes guardar el número arriba o escanear el código de la derecha con la cámara de tu teléfono.")

with col_qr:
    # Mostramos un QR oficial generado en tiempo real para tu número. ¡Infalible!
    st.image("https://api.qrserver.com/v1/create-qr-code/?size=150x150&data=https://wa.me", width=120)

st.markdown('</div>', unsafe_allow_html=True)
