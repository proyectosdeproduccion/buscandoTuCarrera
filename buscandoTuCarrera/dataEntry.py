import os
with open("UX_templates/carrera_template.html", "r") as file:
    content = file.read()
with open("UX_templates/template_style.css", "r") as file:
    css = file.read()

info = ["Arquitectura", "UADE", "no hay imagen", "5 AÑOS", "CABA", "Privada", "Arquitecto/a", "Mañana y tarde", "Presencial", "https://www.uade.edu.ar/facultad-de-arquitectura-y-diseno/arquitectura", "../../css/footerHeader.css", "../template_style.css"]

content = content.replace("{nombreCarrera}", info[0])
content = content.replace("{nombreFacultad}", info[1])
content = content.replace("{imagen}", info[2])
content = content.replace("{duracion}", info[3])
content = content.replace("{ubicacion}", info[4])
content = content.replace("{publicoPrivado}", info[5])
content = content.replace("{titulo}", info[6])
content = content.replace("{turnos}", info[7])
content = content.replace("{modalidad}", info[8])
content = content.replace("{linkPag}", info[9])
content = content.replace("{cssFooterHeader}", info[10])
content = content.replace("{cssTemplate}", info[11])

if os.path.isdir("../paginasTerminadas") == False:
    os.mkdir("../paginasTerminadas")

with open("UX_templates/paginasTerminadas/" +info[0] + "_" + info[1] + ".html", "w") as file:
    file.write(content)
    print("Pagina creada")
