import pandas as pd

# Wczytanie danych z ankiety
df = pd.read_excel("Podsumowanie_przyszlosc.xlsx")

# Liczba respondentów
liczba_respondentow = len(df)

# Średnia ocena przygotowania do przyszłości
srednia_przygotowania = df["Jak oceniasz swoje przygotowanie do przyszłości? (1–10)"].mean()

# Podział według płci
podzial_plec = df["Płeć"].value_counts()

print("Liczba respondentów:", liczba_respondentow)
print("Średnia ocena przygotowania:", srednia_przygotowania)
print("Podział według płci:")
print(podzial_plec)







