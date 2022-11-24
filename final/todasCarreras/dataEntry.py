import os
import pandas

infoCarreras = []

data = pandas.read_csv("arquitectura&diseño.csv")
for i in data.iterrows():
    infoCarreras.append(i[1].array)

#if os.path.isdir("UX_templates/paginasTerminadas") == False:
#    os.mkdir("UX_templates/paginasTerminadas")

for x in infoCarreras:
    with open("carrera_template.html", "r") as file:
        content = file.read()
    carrera = [x[2], x[3], "no hay imagen", x[4], x[5], x[6], x[9], x[8], x[9], x[10], "../../css/footerHeader.css", "../template_style.css", x[0]]
    content = content.replace("{codigo}", x[0])
    content = content.replace("{nombreCarrera}", x[2])
    content = content.replace("{nombreFacultad}", x[3])
    content = content.replace("{imagen}", x[11])
    content = content.replace("{duracion}", x[4])
    content = content.replace("{ubicacion}", x[5])
    content = content.replace("{publicoPrivado}", x[6])
    content = content.replace("{titulo}", x[7])
    content = content.replace("{turnos}", x[8])
    content = content.replace("{modalidad}", x[9])
    content = content.replace("{linkPag}", x[10])
    content = content.replace("{cssFooterHeader}", "../../../../css/footerHeader.css")
    content = content.replace("{cssTemplate}", "../../../cssCarreras/template_style.css")

    with open(f"{str(x[3]).lower()}Objetivos.txt", "r") as file:
        objetivos = file.read()
        content.replace("{objetivos}", objetivos)

    with open(f"{str(x[0]).split(sep='_')[0].lower()}Objetivos.txt", "r") as file:
        infoCarrera = file.read()
        content.replace("{infoCarrera}", infoCarrera)

    with open("arquitectura&diseño/carreras/" + x[2] + "/" + x[0] + ".html", "w") as file:
        file.write(content)
        print(f"Pagina de {x[0]} creada")
