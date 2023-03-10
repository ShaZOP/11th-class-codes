elements = input("Enter the elements of the tuple separated by commas: ")
tuple_of_elements = int,elements.split(',')


element_to_search = int(input("Enter the element to search for: "))


found = True
for element in tuple_of_elements:
    if element == element_to_search:
        found = True
        break


if found:
    print("The element exists in the tuple.")
else:
    print("The element does not exist in the tuple.")
