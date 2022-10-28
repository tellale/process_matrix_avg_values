def _process_matrix(arr):
    '''Takes an array and returns a new array with the average of the n + neighbours.
    Array content must be int.
    '''
    # Creates new array with the same dimensions of the one given
    res = [ [0] * len(arr[0]) for i in range(len(arr)) ]

    #Process each number in the array to determine the neighbours and sum them
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sums = arr[i][j]
            div = 1

            # Up
            if i - 1 >= 0:
                sums += arr[i-1][j]
                div += 1
            
            # Down
            if i + 1 < len(arr):
                sums += arr[i+1][j]
                div += 1
            
            # Left
            if j - 1 >= 0:
                sums += arr[i][j-1]
                div += 1

            # Right
            if j + 1 < len(arr[0]):
                sums += arr[i][j+1]
                div += 1

            # print(f"{arr[i][j]} - sums: {sums} - div: {div}")  # Use this to make sure you are getting the correct data
            # Obtains the average of each position within the array
            res[i][j] = (sums/div)  # div will always be >= 1

    return res

def is_numerical_matrix(arr):
    ''' Determines if:
    1. If the array contains only lists
    2. The size of the sublist in the array are the same
    3. The content of the sublist are int
    '''

    # Returns True when the array contains only lists
    is_nested_list = all(isinstance(el, list) for el in arr)

    if is_nested_list:

        # Returns True when the sublists have the same size
        sublist_size_is_correct = all(len(arr[0])== len(i) for i in arr)

        # Returns True if all elements in sublists are int
        is_numeric = True
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                if not isinstance(arr[i][j], int):
                    is_numeric = False
                    break

        return sublist_size_is_correct and is_numeric

    return is_nested_list

def process_matrix(arr):
    if arr == []: # Trivial case
        return []
    elif is_numerical_matrix(arr): # when True
        return _process_matrix(arr)
    else:
        # when False
        raise ValueError('Only works on numerical matrices')