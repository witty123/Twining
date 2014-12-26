from prettytable import PrettyTable
import matplotlib.pyplot as plt
from visualise import data_frames
import visualise

pt = PrettyTable()
pt = PrettyTable(['Brand \ Product', 'First tweet timestamp (UTC)', 'Last tweet timestamp (UTC)'])

#for key in sorted(data_frames.keys()):
#    pt.add_row([key, data_frames[key]['created_at'][0], data_frames[key]['created_at'][-1]])
    
#print pt




brands = ['sony', 'microsoft']
products = ['iphone6', 'galaxys5']
 
brands_grouped_time = [data_frames[key].groupby(lambda x: x.hour) for key in brands]
products_grouped_time = {key:data_frames[key].groupby(lambda x: x.hour) for key in products}
 

def group_by_15_min_intervals(x):
    if 0 <= x.minute <= 15: return (x.hour, "0-15")
    elif 15 < x.minute <= 30: return (x.hour, "16-30")
    elif 30 < x.minute <= 45: return (x.hour, "31-45")
    else: return (x.hour, "46-00")
    brands_grouped_time = {key:data_frames[key].groupby(lambda x: group_by_15_min_intervals(x)) for key in brands}
    products_grouped_time = {key:data_frames[key].groupby(lambda x: group_by_15_min_intervals(x)) for key in products}
     
# Plot for brands
plt.ylabel("Tweet Volume")
plt.xlabel("Time")
plt.title("Brands Social Trend")
plt.plot([float(str(hour[0])+'.'+hour[1].split('-')[0]) for hour, group in brands_grouped_time['sony']][1:-1], [len(group)for hour, group in brands_grouped_time['sony']][1:-1],'r', label='Sony')
plt.plot([float(str(hour[0])+'.'+hour[1].split('-')[0]) for hour, group in brands_grouped_time['microsoft']][1:-1], [len(group)for hour, group in brands_grouped_time['microsoft']][1:-1],'b', label='Microsoft')
plt.legend()
 
# Plot for products
plt.ylabel("Tweet Volume")
plt.xlabel("Time")
plt.title("Products Social Trend")
plt.plot([float(str(hour[0])+'.'+hour[1].split('-')[0]) for hour, group in products_grouped_time['iphone6']][1:-1], [len(group)for hour, group in products_grouped_time['iphone6']][1:-1],'r', label='iPhone 6')
plt.plot([float(str(hour[0])+'.'+hour[1].split('-')[0]) for hour, group in products_grouped_time['galaxys5']][1:-1], [len(group)for hour, group in products_grouped_time['galaxys5']][1:-1],'b', label='Galaxy S5')
plt.legend() 
