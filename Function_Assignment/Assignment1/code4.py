#WAP for a function that returns the count of the search element in the list
def count(ListData,searchFile):
    count = ListData.count(searchFile)
    return f"{searchFile},found in list {count} time"
listData = [1,2,3,3,4,3]
searchFile = 3
output = count (listData,searchFile)
print(output)