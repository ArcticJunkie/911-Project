import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
import numpy as np


df = pd.read_csv('data_file.csv')
print("START OF QUESTION 1")

print("Printing 10 zip codes with highest frequencies.")
print(df['zip'].value_counts().head(10))

print("Check for existence of > 19446 < in ZIP code column")
print("""

""")
m = df['zip'].isin([19446]).any()
print(m)
print("""

""")
print("Check returns true, > 19446 < exists somehwere in ZIP code column")
print("But where? It exists in the following columns")
print("""

""")
print(df.loc[df['zip'] == 19446])
print("""

""")
print("repeating process for > 19090 <")
m = df['zip'].isin([19090]).any()

if m:
    print("Check returns true, > 19090 < exists in ZIP column, location of occurences given below")
    print("""

""")
    print(df.loc[df['zip'] == 19090])
    print("""

""")


else:
    print("Check returns false, >19090< does not exist in ZIP column")

print(" END OF QUESTION 1")
print("START OF QUESTION 2")
print("Top 4 townships for 911 Calls given below along with frequencies")
print("""

""")
print(df['twp'].value_counts().head(4))
print("""

""")
t1 = df['twp'].isin(["LOWER POTTSGROVE"]).any()
t2 = df['twp'].isin(["NORRISTOWN"]).any()
t3 = df['twp'].isin(["HORSHAM"]).any()
t4 = df['twp'].isin(["ABINGTON"]).any()
if not t1:
    print("Lower Pottsgrove is not present")
if not t2:
    print("Norristown is not present")
if not t3:
    print("Horsham is not present")
if not t4:
    print("Abington is not present")

if t1 and t2 and t3 and t4:
    print("All four given townships are, infact, present in the list")

print("END OF QUESTION 2")
print("START OF QUESTION 3")
df[['title', 'reason']] = df['title'].str.split(':', expand=True)
print("Two most common reasons based on reason for a 911 call are given below, along with frequencies")
print("""

""")
print(df['reason'].value_counts().head(100))
print("""

""")
print("Due to ambiguity in question, I have also included two most common titles for a 911, along with frequencies")
print("""

""")
print(df['title'].value_counts().head(2))
print("""

""")
print("END OF QUESTION 3")
print("START OF QUESTION 4")
df['reason'].value_counts().plot.bar()
plt.show()
print("This plot could be changed to a horizontal plot by simply changing the '.bar()' method to a '.barh()' method.")


print("END OF QUESTION 4")
print("START OF QUESTION 5")
# pd.to_datetime(df['timeStamp'])
df['timeStamp'] = pd.to_datetime(df['timeStamp'], format="%Y-%m-%d %H:%M:%S")
print("Converted timeStamp from string format to datetime format")
# print(type(df.iloc[2, 5]))
df['day_of_week'] = df['timeStamp'].dt.day_name()
print("Created day of week column from new timeStamp (datetime) column")
print("Analysing day of week column ")
print(df['day_of_week'].value_counts().head(3))
print("END OF QUESTION 5")
print("START OF QUESTION 6")
sns.countplot(y='day_of_week', hue="title", data=df)
plt.show()
print("traffic calls were lowest on sunday")
print("END OF QUESTION 6")
print("START OF QUESTION 7")
df['month'] = df['timeStamp'].dt.month_name()
sns.countplot(y='month', hue="title", data=df)
plt.show()
print("June had the highest calls for fire")
print("END OF QUESTION 7")
print("START OF QUESTION 8")
# this is super useful for very easily creating a
req_df = df.loc[df['title'] == 'Traffic']
# new filtered dataframe with easily specified crtierion
req_df = req_df.reset_index(drop=True)
req_df = req_df.iloc[0:1000]
longi = list(req_df['lng'])
lati = list(req_df['lat'])


print(req_df)
map = folium.Map(location=[40.102398, -75.291458],
                 zoom_start=6, tiles="openstreetmap")

fg = folium.FeatureGroup(name='Calls')

for lt, ln in zip(lati, longi):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(
        'Traffic Call'), icon=folium.Icon(color="blue")))


map.add_child(fg)
map.save("Map.html")
print("The areas with low density of traffic calls are likely areas where vehicles are not commonly found, such as airports or forests")
print("The map generation raises a memory error on my machine due to the sheer number of entries with traffic calls (in the range of 100,000).")
print("perhaps on a stronger machine it would generate more smoothly.")
print("due to this, instead of a webmap containing all traffic calls, I have created a webmap containing the first 1000 traffic calls")
