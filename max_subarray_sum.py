# Define a function to find the maximum subarray sum
def maxSubarraySum(arr):
    # Check if the input array is empty, and return 0 if it is
    if len(arr) == 0:
        return 0

    # Initialize variables to keep track of the maximum subarray sum
    max_current = arr[0]
    max_global = arr[0]

    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Calculate the current maximum subarray sum ending at index i
        max_current = max(arr[i], max_current + arr[i])

        # Update the global maximum subarray sum if needed
        max_global = max(max_global, max_current)

    # Return the maximum subarray sum
    return max_global

# Fill an array with user-input integers 
arr = []
size = int(input("Enter the size of the array: "))
for i in range (size):
    n = int(input("Enter an integer: "))
    arr.append(n)

# Display the array
print("The array is:", arr)

# Display the maximum sum of a subarray using the maxSubarraySum function 
print("The maximum sum of a subarray is:", maxSubarraySum(arr))

