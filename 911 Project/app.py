from datetime import datetime
string = "2015-12-10 17:10:52"
time = datetime.strptime(string, "%Y-%m-%d %H:%M:%S")
print(time)
print(time.hour)
