"""
Date Splitter Function
"""

import pandas

def date_splitter(df):
      df[:5] 
        # Create features for year, month, day, hour, and minute 
      df['year'] = df['date'].dt.year 
      df['month'] = df['date'].dt.month 
      df['day'] = df['date'].dt.day 
      df['hour'] = df['date'].dt.hour 
      df['minute'] = df['date'].dt.minute
      df_new=pd.DataFrame(df)
      return df_new
