# This Python code demonstrates Kadane's algorithm to find the subarray within an array
# that has the maximum sum.

# Initializing an empty array to store user input integers
my_array = []

# Asking the user for the size of the array
size = int(input("Enter the size of the array: "))

# Populating the array with user-input integers
for i in range(size):
    n = int(input("Enter an integer: "))
    my_array.append(n)

# Initializing variables to track the maximum sum, current sum, and subarray indices
sum_current = 0           # Keeps track of the current sum of elements
max_sum = 0               # Stores the maximum sum found so far
start_index = 0           # Starting index of the subarray with maximum sum
end_index = 0             # Ending index of the subarray with maximum sum
current_start_index = 0   # Temporary starting index for potential new subarray

# Iterating through the array to find the subarray with the maximum sum (Kadane's algorithm)
for i in range(size):
    sum_current += my_array[i]

    # If the current sum becomes negative, reset it and update the starting index for the next subarray
    if sum_current < 0:
        sum_current = 0
        current_start_index = i + 1

    # If the current sum is greater than the maximum sum, update the maximum sum and indices
    if sum_current > max_sum:
        max_sum = sum_current
        start_index = current_start_index
        end_index = i

# Displaying the original array
print("\nThe array is: ", my_array)

# Extracting and displaying the subarray with the maximum sum and its sum
subarray = my_array[start_index:end_index + 1]
print("\nThe subarray with the maximum sum is:", subarray, "with a sum of", max_sum)
