import numpy
import matplotlib.pyplot as plt
import scipy
#Simple plot:
my_array =  numpy.array([1,10,5,4,19,0,2,8])
plt.plot(my_array)
plt.show()

#Simple pie chart:

categories = 'Cars', 'Trucks' , 'SUVs' , 'Motorcycles' , "Minivans"
quantities = [250,150,175,70,90]
fig,axl = plt.subplots()
axl.pie(quantities,labels= categories, autopct='%1.1f%%',
        shadow=True, startangle=90)

axl.axis('equal')
plt.show()

#Scipy:
my_data = scipy.stats.norm.rvs(size = 500)
plt.hist(my_data,bins=50)
plt.show()