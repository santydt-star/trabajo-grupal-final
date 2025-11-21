# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = [] #lista a ordenar
n = 0      #cantidad de items
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)  
    i = 0
    j = 0
def step():
    global items, n, i, j

    if n<=1 or i>=n-1:    #si no hay nada que ordenar o termino todas las pasadas
        return {"done": True}

    a=j
    b=j+1
    swap=False

    if items[a] > items[b]:
        items[a], items[b] = items[b], items[a]
        swap=True

    j =j+1  #avanza la "mini pasada"

    if j>=n-i-1:
        j=0    #reiniciamos las "mini pasadas"
        i=i+1  #incrementamos el contador de pasadas

    if i>=n-1:
        return {"done": True}   
#se devuelve la info del visualizador
    return {"a": a, "b": b, "swap": swap, "done": False}

 
