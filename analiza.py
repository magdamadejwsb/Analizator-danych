# Statystyki opisowe
from termcolor import colored


def podstawowe_statystyki(df):
    """
    Oblicza i wyświetla podstawowe statystyki danych pogodowych

    Args: 
        df (pandas.DataFrame | None):
            Dane zawierające temperatury, wilgotność i opady

    Returns:
        None: Funkcja wyświetla wyniki w konsoli        
    """

    if df is None or df.empty:
        print(colored("Najpierw wczytaj dane z pliku CSV", "red"))
        return

    print("\n***** PODSTAWOWE STATYSTYKI *****")

    print(f"Średnia temp maksymalna: {df['temp_max'].mean():.2f} ℃")
    print(f"Średnia temp minimalna: {df['temp_min'].mean():.2f} ℃")
    print(f"Suma opadów: {df['opady'].sum():.2f} mm")

    # print(
    #     colored("Średnia temp maksymalna:", "green"), 
    #     colored(f"{df['temp_max'].mean():.2f} ℃", "red")
    #)

# print(podstawowe_statystyki.__doc__)
# print(help(podstawowe_statystyki))  
