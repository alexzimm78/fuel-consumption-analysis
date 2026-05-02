import csv
import matplotlib.pyplot as plt
def read_data(filename):
    data = []
    try:
        with open(filename, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                km = float(row['km'])
                fuel = float(row['fuel'])
                data.append({'km': km, 'fuel': fuel})
    except FileNotFoundError:
        print("Fehler: Datei nicht gefunden!")
    return data


def calculate_consumption(data):
    consumptions = []
    for trip in data:
        if trip['km'] > 0:
            consumption = (trip['fuel'] / trip['km']) * 100
            consumptions.append(consumption)
    return consumptions


def average_consumption(consumptions):
    if len(consumptions) == 0:
        return 0
    return sum(consumptions) / len(consumptions)

def plot_consumption(consumptions):
    plt.plot(consumptions, marker='o')
    plt.title("Kraftstoffverbrauch pro Fahrt")
    plt.xlabel("Fahrt Nummer")
    plt.ylabel("Verbrauch (l/100km)")
    plt.grid()
    plt.show()

def main():
    filename = "data.csv"


    data = read_data(filename)

    if not data:
        print("Keine Daten vorhanden.")
        return

    consumptions = calculate_consumption(data)
    avg = average_consumption(consumptions)

    print("Verbrauch pro Fahrt (l/100km):")
    for c in consumptions:
        print(f"{c:.2f}")

    print(f"\nDurchschnitt: {avg:.2f} l/100km")
    plot_consumption(consumptions)


if __name__ == "__main__":
    main()
