# Datos del ejercicio 1
# x <- c(3,4,6,4,2,5)
# y <- c(6,8,9,5,4.5,9.5)

# Datos del ejercicio 2
# x <- c(5,3,7,2,8)
# y <- c(11,6,10,6,12)

# Datos del ejercicio 3
x <- c(20, 25, 35, 40)
y <- c(50, 58, 65, 75, 82)


# f0 - Calcular la media
media <- function(x) {
    return(sum(x) / length(x))
}


# f1 - Diferencia al cuadrado
diferencia_cuadrado <- function(x) {
    la_media <- media(x)
    la_diferencia <- 0

    for (i in x) {
        la_diferencia <- la_diferencia + (i - la_media) * (i - la_media)
    }

    return(la_diferencia)
}


# f2 - Diferencia XY
diferencia_xy <- function(x, y) {
    mediax <- media(x)
    mediay <- media(y)
    sumatoria <- 0

    for (i in seq_along(x)) {
        sumatoria <- sumatoria + (x[i] - mediax) * (y[i] - mediay)
    }

    return(sumatoria)
}


# f3 - Obtener b1
obtener_b1 <- function(x, y) {
    diferencia <- diferencia_xy(x, y)
    diferencia_cuadrados <- diferencia_cuadrado(x)

    return(diferencia / diferencia_cuadrados)
}


# f4 - Obtener b0
obtener_b0 <- function(x, y) {
    mediay <- media(y)
    mediax <- media(x)
    b1 <- obtener_b1(x, y)

    return(mediay - (b1 * mediax))
}


# f5 - Ecuacion de regresion lineal
regresion_lineal <- function(x, y) {
    datos <- data.frame(x = x, y = y)
    modelo <- lm(y ~ x, data = datos)
    return(modelo)
}

x <- c(2,3,4,5,6,7,8,9,10,11)
y <- c(60,65,70,75,80,85,90,95,100,105)

modelo <- regresion_lineal(x, y)
