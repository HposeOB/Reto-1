import pandas as pd

path = "hoja.xlsx"

datos = pd.read_excel(path,  names=['nombre', 'email'])

email = datos.iloc[:, 1]
email_filtrado = []
for i in email:
    if i not in email_filtrado:
        email_filtrado.append(i)

print(email_filtrado)