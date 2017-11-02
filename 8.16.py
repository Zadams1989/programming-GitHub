weight_list=[]

for i in range(4):
    weight=float(input("Enter weight "+str(i+1)+":\n"))
    weight_list.append(weight)
  
print("Weights:",weight_list)


total=0
for val in weight_list:
    total=total+val
  
avg=total/len(weight_list)
print("\nAverage weight: %.2f" % avg)

maximum=0
for val in weight_list:
    if val>maximum:
        maximum=val
print("Max weight: %f\n" % maximum)

index=int(input("Enter a list index (1 - 4):\n"))
print("Weight in pounds:",weight_list[index-1])
kgs=weight_list[index-1] * 0.453592  
print("Weight in kilograms:%f\n" % kgs)

print("Sorted list: ", sorted(weight_list))
