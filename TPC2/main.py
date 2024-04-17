import json 
import os

listacidades = {}

def getData() -> dict:
    with open("mapa-virtual.json", "r") as f:
        data = json.load(f)

    return data

def getLigacoes(data: dict) -> dict:
    ligacoes = {}

    for ligacao in data['ligacoes']:
        if ligacao['origem'] not in ligacoes:
            ligacoes[ligacao['origem']] = []
        
        ligacoes[ligacao['origem']].append({'destino': ligacao['destino'], 'distância': ligacao['distância']})

    return ligacoes

def generate_pages_cities(data: dict):
    for cidade in data['cidades']:
        html = f"""<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{cidade['nome']}</title>
    <link rel="stylesheet" type="text/css" href="../style.css">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <style>
        #ligacoes {{
            font-family: Arial, Helvetica, sans-serif;
            border-collapse: collapse;
            width: 50%;
        }}

        #ligacoes td, #ligacoes th {{
            border: 1px solid #ddd;
            padding: 8px;
        }}

        #ligacoes tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}

        #ligacoes tr:hover {{
            background-color: #ddd;
        }}

        #ligacoes th {{
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #04AA6D;
            color: white;
        }}
    </style>
</head>
<body>
    <h1><a href="index.html">Mapa Virtual</a></h1>
    <h2>{cidade['nome']}</h2>
    <p>{cidade['descrição']}</p>
    <h4>População</h4>
    {cidade['população']}
    <h4>Distrito</h4>
    {cidade['distrito']}
    <h3>Ligações a outras cidades</h3>
        <table id= "ligacoes">
            <tr>
                <th>Cidades</th>
                <th>Distância</th>
            </tr>\n"""

        with open(f"results/{cidade['id']}.html", "w", encoding='utf-8') as f:
            f.write(html)

def adicionaligacoes(ligacoes: dict):
    html = ""
    for ligacao, info in ligacoes.items():
        for infoligacao in info:
            html += f"""\t\t\t<tr>
\t\t\t\t<td>{listacidades[ligacao]} -&gt; {listacidades[infoligacao['destino']]}</td>
\t\t\t\t<td><span class="distancia">{infoligacao['distância']}km</span></td>
\t\t\t</tr>\n"""


            with open(f"results/{ligacao}.html", "a", encoding='utf-8') as f:
                f.write(html)
                html = ""
                f.close()

def generate_index_html(data: dict):
    for cidade in data['cidades']:
        listacidades[cidade['id']] = cidade['nome']

    html = """<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa Virtual</title>
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
</head>
<body>
    <h1>Mapa Virtual</h1>
    <h2>Lista Cidades</h2>
    <ul class="w3-ul w3-hoverable">\n"""

    for idcidade, nome in listacidades.items():
        html += f"""\t\t<li><a href="{idcidade}.html">{nome}</a></li>\n"""

    html += """\t</ul>\n</body>\n</html>"""

    with open("results/index.html", "w", encoding='utf-8') as f:
        f.write(html)

def main():

    os.makedirs("results", exist_ok=True)
    data = getData()
    ligacoes = getLigacoes(data)

    generate_pages_cities(data)    
    generate_index_html(data)
    adicionaligacoes(ligacoes)

if __name__ == '__main__':
    main()
