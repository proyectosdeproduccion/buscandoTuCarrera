# -*- coding:utf-8 -*-
import pandas

infoCarreras = []
csv_file = 'final/todasCarreras/ejemplo1.csv'
data = pandas.read_csv(csv_file, encoding="utf-8")
for i in data.iterrows():
    infoCarreras.append(i[1].array)

#if os.path.isdir("UX_templates/paginasTerminadas") == False:
#    os.mkdir("UX_templates/paginasTerminadas")

for x in infoCarreras:
    with open("final/todasCarreras/carrera_template.html", "r", encoding="utf-8") as file:
        content = file.read()
    #carrera = [x[2], x[3], "no hay imagen", x[4], x[5], x[6], x[9], x[8], x[9], x[10], "../../css/footerHeader.css", "../template_style.css", x[0]]
    content = content.replace("{codigo}", str(x[0]))
    content = content.replace("{nombreCarrera}", x[2])
    content = content.replace("{nombreFacultad}", x[3])
    content = content.replace("{imagen}", F"../../imagenes/{x[2].lower()}/{x[11]}.jpg")
    content = content.replace("{duracion}", x[4])
    content = content.replace("{ubicacion}", x[5])
    content = content.replace("{publicoPrivado}", x[6])
    content = content.replace("{titulo}", x[7])
    content = content.replace("{turnos}", x[8])
    content = content.replace("{modalidad}", x[9])
    content = content.replace("{linkPag}", x[10])
    content = content.replace("{cssFooterHeader}", "../../../../css/footerHeader.css")
    content = content.replace("{cssTemplate}", "../../../cssCarreras/template_style.css")
    

    with open(f"final/todasCarreras/{str(x[3]).lower()}Objetivos.txt", "r", encoding="utf-8") as file:
        objetivos = file.read()
        content = content.replace("{objetivos}", objetivos)

    with open(f"final/todasCarreras/{str(x[0]).split(sep='_')[0].lower()}Info.txt", "r", encoding="utf-8") as file:
        infoCarrera = file.read()
        content = content.replace("{infoCarrera}", infoCarrera)
    with open("final/todasCarreras/arquitectura&diseño/carreras/" + str(x[2]).replace(" ", "") + "/" + x[0] + ".html", "w", encoding="utf-8") as file:
        file.write(str(content).replace("�", "ñ"))
        print(f"Pagina de {x[0]} creada")
