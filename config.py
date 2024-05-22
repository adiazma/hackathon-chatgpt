from openai import OpenAI
import pandas as pd
import json, time

total = []
client = OpenAI()
for item in json.loads(open('response_prompt.json').read()):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": """
            Del siguiente json {json_inicio} dame la clasificación de morosidad para la empresa Telefonica en el siguiente formato {json_fin} de la persona en cuestión. 
            SI NO se puede determinar a partir de la información proporcionada, APROXIMALA PARA TODOS LOS CAMPOS SEGUN LOS DATOS QUE TENGAS DE PERÚ. 
        """.format(
            json_inicio=json.dumps(item),
            json_fin=json.dumps({
                'clasificacion_tipo': 'responde solo con ALTO, MEDIO, BAJO',
                'notificacion': 'responde solo con WHATSAPP, EMAIL, CARTA, LLAMADA',
                'speech': 'SPEECH solicitando el pago de la mora SI ES QUE APLICA'
            })
        )},
        ]
    )
    res = response.choices[0].message.content
    try:
        total.append({**json.loads(res), **item})
        print(total[-1])
    except:
        print(f'ERROR: {res}')
    time.sleep(.5)

with open('response_prompt_2.json', 'w') as file:
    json.dump(total, file, indent=4)