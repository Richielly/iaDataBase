import pandas as pd
import matplotlib.pyplot as plt


def generate_graphs(csv_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Count the venue types
    venue_type_count = df['venue_type'].value_counts()
    venue_type_count.plot(kind='bar', title='Venue Type Counts')
    plt.xlabel('Venue Type')
    plt.ylabel('Count')
    plt.show()

    # Plot whether lunch is available
    lunch_count = df['lunch'].value_counts()
    labels = ['Lunch Available', 'No Lunch Available']
    lunch_count.plot(kind='pie', labels=labels, autopct='%1.1f%%', title='Lunch Availability')
    plt.axis('equal')
    plt.show()

    # Plot whether alcohol is available
    alcohol_count = df['alcohol'].value_counts()
    labels = ['Alcohol Available', 'No Alcohol Available']
    alcohol_count.plot(kind='pie', labels=labels, autopct='%1.1f%%', title='Alcohol Availability')
    plt.axis('equal')
    plt.show()


# Example usage
generate_graphs(r'C:\Users\Equiplano\Downloads\fishfry-locations.csv')