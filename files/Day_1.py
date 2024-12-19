import re
# Day One Part One


def list_difference(numbers: str) -> int:
    """
    Takes in a file path with two columns, takes the least value pairs of each column, and subtracts them, and returns
    the sum off the difference.
    Args:
        numbers (str): A file path to a file containing two columns of numbers
    Returns:
        int
    Examples:
        >>> list_difference('input.txt')
        2970687
    """
    # Opens the File
    with open(numbers, 'r') as file:
        # Reads the file line by line
        lines = file.readlines()
        cleaned_lines = []
        # Gets rid of whitespace, to get every element as its own into the cleaned_lines list
        for line in lines:
            cleaned_lines += line.strip().split()
        # Creates two lists for column 1 and column 2
        list_1 = []
        list_2 = []
        # Loops through each element, and if that element is divisible by two, then it must be column 1, otherwise it is
        # column 2
        for i in range(len(cleaned_lines)):
            if i % 2:
                list_1.append(cleaned_lines[i])
            else:
                list_2.append(cleaned_lines[i])
        # Sorts the List to get it least to greatest
        list_1.sort()
        list_2.sort()
        combined_list = []
        # Goes through the list and finds the difference between the least value pairs
        for i in range(len(list_1)):
            combined_list += [abs(int(list_1[i]) - int(list_2[i]))]
        return sum(combined_list)
# Day one Part Two
def list_similarity(numbers: str) -> int:
    """
    Takes in a file path with two columns. Then it counts the number of times elements in column 1 appear in column 2 adds it all up
    to get a similarity score, and then returns the similarity score.
    Args:
        numbers (str): A file path to a file containing two columns of numbers
    Returns:
        int: an integer representing the similarity score
    Examples:
        >>> list_similarity('input2.txt')
        5697142
    """
    # Opens the File
    with open(numbers, 'r') as file:
        # Reads the file line by line
        lines = file.readlines()
        cleaned_lines = []
        # Gets rid of whitespace, to get every element as its own into the cleaned_lines list
        for line in lines:
            cleaned_lines += line.strip().split()
        # Creates two lists for column 1 and column 2
        list_1 = []
        list_2 = []
        # Loops through each element, and if that element is divisible by two, then it must be column 1, otherwise it is
        # column 2
        for i in range(len(cleaned_lines)):
            if i % 2:
                list_1.append(cleaned_lines[i])
            else:
                list_2.append(cleaned_lines[i])
        # Have a for loop that loops through list_1
        similarity = 0
        for element in list_1:
            # Count the number times it appears in list_2, multiply it with the original number
            # Add it to a similarity number
            similarity += int(list_2.count(element)) * int(element)
        return similarity
# Day 2 Problem Part 1
def safe_levels(filepath = None , list_1 = None):
    """
    Takes in either a file path or a list, and checks is row in filename, or the single list if list is given is safe.
    It is considered safe if it is increasing or decreasing fully by value in between 1 and 3. Returns the number of safe
    lists.
    Args:
        filepath (str): A file path
        list_1 (list): A single list
    Returns:
        int: the number of safe lists
    Examples:
        >>> safe_levels('mull.txt')
            490
    """
    safe_count = 0
    cleaned_lines = []
    if filepath is not None:
        with open(filepath, 'r') as file:
            # Read the file line by line
            lines = file.readlines()
            cleaned_lines = [line.strip().split() for line in lines]
            # Loop through each element
    elif list_1 is not None:
        cleaned_lines = list
    for element in cleaned_lines:
        # Element is Assumed to be increasing or decreasing
        increasing = True
        decreasing = True
        # Element is assumed to be Safe
        safe = True

        for i in range(len(element) - 1):
            current_number = int(element[i])
            next_number = int(element[i + 1])

            # Check if the sequence is increasing or decreasing
            if current_number >= next_number:
                increasing = False
            if current_number <= next_number:
                decreasing = False

            # Also check if the difference between adjacent numbers is valid
            if not (1 <= abs(next_number - current_number) <= 3):
                safe = False

        # If the sequence is neither increasing nor decreasing, it's unsafe
        if increasing == False and decreasing == False:
            safe = False

        # If the report is safe, increment the count
        if safe:
            safe_count += 1

    return safe_count
# Day 2 Problem Part 2
def safe_levels_2(filename):
    """
    Takes in either a file path  and checks if every row in filename is safe.
    It is considered safe if it is increasing or decreasing fully by value in between 1 and 3. It is also considerd safe
    if removing one element from the list makes it safe. Returns the number of safe lists.
    lists.
    Args:
        filename (str): A file path
    Returns:
        int: the number of safe lists
    Examples:
        >>> safe_levels('mull.txt')
            536
    """
    safe_count = 0

    # Open the file
    with open(filename, 'r') as file:
        # Read the file line by line
        lines = file.readlines()
        cleaned_lines = [line.strip().split() for line in lines]

        # Loop through each element
        for element in cleaned_lines:
            # Assume it is unsafe initially
            safe = False

            # Removing one element at a time and checking if it becomes safe
            for i in range(len(element)):
                modified_sequence = element[:i] + element[i+1:]

                # Check if the modified sequence is safe
                if safe_levels(None, [modified_sequence]) > 0:
                    safe = True

            # If the report is safe, increment the count
            if safe:
                safe_count += 1
    return safe_count
# Day 3 Problem Part 1
def mull(input):
    """
    Takes in a jumbled up string mess, with chars mull(1,2), and multiplies 1 and 2, and adds it with all mull(x,y).
    Returns the total sum
    Args:
        input (str): A file path
    Returns:
        int: the total sum
    Examples:
        >>> mull('mull.txt')
            190604937
    """
    # Opens and Reads the File
    with open(input, 'r') as file:
        content = file.read()
    total_sum = 0
    # Finds all instances of the pattern and stores it as tuple
    all_mull = re.findall("mul\((\d+),(\d+)\)", content)
    total_sum = 0
    # Access the tuples, multiplies the first and second element, and adds it to the total sum
    for element in all_mull:
        total_sum += int(element[0]) * int(element[1])
    return total_sum
