
import pandas as pd
from datetime import timedelta
df = pd.read_csv("C:/Users/rutuj/OneDrive/Documents/GitHub/MapUp-Data-Assessment-F/datasets/dataset-1.csv")
print(df)
#Question 1:Car Matrix Generation
def generate_car_matrix(df):

    car_matrix = df.pivot_table(index='id_1', columns='id_2', values='car')
     # Fill diagonal values with 0
    car_matrix.fillna(0, inplace=True)
    return car_matrix

def main():
   print("car matrix generation")
   car_matrix = generate_car_matrix(df.copy())
   print(car_matrix)
if __name__ == "__main__":
    main()

#Question 2
def get_type_count(df):
    #creating new column car_type
    df["car_type"]  = pd.cut(df["car"], bins = [-1,15,25, float("inf")], labels = ["low", "medium", "high"])
    #Calculate the count of occurrences for each car_type category
    count_cartype = df["car_type"].value_counts().to_dict()
    sort_count_cartype = dict(sorted(count_cartype.items()))
    return sort_count_cartype

def main():
   print("Demonstration of Car Type Count Calculation")
   count_cartype = get_type_count(df.copy())
   print(count_cartype)
if __name__ == "__main__":
    main()

#Question 3
def get_bus_indexes(df):
# calculate mean of bus column
   bus_mean = df["bus"].mean()
# Identify bus values greater than twice the mean
   new_df = df[df["bus"] > 2 * bus_mean]
#sort the indices
   bus_indexes = sorted(new_df.index.to_list())
   return bus_indexes

def main():
   print("Demonstration of Bus Count Index Retrieval")
   bus_indexes = get_bus_indexes(df.copy())
   print(bus_indexes)
if __name__ == "__main__":
    main()

#Question 4
def filter_routes(df):
    # Calculate average truck values per route
  avg_trucks_by_route = df.groupby("route")["truck"].mean()
  # Filter routes with average truck values greater than 7
  filtered_routes = avg_trucks_by_route[avg_trucks_by_route > 7].index.to_list()
  # Sort the filtered routes
  sorted_routes = sorted(filtered_routes)
  return sorted_routes
   
def main():
   print("Route Filtering")
   filtered_routes = filter_routes(df.copy()) 
   print(filtered_routes)
if __name__ == "__main__":
   main()

#Question 5

def multiply_matrix(df):
  
  def multiply_value(val):
    if val > 20:
      return val * 0.75
    return val * 1.25

  car_matrix = generate_car_matrix(df.copy())
  modified_df = car_matrix.map(lambda x: round(multiply_value(x), 1))
  return modified_df
    
def main():
   print("Matrix Value Modification")
   modified_df = multiply_matrix(df.copy())
   print(modified_df)
if __name__ == "__main__":
    main()

#Question 6
dframe = pd.read_csv("C:/Users/rutuj/OneDrive/Documents/GitHub/MapUp-Data-Assessment-F/datasets/dataset-2.csv")
#print(dframe)

def check_timestamp_completeness(dframe):

  def is_timestamp_incorrect(data):

    start_time = pd.to_datetime(data['startTime'], utc=True)
    end_time = pd.to_datetime(data['endTime'], utc=True)

    # Check if timestamps cover 24 hours
    if (end_time - start_time) < timedelta(hours=24):
      return True

    # Check if timestamps span all 7 days
    if (end_time.weekday() - start_time.weekday()) != 6:
      return True

    return False

def main():
 print("Time Check")
 incorrect_timestamps = check_timestamp_completeness(dframe.copy())
 print(incorrect_timestamps)
if __name__ == "__main__":
  main()