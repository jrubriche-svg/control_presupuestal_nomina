# =============================================================================
# MAIN - CON CARGA RÁPIDA DE FECHA
# =============================================================================
def main():
    # Inicializar session state
    if "pagina_actual" not in st.session_state:
        st.session_state.pagina_actual = "INICIO"
    
    # 🔹 Cargar la fecha de actualización SIEMPRE al inicio
    # Esta función es rápida porque solo lee 1 fila
    if "fecha_actualizacion" not in st.session_state:
        fecha = obtener_fecha_actualizacion()
        st.session_state.fecha_actualizacion = fecha
    
    # Cargar estilos
    cargar_estilos()
    
    # Navegación
    if st.session_state.pagina_actual == "INICIO":
        mostrar_pantalla_inicial()
    elif st.session_state.pagina_actual == "POR_FUENTE":
        mostrar_pantalla_por_fuente()
    elif st.session_state.pagina_actual == "RECURSOS_PROPIOS":
        mostrar_pantalla_recursos_propios()
    elif st.session_state.pagina_actual == "SGP":
        mostrar_pantalla_sgp()

if __name__ == "__main__":
    main()
