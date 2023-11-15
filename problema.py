def test_analyze_data():

    print('Test 1:')
    data1 = [1, 5, -2, 8, 0, -2, 5, 1, 10, -5]
    analyze_data(data1)

    print('Test 2:')
    data2 = [2.5, 3.5, 1.5, 2.5, 2.5]
    analyze_data(data2)

    print('Test 3:')
    data3 = [1, 3.5, "apple", 2.5, 1, 3, "banana"]
    analyze_data(data3)
    

# Implement the analyze_data function here
def analyze_data(data):
    if not data:
        values = {'Minimum': None, 'Maximum': None, 'Average': None, 'Unique Values Count': 0, 'Median': None}

    # Filter out non-numeric values
    numeric_data = [x for x in data if isinstance(x, (int, float))]
    #print(numeric_data)

    if not numeric_data:
        values = {'Minimum': None, 'Maximum': None, 'Average': None, 'Unique Values Count': 0, 'Median': None}

    # Calculate statistics
    min_value = min(numeric_data)
    max_value = max(numeric_data)
    average_value = sum(numeric_data) / float(len(numeric_data))
    unique_count = len(set(numeric_data))

    # Calculate median
    sorted_data = sorted(numeric_data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]

    values = {'Minimum': min_value, 'Maximum': max_value, 'Average': average_value, 'Unique Values Count': unique_count, 'Median': median}
    print('Minimum:',values['Minimum'])
    print('Maximum:',values['Maximum'])
    print('Average:',values['Average'])
    print('Unique Values Count:',values['Unique Values Count'])
    print('Median:',values['Median'], '\n')
    return values

# Run the test cases
test_analyze_data()

