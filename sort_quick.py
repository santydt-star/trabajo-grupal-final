# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n, i, j, pivote
    items = list(vals)
    n = len(items)
    i=-1
    j=0
    pivote=n-1
    # TODO: inicializar punteros/estado

def step():
    global items, n, i, j, pivote
    if pivote>=0:
        if j<pivote:
            if items[j]<items[pivote]:
                i=i+1
                items[i],items[j]= items[j],items[i]
                j=j+1
                return {"a": i, "b": j-1,"swap": True, "done": False}
            if items[j]>=items[pivote]:
                j=j+1
                return {"a": j-1, "b": pivote, "swap": False, "done": False}
        if j==pivote:
           i=i+1
           items[i],items[pivote]=items[pivote],items[i]
           return {"a": i, "b": pivote, "swap": True, "done": False}
        if j>pivote:
            pivote=pivote-1
            i=-1
            j=0
            return {"a": None, "b":None, "swap":False, "done": False}
    if pivote<0:
        return {"done": True}
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    
