#PRIMEIRA FORMA
def inverter_String(palavra:str) -> str:
    return palavra[::-1]



print(inverter_String('palavra'))

#SEGUNDA FORMA
string = "AUGUSTO"

string_invertida = ""

for i in range(len(string) - 1, -1, -1):
    string_invertida += string[i]


print(f"String original: {string}")
print(f"String invertida: {string_invertida}")