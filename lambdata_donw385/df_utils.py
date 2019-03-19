"""
Utility Functions for DataFrames
"""
import pandas as pd

DF_Test = pd.DataFrame([1,2,3])

delete_outliers = def delete_outliers(x):
  elements = np.array(x)

  mean = np.mean(elements, axis=0)
  sd = np.std(elements, axis=0)

  final_list = [x for x in arr if (x > mean - 2 * sd)]
  final_list = [x for x in final_list if (x < mean + 2 * sd)]
  print(final_list)


date_splitter = def date_splitter(df):
  df[:5] 
  df['year'] = df['date'].dt.year 
  df['month'] = df['date'].dt.month 
  df['day'] = df['date'].dt.day 
  df['hour'] = df['date'].dt.hour 
  df['minute'] = df['date'].dt.minute
  df_new=pd.DataFrame(df)
  return df_new
