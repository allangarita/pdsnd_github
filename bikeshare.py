# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 19:38:11 2022
3. Additional Changes to Documentation
Punto B. Cambio 02
@author: 43557132
"""

import time
import pandas as pd

"""
CITY_DATA = {'chicago': 'C:/UAIR/2022/Capacitaciones y Certificaciones/Programación para Data Science con Python/all-project-files/chicago.csv',
          'new york city': 'C:/UAIR/2022/Capacitaciones y Certificaciones/Programación para Data Science con Python/all-project-files/new_york_city.csv',
          'washington': 'C:/UAIR/2022/Capacitaciones y Certificaciones/Programación para Data Science con Python/all-project-files/washington.csv'}
"""

CITY_DATA = {'chicago': './chicago.csv',
          'new york city': './new_york_city.csv',
          'washington': './washington.csv'}


def FSolicitarDatos():
    """
    Esta función se encarga de solicitar los datos por la consola del usuario y validar
    si son aptos para el procesamiento
    
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """    
    # Sección de Codigo con los mensajes de bienvenida y explicación para el usuario
    print('---------------------------------------------------------')    
    print('¡Hola! ¡Exploremos un poco la información de US bikeshare!')    
    print('---------------------------------------------------------')    
    print('Digite el nombre de la ciudad que desea consultar')
    print('Opciones: chicago, new york city, washington')
    print('---------------------------------------------------------')    
    #Ejecuta el bucle while hasta que la condición de validación se cumpla
    while True:
        try:
            #Solicita el dato en consola del usuario para la ciudad
            city = str(input('Digite la opción deseada: '))            
            #Elimina espacion en blanco digitados por el usuario al inicio y al final
            city = city.strip()
            #conviente la cadena de caracteres a minuscula
            city = city.lower()
        except ValueError:
            #En caso de Error
            print('---------------------------------------------------------')    
            print('Debes ingresar un nombre de ciudad valido')
            print('Opciones: chicago, new york city, washington')
            print('---------------------------------------------------------')    
            continue
        
        #Valida que la entrada corresponda a alguna de las opciones válidas
        if city not in ('chicago', 'new york city', 'washington'):
            print('---------------------------------------------------------')    
            print('Debes ingresar un nombre de ciudad valido')
            print('Opciones: chicago, new york city, washington')
            print('---------------------------------------------------------')    
        
        else:
            break
        
    print('---------------------------------------------------------')    
    print('Digite el nombre del mes que desea consultar')
    print('Opciones: all, january, february, ... , june')
    print('---------------------------------------------------------')    
    #Ejecuta el bucle while hasta que la condición de validación se cumpla
    print('---------------------------------------------------------')    
    while True:
        try:
            #Solicita el dato en consola del usuario para el mes
            month = str(input('Digite la opción deseada: '))            
            #Elimina espacion en blanco digitados por el usuario al inicio y al final
            month = month.strip()
            #conviente la cadena de caracteres a minuscula
            month = month.lower()
        except ValueError:
            #En caso de Error
            print('---------------------------------------------------------')    
            print('Digite el nombre del mes que desea consultar')
            print('Opciones: all, january, february, ... , june')
            print('---------------------------------------------------------')    
            continue
        
        #Valida que la entrada corresponda a alguna de las opciones válidas
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print('---------------------------------------------------------')    
            print('Digite el nombre del mes que desea consultar')
            print('Opciones: all, january, february, ... , june')
            print('---------------------------------------------------------')    
        
        else:
            break
    print('---------------------------------------------------------')    
    print('Digite el nombre del día que desea consultar')
    print('Opciones: all, monday, tuesday, ... , sunday')
    print('---------------------------------------------------------')    
    #Ejecuta el bucle while hasta que la condición de validación se cumpla
    print('---------------------------------------------------------')    
    while True:
        try:
            #Solicita el dato en consola del usuario para la día
            day = str(input('Digite la opción deseada: '))            
            #Elimina espacion en blanco digitados por el usuario al inicio y al final
            day = day.strip()
            #conviente la cadena de caracteres a minuscula
            day = day.lower()
        except ValueError:
            #En caso de Error
            print('---------------------------------------------------------')    
            print('Digite el nombre del día que desea consultar')
            print('Opciones: all, monday, tuesday, ... , sunday')
            print('---------------------------------------------------------')    
            continue
        
        #Valida que la entrada corresponda a alguna de las opciones válidas
        if day not in ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'saturday', 'sunday'):
            print('---------------------------------------------------------')    
            print('Digite el nombre del día que desea consultar')
            print('Opciones: all, monday, tuesday, ... , sunday')
            print('---------------------------------------------------------')    
        
        else:
            break

    print('-'*40)
    return city, month, day

def FCargarDatos(city, month, day):
    """
    Esta funcion se encarga de recibir los parametros para cargar los datos y filtrar
    segun lo que solicite el usuario
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    #Cargar el DataFrame con los datos indicados del archivo CSV
    df = pd.read_csv(CITY_DATA[city])  
    
    # Conviente la columna en tipo de dato fecha
    df['Start Time'] = pd.to_datetime(df['Start Time'])    
    # crea columna con el numero de mes
    df['month'] = df['Start Time'].dt.month    
    # crea columna con el nombre del día
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filta la información segun lo que solicite el usuario
    if month != 'all':
        # usa los indices del mes para filtrar
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july']
        month = months.index(month) + 1

        # filtra por numero de mes
        df = df[df['month'] == month]

    # filtra por día de la semana
    if day != 'all':        
        df = df[df['day_of_week'] == day.title()]
        
    return df 

def FTimeStats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    #convertir la columna del DF a tipo de dato datetime
    VTMesModa = df['month'].mode()[0]
    print('El mes en el cual hubo mayor demanda de uso fue: ', VTMesModa)
    
    # display the most common day of week
    VTDiaModa = df['day_of_week'].mode()[0]
    print('El día en el cual hubo mayor demanda de uso fue: ', VTDiaModa)

    # display the most common start hour
    df['star_hour'] = df['Start Time'].dt.hour
    VTHoraModa = df['star_hour'].mode()[0]
    print('La hora en el cual hubo mayor demanda de uso fue: ', VTHoraModa)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    return df

def FStationStats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    VTSTModa = df['Start Station'].mode()[0]
    print('La estación de inicio más usada por los clientes fue: ', VTSTModa)
    
    # display most commonly used end station
    VTETModa = df['End Station'].mode()[0]
    print('La estación de entrega más usada por los clientes fue: ', VTETModa)


    # display most frequent combination of start station and end station trip
    df['str_end_sta'] = 'Salida: ' + df['Start Station'] + ' - Entrega: ' + df['End Station']
    VTStEnSModa = df['str_end_sta'].mode()[0]
    print('La combinación de estación de salidad y entrega más usada por los clientes fue: \n', VTStEnSModa)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def PTripDurationStats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    VTTotalTrvTime = df['Trip Duration'].sum()
    print('El total de tiempo de viajes fue: ', VTTotalTrvTime)
    # display mean travel time
    VTMean = df['Trip Duration'].mean()
    print('La media del tiempo de viajes fue: ', VTMean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def FUserStats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    VTTipoUsuario = df['User Type'].value_counts()
    print('Los tipos de usuarios y cantidad son: \n', VTTipoUsuario)

    # Display counts of gender
    VTGenero = df['Gender'].value_counts()
    print('La cantidad entre hombre y mujeres que usaron el servicio fue: \n', VTGenero)

    # Display earliest, most recent, and most common year of birth
    VTCumpAnt = df['Birth Year'].max()
    VTCumpRec = df['Birth Year'].min()
    VTCumpMod = df['Birth Year'].mode()[0]
    print('El año de cumpleaños mas antiguo es: ', VTCumpAnt)
    print('El año de cumpleaños mas reciente es: ', VTCumpRec)
    print('El año de cumpleaños mas común es: ', VTCumpMod)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

        
def FDatosSinProcesar(df):
    VTVerDatos = input('\n¿Le gustaría ver 5 filas de datos de viajes individuales? Ingrese sí o no\n')
    VTIniLoc = 5
    while VTVerDatos.lower() not in ('n', 'no'):
      print(df.iloc[VTIniLoc-5:VTIniLoc])
      VTIniLoc += 5
      VTVerDatos = input("Desea continuar?: ").lower()

def FMensajes():
    print('Gracias por usar nuestros sistemas')
    print('Adios!!!')

def main():
    while True:
        city, month, day = FSolicitarDatos()
        df = FCargarDatos(city, month, day)  
        FTimeStats(df)
        FStationStats(df)
        PTripDurationStats(df)
        if city != 'washington':            
            FUserStats(df)
                
        FDatosSinProcesar(df)
        FMensajes()
        restart = input('\nTe gustaria volver a revisar la información? Digite (s)si o (n)no.\n')
        if restart.lower() not in ('s', 'sí', 'si'):
            break

if __name__ == "__main__":
	main()    

