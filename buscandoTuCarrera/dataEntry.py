import os
import pandas

infoCarreras = []

data = pandas.read_csv("csvARQyDIS.csv")
for i in data.iterrows():
    infoCarreras.append(i[1].array)

if os.path.isdir("../paginasTerminadas") == False:
    os.mkdir("../paginasTerminadas")

for x in infoCarreras:
    with open("UX_templates/carrera_template.html", "r") as file:
        content = file.read()
    carrera = [x[2], x[3], "no hay imagen", x[4], x[5], x[6], x[9], x[8], x[9], x[10], "../../css/footerHeader.css", "../template_style.css", x[0]]
    content = content.replace("{codigo}", x[0])
    content = content.replace("{nombreCarrera}", x[2])
    content = content.replace("{nombreFacultad}", x[3])
    content = content.replace("{imagen}", "no hay imagen")
    content = content.replace("{duracion}", x[4])
    content = content.replace("{ubicacion}", x[5])
    content = content.replace("{publicoPrivado}", x[6])
    content = content.replace("{titulo}", x[7])
    content = content.replace("{turnos}", x[8])
    content = content.replace("{modalidad}", x[9])
    content = content.replace("{linkPag}", x[10])
    content = content.replace("{cssFooterHeader}", "../../css/footerHeader.css")
    content = content.replace("{cssTemplate}", "../template_style.css")

    with open("UX_templates/paginasTerminadas/" + x[0] + ".html", "w") as file:
        file.write(content)
        print(f"Pagina de {x[0]} creada")
