import os, re
import xml.etree.ElementTree as ET

html_content = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ruas de Braga (Século XVIII)</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
    <h1>Ruas de Braga (Século XVIII)</h1>
<body>
    <ul class="w3-ul w3-hoverable">
"""

html_content_street_page = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
"""

directory_text = 'texto'
streetNames = []

def createResultsDir():
    if not os.path.exists('resultados'):
        os.makedirs('resultados')

def sortStreetNames():
    streetNames.sort()

def createMainPage():
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

def createStreetsPages():
    for streetName in streetNames:
        linkname = streetName.replace(" ", "")
        with open(f'resultados/{linkname}.html', 'w', encoding='utf-8') as f:
            f.write(html_content_street_page)
            f.write(f'\t<title>{streetName}</title>\n')
            f.write("</head>\n")
            f.write("<body>\n")
            f.write(f"\t<h1>{streetName}</h1>")

def addStreetPagesLinks():
    with open('index.html', 'a', encoding='utf-8') as f:
        for streetName in streetNames:
            linkname = streetName.replace(" ", "")
            f.write(f'\t\t<li><a href="resultados/{linkname}.html">{streetName}</a></li>\n')

        f.write("\t</ul>\n</body>\n")

def getStreetNames():
    for archive in os.listdir(directory_text):
        if archive.endswith('.xml'):
            path = os.path.join(directory_text, archive)

            tree = ET.parse(path)
            root = tree.getroot()

            streetName = root.find('.//meta/nome').text
            streetNames.append(streetName)


def fixwhitespaces(string):
    return re.sub(r'(?<!\n)\s{2,}', ' ', string)

def xml_to_html():
    
    for arq in os.listdir(directory_text):
        if arq.endswith('.xml'):
            path = os.path.join(directory_text, arq)
            tree = ET.parse(path)
            root = tree.getroot() 
            init = ""
            text = ""

            name = root.find('.//meta/nome').text
            filename = name.replace(" ", "")

            for figura in root.findall('.//figura'):
                imagem_path = figura.find('imagem').attrib['path']
                subtext = figura.find('legenda').text

                img_html = f'<img src="{imagem_path}" alt="{subtext}" style="max-width: 800px; max-height: 500px;">'

                init += f'\t<figure>\n\t\t{img_html}\n\t\t<figcaption>{subtext}</figcaption>\n\t</figure>\n'

            # Iterar sobre os elementos <para>
            for elem in root.findall('.//corpo/para'):
                # Obter todo o texto dentro do elemento e suas subtags
                full_text = ET.tostring(elem, method='text', encoding='utf-8').decode('utf-8')
                text += full_text  # Adicionar uma quebra de linha após cada elemento <para>

    
            with open(f'resultados/{filename}.html', 'w', encoding='utf-8') as r:
                r.write(init)
                r.write("\t<p>")
                for line in text.splitlines():
                    r.write(fixwhitespaces(line))
                r.write("</p>\n")
                r.write("\t<button onclick=\"window.location.href = '../index.html';\">Voltar para Página Principal</button>\n")
                r.close()
    

def main():
    createResultsDir()
    createMainPage()
    getStreetNames()
    sortStreetNames()
    createStreetsPages()
    addStreetPagesLinks()
    xml_to_html()

if __name__ == '__main__':
    main()