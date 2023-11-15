import datetime


def test_analyze_data():

    print('Test 1')
    data1 = [1, 5, -2, 8, 0, -2, 5, 1, 10, -5]
    print('Input:', data1)
    print('Output:', analyze_data(data1))

    print('Test 2')
    data2 = [2.5, 3.5, 1.5, 2.5, 2.5]
    print('Input:', data2)
    print('Output:', analyze_data(data2))

    print('Test 3')
    data3 = [1, 3.5, "apple", 2.5, 1, 3, "banana"]
    print('Input:', data3)
    print('Output:', analyze_data(data3))

    print('Test 5')
    data4 = [datetime.date(2022, 1, 1), datetime.date(2021, 1, 1), datetime.date(2022, 1, 1)]
    print('Input:', data4)
    print('Output:', analyze_data(data4))

    print('Test 5')
    data5 = []
    print('Input:', data5)
    print('Output:', analyze_data(data5))

    
    

# Implement the analyze_data function here
def analyze_data(data):
    if not data:
        values = (None, None, None, 0, None)

    # Filter out non-numeric values
    numeric_data = [x for x in data if isinstance(x, (int, float))]
    #print(numeric_data)

    if not numeric_data:
        values = (None, None, None, 0, None)
        
    # Calculate statistics
    try:
        min_value = min(numeric_data)
    
    except:
        min_value = None

    try:
        max_value = max(numeric_data)
    except:
        max_value = None
        
    try:
        average_value = sum(numeric_data) / float(len(numeric_data))
    except:
        average_value = None

    try:
        unique_count = len(set(numeric_data))
    except:
        unique_count = 0

    try:
        # Calculate median
        sorted_data = sorted(numeric_data)
        n = len(sorted_data)
        if n % 2 == 0:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        else:
            median = sorted_data[n // 2]
    except:
        median = None

        
    values = (min_value, max_value, average_value, unique_count, median)
        
    return values

# Run the test cases
test_analyze_data()
