# from fuzzywuzzy import fuzz
# import python-Levenshtein
# string1 = 'PnP'
# string2 = 'Plug and Play'
#
# fuzz.token_sort_ratio(string1, string2)

### P - Print the count of maximum consecutive no.??
stringg = list(input("enter the input : "))
#print("Beeetween")
count,max = 0,0
for i in range(0,len(stringg)):
    for j in range(i+1,len(stringg)):
        if stringg[i]==stringg[j]:
            count = 1
            for k in range(j, len(stringg)):
                if stringg[j]==stringg[k]:
                    count+=1
                else:
                    break
                if count>max:
                    max=count
            count = 0

print(max)







