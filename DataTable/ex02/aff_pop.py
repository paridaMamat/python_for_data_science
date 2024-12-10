from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd
import sys


def process_population(population_series):
    """
    Converts a population series with units (K, M, B)\
        into a standard format (in millions).
    """
    def parse_value(value):
        if isinstance(value, str):
            if value.endswith('K'):
                return float(value[:-1]) * 0.001
            elif value.endswith('M'):
                return float(value[:-1])
            elif value.endswith('B'):
                return float(value[:-1]) * 1000
        return None

    return population_series.apply(parse_value)


def million_formatter(x, pos):
    """
    Formatter for the y-axis to display population\
        values in the format '20M', '40M', etc.
    """
    return f"{int(x)}M" if x != 0 else ""


def extract_data(dataset, cap_country, cmp_country):
    """
    display and extract data of campus country and\
        compare country before 2050
    return campus country's data , compare country's\
        data and column of
    years before 2050
    """

    # Filter data for the two countries
    filtered_data =\
        dataset[dataset["country"].isin([cap_country, cmp_country])]
    print(filtered_data)

    # Filter data for France and the chosen country
    campus_data = dataset[dataset["country"] == cap_country].iloc[0]
    cmp_country_data = dataset[dataset["country"] == cmp_country].iloc[0]

    # Extract years and data
    years = campus_data.index[1:].astype(int)
    cap_population = process_population(pd.Series(campus_data[1:]))
    cmp_population = process_population(pd.Series(cmp_country_data[1:]))

    # Filter data to limit to years <= 2050
    filter_years = years <= 2050
    years = years[filter_years]
    cap_population = cap_population[filter_years]
    cmp_population = cmp_population[filter_years]
    return cap_population, cmp_population, years


def main():
    """
    Program that loads the population_total.csv dataset\
        and displays the population data for campus country(France)\
            versus a country provided as a command-line argument.\
                The years displayed are from 1800 to 2050.
    """
    try:
        # Check if exactly one argument is provided
        if len(sys.argv) != 2:
            raise AssertionError("Choose exactly one country as\
                                 an argument.")

        # Load the dataset
        dataset = load("population_total.csv")
        if dataset is None:
            raise ValueError("Failed to load dataset.")

        # Extract countries
        cap_country = "France"
        cmp_country = sys.argv[1]
        if cmp_country not in dataset["country"].values:
            raise ValueError(f"Country '{cmp_country}'\
                             not found in the dataset.")

        cap_population, cmp_population, years =\
            extract_data(dataset, cap_country, cmp_country)

        # Plotting
        plt.plot(years, cap_population, 'g', label=cap_country)
        plt.plot(years, cmp_population, 'b', label=cmp_country)
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(range(years.min(), 2051, 40))

        # Determine y-tick increment dynamically based on population range
        max_population = max(max(cap_population), max(cmp_population))
        if max_population <= 100:
            y_ticks = range(0, int(max_population), 20)
            plt.yticks(y_ticks)
        # Apply custom y-axis formatter
        plt.gca().yaxis.set_major_formatter(FuncFormatter(million_formatter))
        plt.ylabel("Population")
        plt.legend()
        plt.tight_layout()
        plt.show()

    except AssertionError as e:
        print(f"Error: {e}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
