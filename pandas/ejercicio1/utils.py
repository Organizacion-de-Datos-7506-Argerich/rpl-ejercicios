def calcular_cuatrimestre(fecha) -> str:
    splitted = fecha.split('-')
    if splitted[1] in ['05', '06', '07', '08']:
        return '2C'
    return '1C'