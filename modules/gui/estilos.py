COLORES_LOTERIA = {
    'fondo_principal': '#F8F9FA',        # Blanco suave
    'fondo_secundario': '#E5E7EB',       # Gris muy claro
    'acento_dorado': '#FFD700',          # Dorado brillante
    'acento_verde': '#228B22',           # Verde dinero
    'azul_confianza': '#1E3A8A',         # Azul marino
    'azul_claro': '#3B82F6',             # Azul medio
    'rojo_emocion': '#DC2626',           # Rojo ganar
    'texto_principal': '#1F2937',        # Gris oscuro
    'texto_secundario': '#6B7280',       # Gris medio
}

ESTILO_BOTONES = {
    'font': ('Arial', 12, 'bold'),
    'height': 2,
    'width': 15,
    'relief': 'raised',
    'bd': 2,
    'cursor': 'hand2',
    'padx': 10,
    'pady': 10,
}

BOTONES_PRINCIPALES = {
    'bg': COLORES_LOTERIA['acento_verde'],
    'fg': 'white',
    'activebackground': COLORES_LOTERIA['acento_dorado']
} 