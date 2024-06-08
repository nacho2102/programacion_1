equipos = ["Independiente", "Racing", "Boca", "Defensa", "Dock Sud", "Riber", "San Lorenzo"]
puntos = [32, 29, 36, 30, 30, 28, 26]
dif_goles = [12, 10, 16, 9, 10, 8, 8]

for i in range(len(equipos)  - 1):
    auxiliar = None
    for j in range(i + 1, len(equipos)):
        if puntos[i] < puntos[j]:
            auxiliar = puntos[j]
            puntos[j] = puntos[i]
            puntos[i] = auxiliar
            
            auxiliar = equipos[j]
            equipos[j] = equipos[i]
            equipos[i] = auxiliar

            auxiliar = dif_goles[j]
            dif_goles[j] = dif_goles[i]
            dif_goles[i] = auxiliar

        elif puntos[i] == puntos[j] and dif_goles[i] < dif_goles[j]:
            auxiliar = equipos[j]
            equipos[j] = equipos[i]
            equipos[i] = auxiliar

            auxiliar = puntos[j]
            puntos[j] = puntos[i]
            puntos[i] = auxiliar

            auxiliar = dif_goles[j]
            dif_goles[j] = dif_goles[i]
            dif_goles[i] = auxiliar


for i in range(len(equipos)):       
    print(puntos[i], equipos[i], dif_goles[i])