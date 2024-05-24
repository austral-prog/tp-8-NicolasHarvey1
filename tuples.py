def get_coordinate(record):
    treasure, coordinate = record
    return coordinate



def convert_coordinate(coordinate):
    num, letra = coordinate
    return num, letra


def create_record(azara_record, rui_record):
    tesoro, coordenada1 = azara_record
    ubicación, coordenada2, cuadrante = rui_record
    num, letra = coordenada1
    unpack_coordenanda1 = num, letra
    if  unpack_coordenanda1 == coordenada2:
        return tesoro, coordenada1, ubicación, coordenada2, cuadrante
    else:
        return "not a match"
