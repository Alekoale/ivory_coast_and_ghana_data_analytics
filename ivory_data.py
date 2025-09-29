import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from io import StringIO

def load_and_process_data():
  """Loads and processes the population data."""
  csv_data = """Year,Country,Population
1960,Côte d'Ivoire,3508000
1960,Ghana,6728000
1970,Côte d'Ivoire,5411000
1970,Ghana,8678000
1980,Côte d'Ivoire,8066000
1980,Ghana,12081000
1990,Côte d'Ivoire,11962000
1990,Ghana,15117000
2000,Côte d'Ivoire,16387000
2000,Ghana,19278000
2010,Côte d'Ivoire,21095000
2010,Ghana,24957000
2020,Côte d'Ivoire,26378000
2020,Ghana,31073000
2023,Côte d'Ivoire,28891000
2023,Ghana,34122000
"""
  df = pd.read_csv(StringIO(csv_data))
  df_ivory = df[df["Country"] == "Côte d'Ivoire"].copy()
  df_ghana = df[df["Country"] == "Ghana"].copy()
  return df_ivory, df_ghana

def calculate_and_print_stats(country_name, population_data):
  """Calculates and prints basic statistics for population data."""
  print(f"=== {country_name} Stats ===")
  print(f"Mean: {np.mean(population_data):,.0f}")
  print(f"Min: {np.min(population_data):,.0f}")
  print(f"Max: {np.max(population_data):,.0f}")
  print(f"Std Dev: {np.std(population_data):,.0f}\n")

def plot_population_trends(years_ivory, pop_ivory, years_ghana, pop_ghana):
  """Generates and saves a line plot of population trends."""
  plt.figure(figsize=(10,6))
  plt.plot(years_ivory, pop_ivory, marker="o", color="green", label="Côte d'Ivoire")
  plt.plot(years_ghana, pop_ghana, marker="o", color="orange", label="Ghana")
  plt.title("Population Trends: Côte d’Ivoire vs Ghana")
  plt.xlabel("Year")
  plt.ylabel("Population")
  plt.legend()
  plt.grid(True)
  plt.tight_layout()
  plt.savefig("population_trends.png", dpi=150)
  plt.savefig("population_trends.pdf")
  plt.show()

def plot_population_histograms(pop_ivory, pop_ghana):
  """Generates and saves side-by-side histograms of population distribution."""
  fig, axes = plt.subplots(1, 2, figsize=(12,6), sharey=True)

  # Côte d’Ivoire histogram
  axes[0].hist(pop_ivory, bins=8, color="green", alpha=0.7)
  axes[0].set_title("Côte d’Ivoire's Population Distribution")
  axes[0].set_xlabel("Population")
  axes[0].set_ylabel("Frequency (years)")

  # Ghana histogram
  axes[1].hist(pop_ghana, bins=8, color="orange", alpha=0.7)
  axes[1].set_title("Ghana's Population Distribution")
  axes[1].set_xlabel("Population")

  plt.tight_layout()
  plt.savefig("population_histograms.png", dpi=150)
  plt.savefig("population_histograms.pdf")
  plt.show()


def main():
  df_ivory, df_ghana = load_and_process_data()

  # Convert to NumPy arrays
  years_ivory = df_ivory["Year"].to_numpy()
  pop_ivory = df_ivory["Population"].to_numpy()
  years_ghana = df_ghana["Year"].to_numpy()
  pop_ghana = df_ghana["Population"].to_numpy()

  # --- NumPy Stats ---
  calculate_and_print_stats("Côte d'Ivoire", pop_ivory)
  calculate_and_print_stats("Ghana", pop_ghana)

  # --- Plots ---
  plot_population_trends(years_ivory, pop_ivory, years_ghana, pop_ghana)
  plot_population_histograms(pop_ivory, pop_ghana)


if __name__ == "__main__":
  sys.exit(main())