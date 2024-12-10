from load_csv import load
import matplotlib.pyplot as plt


def main(file_path: str, country: str):
    """
    Load the life expectancy dataset and display the life\
        expectancy trend for a specific country.

    Parameters:
        file_path (str): Path to the CSV file.
        country (str): Name of the country to visualize.
    """
    try:
        # Load the dataset
        dataset = load(file_path)
        if dataset is None:
            raise print("Failed to load the dataset.")

        # Check if the country exists in the dataset
        if country not in dataset['country'].values:
            raise print(f"Country '{country}' not found in the dataset.")

        # Filter the data for the specified country
        country_data = dataset[dataset['country'] == country].iloc[0]
        print(country_data)
        # Extract years and life expectancy values
        years = country_data.index[1:].astype(int)
        life_expectancy = country_data.values[1:]

        # Plot the data
        plt.plot(years, life_expectancy, label=country)
        plt.title(f"{country} Life Expectancy Projections")
        plt.xlabel("Year")
        # Customize x-axis ticks to jump every 40 years
        plt.xticks(range(years[0], years[-1] + 1, 40))
        plt.ylabel("Life Expectancy")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")
        return None


# Test the function
if __name__ == "__main__":
    main("life_expectancy_years.csv", "France")
