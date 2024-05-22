from openai import OpenAI
import pandas as pd
import json, time

total = []
client = OpenAI()
df = pd.read_excel('datos_prueba.xlsx')
for item in df.to_dict('records'):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": """
            Del siguiente json {json_inicio} dame la siguiente informacion {json_fin} donde "xx" viene del analisis que ahgas del primer json.
            SI NO se puede determinar a partir de la información proporcionada, APROXIMALA PARA TODOS LOS CAMPOS SEGUN LOS DATOS QUE TENGAS DE PERÚ. 
            Responde SOLO con el JSON.
        """.format(
            json_inicio=json.dumps(item),
            json_fin=json.dumps({
                'Rango de Edad': 'xx',
                'Nivel Socioeconomico': 'xx',
                'Region del Pais': 'xx',
                'Antecedentes de Mora': 'xx',
                'Hanito de consumo': 'xx',
                'Tipo de Personalidad': 'xx',
                'Responsabilidad': 'xx',
                'Empatia': 'xx',
                'Estabilidad Emocional': 'xx',
                'Honestidad': 'xx',
                'Nivel de Comunicacion': 'xx',
            })
        )},
        ]
    )
    total.append({**json.loads(response.choices[0].message.content), **item})
    print(total[-1])
    time.sleep(.5)

with open('response_prompt.json', 'w') as file:
    json.dump(total, file, indent=4)