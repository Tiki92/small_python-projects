
# This file should be in the same directory as 'slcsp.csv', 'plans.csv' and 'zips.csv'
import csv
from collections import Counter


print("Started")

silver_plans = {}

rate_areas = []
  
zip_codes = []

zipcodesV = {}


# Storing the zipcodes we need to find the slcsp for in zip_codes
with open('slcsp.csv') as result:
    zips = csv.DictReader(result)
    for i in zips:
        zip_codes.append(int(i['zipcode']))
    

# Storing all the unique rate areas in rate_areas
def get_rate_areas():
        with open('plans.csv') as plans:
            health_plans = csv.DictReader(plans)
            for row in health_plans:
                if int(row['rate_area']) not in rate_areas:
                    rate_areas.append(int(row['rate_area']))

# Sorting silver plans by rate area and state in silver_plans                  
def get_silver_plans():
            for i in rate_areas:
                    with open('plans.csv') as plans:
                        health_plans = csv.DictReader(plans)
                        silver_plans[i] = {}
                        rates = []

                        for row in health_plans:
                            metal_level = row['metal_level']
                            rate_area = row['rate_area']
                            state = row['state']
                    
                            if metal_level == 'Silver' and rate_area == str(i) and state in silver_plans[i]:
                                silver_plans[i][state].append(float(row['rate']))
                            elif metal_level == 'Silver' and rate_area == str(i) and state not in silver_plans[i]:
                                silver_plans[i][state] = []
                                silver_plans[i][state].append(float(row['rate']))

# Storing all the zipcodes occurrences in silver_plans                           
def get_zipcodes_sp():
    for sol in zip_codes:
        with open('zips.csv') as result:
            zips = csv.DictReader(result)
            vers = []
            zipcodesV[sol] = []

            for row in zips:
                zipcode = int(row['zipcode'])
                rate_area = int(row['rate_area'])
                state = row['state']

                if sol == zipcode and rate_area in silver_plans and state in silver_plans[rate_area] and sol in zipcodesV:
                    vers.append(silver_plans[rate_area][state])
                                       
        zipcodesV[sol] = vers

# Storing the zipcodes and the slcsp foe the specific zipcode       
def restructure():
    for i in zipcodesV:
        if len(zipcodesV[i]) == 0:
            pass
        elif len(zipcodesV[i]) == 1:
            zipcodesV[i] = zipcodesV[i][0]
        elif Counter(zipcodesV[i][0]) == Counter(zipcodesV[i][1]):
            zipcodesV[i] = zipcodesV[i][0]
        else:
            zipcodesV[i] = []
# Finding the second smallest rate
def second_smallest(numbers):
  if (len(numbers)<2):
    return
  if ((len(numbers)==2)  and (numbers[0] == numbers[1]) ):
    return
  dup_items = set()
  uniq_items = []
  for x in numbers:
    if x not in dup_items:
      uniq_items.append(x)
      dup_items.add(x)
  uniq_items.sort()    
  return  uniq_items[1] 

# Associating zipcodes with second smallest rate   
def zip_sp():
    for i in zipcodesV:
        zipcodesV[i] = second_smallest(zipcodesV[i])

    
get_rate_areas()
get_silver_plans()
get_zipcodes_sp()
restructure()
zip_sp()

# Writing the results in a csv file
with open('results.csv','w') as f:
    w = csv.writer(f)
    w.writerow(['zipcode', 'rate'])
    w.writerows(zipcodesV.items())

print("File results.csv was created")


    
        
                
                        




              

