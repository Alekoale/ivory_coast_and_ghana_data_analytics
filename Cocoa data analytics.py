import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_scatter(country_df, country_name, color="blue"):
    """Creates and displays a scatter plot for a country's yield over the years."""
    fig, ax = plt.subplots(figsize=(12,6))
    ax.scatter(country_df["Year"], country_df["Yield"], color=color)
    ax.set_title(f"Year vs Yield - {country_name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Yield")
    ax.set_xticks(country_df["Year"])
    ax.set_xticklabels(country_df["Year"], rotation=90)
    ax.grid(True)
    plt.show()

def plot_bar(country_df, country_name, color="blue"):
    """Creates and displays a bar chart for a country's harvested area over the years."""
    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(country_df["Year"], country_df["Area harvested"], color=color)
    ax.set_title(f"Area harvested by Year - {country_name}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Area harvested")
    ax.set_xticks(country_df["Year"])
    ax.set_xticklabels(country_df["Year"], rotation=90)
    ax.grid(axis="y")
    plt.show()

def main():
    """
    Loads cocoa production data, organizes it by country,
    generates and saves plots, and displays tables.
    """
    # Load the cocoa production dataset from a CSV file.
    # Make sure the file "Cocoa production.csv" is uploaded to your Colab environment.
    try:
        df = pd.read_csv("Cocoa production.csv")
        # Convert the 'Year' column to string type to ensure correct plotting on the x-axis.
        df["Year"] = df["Year"].astype(str)

        # Organize the data into two tables, one for Côte d'Ivoire and one for Ghana.
        # We drop the 'Area' column as it's no longer needed in the country-specific tables.
        df_ivory = df[df["Area"]=="Côte d'Ivoire"].drop(columns=["Area"])
        df_ghana = df[df["Area"]=="Ghana"].drop(columns=["Area"])

        # Create a figure with a 2x2 grid of subplots to display multiple plots in one figure.
        fig, ax = plt.subplots(2,2, figsize=(13,6))
        # Flatten the axes array if it's a 2D array for easier indexing.
        if isinstance(ax, plt.Axes):
            ax = [ax]
        else:
            ax = ax.flatten()

        # Panel 1: Scatter plot for Ghana's Year vs Yield.
        ax[0].scatter(df_ghana["Year"], df_ghana["Yield"], color="orange")
        ax[0].set_title("Ghana - Year vs Yield ")
        ax[0].set_xlabel("Year")
        ax[0].set_ylabel("Yield")
        ax[0].grid(True)
        ax[0].tick_params(axis='x', rotation=90)

        # Panel 2: Scatter plot for Ivory Coast's Year vs Yield.
        ax[1].scatter(df_ivory["Year"], df_ivory["Yield"], color="green")
        ax[1].set_title("Côte d'Ivoire - Year vs Yield ")
        ax[1].set_xlabel("Year")
        ax[1].set_ylabel("Yield")
        ax[1].grid(True)
        ax[1].tick_params(axis='x', rotation=90)

        # Panel 3: Bar chart for Ghana's Area harvested by Year.
        ax[2].bar(df_ghana["Year"], df_ghana["Area harvested"], color="orange")
        ax[2].set_title("Ghana - Area harvested by Year")
        ax[2].set_xlabel("Year")
        ax[2].set_ylabel("Area harvested")
        ax[2].grid(axis="y")
        ax[2].tick_params(axis='x', rotation=90)

        # Panel 4: Bar chart for Ivory Coast's Area harvested by Year.
        ax[3].bar(df_ivory["Year"], df_ivory["Area harvested"], color="green")
        ax[3].set_title("Côte d'Ivoire - Area harvested by Year")
        ax[3].set_xlabel("Year")
        ax[3].set_ylabel("Area harvested")
        ax[3].grid(axis="y")
        ax[3].tick_params(axis='x', rotation=90)

        # Set the main title for the entire figure.
        fig.suptitle("Cocoa Production Analysis", fontsize=16)
        # Adjust layout to prevent titles/labels from overlapping and make space for the main title.
        plt.tight_layout(rect=[0, 0, 1, 0.96])

        # Save the figure as a PDF file.
        fig.savefig("Cocoa_analysis.pdf")
        # Display the combined plot.
        plt.show()


        # Print the organized tables for Côte d'Ivoire and Ghana.
        print("Côte d'Ivoire table.")
        #display(df_ivory)
        print("Ghana table.")
       # display(df_ghana)

        # Display individual scatter and bar plots for both countries using the defined functions.
        plot_scatter(df_ivory, "Côte d'Ivoire", color="green")
        plot_scatter(df_ghana, "Ghana", color="orange")
        plot_bar(df_ivory, "Côte d'Ivoire", color="green")
        plot_bar(df_ghana, "Ghana", color="orange")

    except FileNotFoundError:
        print("Error: 'Cocoa production.csv' not found. Please upload the file to your Colab environment.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    sys.exit(main())