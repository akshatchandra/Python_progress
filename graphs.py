import pandas
import matplotlib
import matplotlib.pyplot as plt

Raw_Housing_Data = pandas.read_csv("1. Regression - Module - (Housing Prices).csv")
print(plt.plot(Raw_Housing_Data['Sale Price']))

plt.plot(Raw_Housing_Data['Sale Price'], color='green')
plt.xlabel("Record Number")
plt.ylabel("Sale Price")
plt.title("First Graph")
plt.show()
