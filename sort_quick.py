# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i=0
j=0
pivote=0
fase=""
# Agregá acá tus punteros/estado, p.ej.:
# i = 0; j = 0; fase = "x"; stack = []

def init(vals):
    global items, n, i, j, pivote, fase
    items = list(vals)
    n = len(items)
    i=-1
    j=0
    pivote=n-1
    fase= "particion"
    # TODO: inicializar punteros/estado

def step():
    global items, n, i, j, pivote, fase
    if pivote<=0:
        return {"done": True}
    if fase=="particion":
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
           fase="reset"
           return {"a": i, "b": pivote, "swap": True, "done": False} 
    if fase=="reset":
        i=-1
        pivote=pivote-1
        j=0
        fase="particion"
        return {"a": j, "b":pivote,"swap":False, "done": False}
    return {"done": True}
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    
