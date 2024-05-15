import json

with open("compositores.json", "r", encoding="utf8") as f:
    dataset = json.load(f)

compositores = dataset["compositores"]

compositores.append(dict({
    "id": "C1001",
    "nome": "Arnold Schoenberg",
    "bio": "Arnold Schoenberg (Viena, 13 de setembro de 1874 — Los Angeles, 13 de julho de 1951) foi um compositor, maestro, teórico musical e pintor austríaco. Foi o fundador da escola de música dodecafônica.",
    "periodo": "Moderno",
    "dataNasc": "1874-09-13",
    "dataObito": "1951-07-13",
}))

compositores.append(dict({
    "id": "C1002",
    "nome": "Igor Stravinsky",
    "bio": "Igor Stravinsky (Oranienbaum, 17 de junho de 1882 — Nova Iorque, 6 de abril de 1971) foi um dos mais importantes compositores do século XX. Nasceu na Rússia e depois se naturalizou francês e americano.",
    "periodo": "Moderno",
    "dataNasc": "1882-06-17",
    "dataObito": "1971-04-06",
}))

compositores.append(dict({
    "id": "C1003",
    "nome": "Alban Berg",
    "bio": "Alban Berg (Viena, 9 de fevereiro de 1885 — Viena, 24 de dezembro de 1935) foi um compositor austríaco do início do século XX, associado ao expressionismo e à Segunda Escola de Viena.",
    "periodo": "Moderno",
    "dataNasc": "1885-02-09",
    "dataObito": "1935-12-24",
}))

compositores.append(dict({
    "id": "C1004",
    "nome": "Anton Webern",
    "bio": "Anton Webern (Viena, 3 de dezembro de 1883 — Mittersill, 15 de setembro de 1945) foi um compositor e maestro austríaco, um dos mais importantes representantes do dodecafonismo.",
    "periodo": "Moderno",
    "dataNasc": "1883-12-03",
    "dataObito": "1945-09-15",
}))

compositores.append(dict({
    "id": "C1005",
    "nome": "Paul Hindemith",
    "bio": "Paul Hindemith (Hanau, 16 de novembro de 1895 — Frankfurt am Main, 28 de dezembro de 1963) foi um compositor, violinista, maestro, educador e teórico musical alemão.",
    "periodo": "Moderno",
    "dataNasc": "1895-11-16",
    "dataObito": "1963-12-28",
}))

with open("dataset.json", "w", encoding="utf8") as f:
    json.dump(dataset, f, indent=2)