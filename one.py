import matplotlib.pyplot as plt
#monthly sales data for the year
months=(["Jan","Feb","Mar","Apr","May","June","Aug","Sept","Oct","Nov","Dec"])
sales_data=([25,30,35,40,45,38,50,48,55,60,58])
#create a bar chart
plt.bar(months, sales_data, color='blue ')
plt.xlabel('Months ')
plt.ylabel('Sales Figures')
plt.title('Monthly Sales Data for the Year')
#show the plot
plt.show()

