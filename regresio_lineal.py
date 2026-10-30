#x = [20, 25, 30, 35, 40]
#y = [50, 58, 65, 75, 82]

x= [20, 25, 30, 35, 40]
y= [50, 58, 65, 75, 82]

#x = [2,3,4,5,6,7,8,9,10,11]
#y = [60,65,70,75,80,85,90,95,100,105]
#f0

def media(x):
    return sum(x) / len(x)
#f1
def diferencia_cuadrado(x):
    la_media = media(x)
    la_diferencia = 0
    for i in x:
        la_diferencia = la_diferencia + (i - la_media) * (i - la_media)
    return la_diferencia

#f2
def diferencia_xy(x, y):
    mediax = media(x)
    mediay = media(y)
    lista_xy = [(a - mediax) * (b - mediay) for a, b in zip(x, y)]
    sumatoria = sum(lista_xy)
    return sumatoria
    
    

def obtener_b1(x,y):
    diferencia = diferencia_xy(x,y)
    diferencia_cuadrados = diferencia_cuadrado(x)
    return diferencia / diferencia_cuadrados

def obtener_b0(x, y):
    mediay = media(y)
    mediax = media(x)
    b1 = obtener_b1(x,y)
    return mediay  - (b1 * mediax)

def predecir(x, y):
    b0 = obtener_b0(x, y)
    b1 = obtener_b1(x, y)
    return b0 + b1 * 32

