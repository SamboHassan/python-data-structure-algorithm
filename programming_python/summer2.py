def summer(numCols, fileName):
 sums = [0] * numCols
 for line in open(fileName): # use file iterators
 cols = line.split(',') # assume comma-delimited
 nums = [int(x) for x in cols] # use limited converter
 both = zip(sums, nums) # avoid nested for loop
 sums = [x + y for (x, y) in both] # 3.X: zip is an iterable
 return sums


C:\...\PP4E\Lang> type table3.txt
1,5,10,2,1
2,10,20,4,2
3,15,30,8,3
4,20,40,16,4
C:\...\PP4E\Lang> python summer2.py 5 table3.txt
[10, 50, 100, 30, 10]
