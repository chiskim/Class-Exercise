import matplotlib.pyplot as plt

months=(["Jan","Feb","Mar","Apr","May","June","Aug","Sept","Oct","Nov","Dec"])
temperature_data =([10,12,15,20,25,30,32,30,27,22,17,12])

plt.bar(months,temperature_data)
plt.xlabel('months')
plt.ylabel('Temperature (C)')
plt.title("Monthly temperature data for the year")

plt.show()


