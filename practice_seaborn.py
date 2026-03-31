import matplotlib.pyplot as plt
import seaborn as sns

"""name=["vishak","vidya","lalitha","vincent"]
age =[21,27,45,50]

sns.scatterplot(x=name,y=age,marker="o",hue=age,palette="rainbow",edgecolor="black")
plt.grid(True)
plt.figure(figsize=(6,7))
plt.show()"""


#Strip plot

"""Months = ["Jan","Feb","Mar","Apr","May","Jun","jul","Aug","Sept","Oct","Nov","Dec"]
years = [2000,2005,2010,2015,2020,2025,2030,2035,2040,2045,2045,2050]
sns.stripplot(x=Months,y=years,hue=years,palette="coolwarm",linestyle=":",marker="o")
plt.grid(True)
plt.ylim(1999,2060)
plt.xticks(rotation=30)
plt.show()"""

#Heatmap
"""import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = {
    "Month": ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"],
    "Temperature": [24, 26, 28, 30, 32, 31, 29, 29, 28, 27, 25, 24],
    "Humidity": [70, 65, 60, 55, 50, 60, 75, 80, 78, 72, 68, 70],
    "Rainfall": [20, 10, 15, 25, 40, 120, 200, 180, 150, 90, 50, 30]
}
df=pd.DataFrame(data)
df.set_index("Month",inplace=True)
sns.heatmap(df,cmap="rainbow",annot=True)
plt.show()"""


#Load_Dataset

"""flight = sns.load_dataset("flights")
pivot = flight.pivot(index="month",columns="year",values="passengers")
sns.heatmap(pivot,annot=True)
plt.show()"""


#Displot
import pandas as pd
"""Company = ["Google", "Microsoft", "Amazon","Infosys","TCS","Wipro","HCLTech"]
product_companies = ["swiggy","zomato","zoho","blinkit","paytm","flipkart","Amazon"]
df=pd.DataFrame({"service":Company,"product":product_companies})
sns.scatterplot(data=df,x="service",y="product")
sns.countplot(data=df,x="service")
plt.show()"""

"""Marks = [45, 50, 55, 60, 65, 70, 75, 80]
df = pd.DataFrame({"Score":Marks})
sns.displot(data=df,x="Score",kde=True,color="red")
plt.show()"""
















