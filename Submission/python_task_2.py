import pandas as pd
import numpy as np
data = pd.read_csv("C:/Users/rutuj/OneDrive/Documents/GitHub/MapUp-Data-Assessment-F/datasets/dataset-3.csv")
print(data)
#Question 1
import pandas as pd
data.info()
def calculate_distance_matrix(data):

  # Extract unique toll locations
  toll_locations = data["id_start"].unique()

  # Create an empty DataFrame to store distances
  distance_matrix = pd.DataFrame(index=toll_locations, columns=toll_locations)

  # Fill the distance matrix with cumulative distances
  for i, row in data.iterrows():
    from_location = row["id_start"]
    to_location = row["id_end"]
    distance = row["distance"]

    # Add the distance to the matrix in both directions to ensure symmetry
    distance_matrix.loc[from_location, to_location] += distance
    distance_matrix.loc[to_location, from_location] += distance

  # Set diagonal values to 0 (distance to self is 0)
  distance_matrix.fillna(0, inplace=True)

  return distance_matrix

# Calculate distance matrix
distance_matrix = calculate_distance_matrix(data)

# Print the distance matrix
print(distance_matrix.to_string())

