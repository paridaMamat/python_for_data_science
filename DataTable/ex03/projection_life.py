import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from load_csv import load


# Custom formatting function for the x-axis
def format_income(x, pos):
    """Formats numbers with 'K' for thousands."""
    if x >= 1000:
        return f"{int(x / 1000)}K"
    return f"{int(x)}"


def main():
    """Program that loads the\
        'income_per_person_gdppercapita_ppp_inflation_adjusted.csv'\
            and 'life_expectancy_years.csv' datasets, and displays a\
                plot of life expectancy\
                    vs GDP per capita for the year 1900 for each country.
    """
    try:
        # Load the datasets
        income_dataset =\
            load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_ex_dataset = load("life_expectancy_years.csv")

        # Check if the datasets were loaded correctly
        if income_dataset is None or life_ex_dataset is None:
            raise ValueError("Failed to load one or both datasets.")

        # Filter data for the year 1900
        income_1900 = income_dataset["1900"]
        life_ex_1900 = life_ex_dataset["1900"]

        # Check if both datasets contain the same countries
        com_count =\
            list(set(income_1900.index).intersection(set(life_ex_1900.index)))

        if not com_count:
            raise ValueError("No common countries found between\
                             the two datasets.")

        # Extract the filtered data for plotting
        income_filtered = income_1900[com_count]
        life_filtered = life_ex_1900[com_count]

        # Create a scatter plot with logarithmic x-axis
        plt.xscale('log')  # Use logarithmic scale for x-axis
        plt.scatter(income_filtered, life_filtered, color='blue')

        # Add labels, title, and legend
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")

        ax = plt.gca()
        ax.xaxis.set_major_formatter(FuncFormatter(format_income))

        # Set specific tick locations
        ax.set_xticks([300, 1000, 10000])
        ax.set_xticklabels(['300', '1K', '10K'])

        # Set x-axis limits
        plt.xlim(300, 11000)
        # Ensure tight layout and display
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
