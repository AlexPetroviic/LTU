TASK 1 - Ground Level
----
I used a histogram of Z-values to detect the groundlevel. That was done by finding the index(from Z-axis) of the bin with the highest value.  After that i could either take that index and use it as the ground, but to be sure that i don't include points that is under the ground, i took the midpoint of that bin by taking that ((bin_index[i] + bin_index[i+1]) / 2). By doing it that way, i avoided the including of points that goes under the ground and ensuring that only points above is included. 

Above pcd1 groundlevel : (62411, 3)
Above pcd2 groundlevel : (71858, 3)

g1 = groundlevel1 : 61.24968500000003
g2 = groundlevel2 : 61.26545