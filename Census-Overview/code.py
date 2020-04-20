# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path , delimiter = "," , skip_header=1)
census = np.concatenate((new_record,data),axis = 0)
print(census)


# --------------
#Code starts here
age = census[ : ,0]
max_age = np.max(age)
min_age = np.min(age)

age_mean = np.mean(age)

age_std = np.std(age)



# --------------
#Code starts here
race_0 = census[census[ : ,2]==0]
race_1 = census[census[ : ,2]==1]
race_2 = census[census[ : ,2]==2]
race_3 = census[census[ : ,2]==3]
race_4 = census[census[ : ,2]==4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

print('Race_0: ', len_0)
print('Race_1: ', len_1)
print('Race_2: ', len_2)
print('Race_3: ', len_3)
print('Race_4: ', len_4)

#Storing the different race lengths with appropriate indexes
race_list=[len_0, len_1,len_2, len_3, len_4]

#Storing the race with minimum length into a variable 
minority_race=race_list.index(min(race_list))

#Code ends here




# --------------
#Code starts here
senior_citizens = census[census[ : , 0] > 60]
working_hours = census[ : , 6]
working_hours_sum = working_hours_sum=senior_citizens.sum(axis=0)[6]
senior_citizens_len = len(senior_citizens)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[ : , 1] > 10]
low = census[census[ : , 1] <= 10]

high_income = high[ : , 7]
avg_pay_high = high_income.mean()

low_income = low[ : , 7]
avg_pay_low = low_income.mean()

print(avg_pay_high == avg_pay_low)



