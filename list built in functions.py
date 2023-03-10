pc_build = ["cpu","gpu","ram,","power","mobo"]
print(pc_build)
        #len function for printing the no.of elements in a list
print(len(pc_build))

          #convertion of strings to list by splitting the string's value
str1 = "shakthi"
list1 = list(str1)
print(list1)

          #adding a element in the list by using append
pc_build.append("Cabinet")
print(pc_build)

          #suming of elements using  extend
pc_config = ["5600","rtx 3060","ripjaws","lian li 215"]
pc_build.extend(pc_config)
print(pc_build)

        #inserting elements by assigning in index value
pc_build.insert(2,"cabinet")#here to 2 is the index value "Cabinet" is the element value
print(pc_build)

#removing an element using remove
pc_build.remove("cpu")#should mention the element not in index
print(pc_build)

        #removing an element using index not using the value using pop
simple = [1,4,12,4,234,23,466,6,454,]
simple.pop(2)
print(simple)


        #finding the index value using index in a list
print(pc_build.index("cabinet"))

         #counting the repittion of elements in a list using count
list1 = [1,238432,34,45,444,555,444,444,44,]
print(list1.count(444))

            #reversing list
simple.reverse()
print(simple)
#sorting a list
list1.sort()
print(list1)

     



