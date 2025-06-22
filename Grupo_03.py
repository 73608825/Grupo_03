# Librerias o modulos
import ProgramasPython.Librerias.MostrarDatos as mostrar
import ProgramasPython.Librerias.Validar as validar
import ProgramasPython.Librerias.Operaciones as operaciones
# Contadores y acumuladores
global contador, contA, contB, contC, contD, contE
global acumTotal, acumA, acumB, acumC, acumD, acumE, acumMayorMil
contador = 0
contA = 0
contB = 0
contC = 0
contD = 0
contE = 0
acumTotal = 0
acumA = 0
acumB = 0
acumC = 0
acumD = 0
acumE = 0
acumMayorMil = 0

# Mostrar menu
while True:
    mostrar.menu()

    opcionMenu = int(input("Ingrese opcion de menu:\t\t"))

    match opcionMenu:
        case 1:
            # Ingreso y validación de Monto Base en Dólares
            MontoBaseDolares = []
            while not validar.ValidarMontoBase(MontoBaseDolares):
                MontoBaseDolares = float(input("Monto Base en Dólares invalido. Intente nuevamente:\t\t"))
            
            # Ingreso y validación de Categoría
            Categoria = input("Ingrese la categoría (A o B o C o D o E):\t\t")
            while not validar.ValidarCategoria(Categoria):
                Categoria = input("Categoria inválida. Intente nuevamente (A o B o C o D o E):\t").upper()
            
            # Ingreso y validacion de tipo de cambio a soles
            TipoCambioSoles = float(input("Ingrese el tipo de cambio a soles:\t\t"))
            
            PorcPenalidad = 0
            MensajeRuidoDeci = ""
            contador += 1 
            acumTotal += MontoAPagarSoles
            # Clasificacion por Categoria, ruido en decibeles y porcentaje de penalidad
            if Categoria == 'A':
                contA += 1
                PorcPenalidad = 0.05
                MensajeRuidoDeci = "60 o menos"
            elif Categoria == 'B':
                contB += 1
                PorcPenalidad = 0.07
                MensajeRuidoDeci = "61-100"
            elif Categoria == 'C':
                contC += 1
                PorcPenalidad = 0.09
                MensajeRuidoDeci = "101-149"
            elif Categoria == 'D':
                contD += 1
                PorcPenalidad = 0.12
                MensajeRuidoDeci = "150-200"
            elif Categoria == 'E':
                contE += 1
                PorcPenalidad = 0.15
                MensajeRuidoDeci = "Más de 200"
   
        case 2:
        case 3:
            respuesta = input("Seguro que quiere Salir? (S o s o N o n):\t")
            while not validar.ValidarRpta(respuesta):
                respuesta = input("ERROR. Vuelva a ingresar S o s o N o n:\t").upper()
                    
            if respuesta == "S":
                print("Gracias..Vuelva pronto..!")
                break