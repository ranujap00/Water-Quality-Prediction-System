def outliers(values,ranges):
    outlier = []
     
    numeric_values = [value for value in values if isinstance(value, (int, float))]

    filtered_ranges = [range_val for range_val in ranges if range_val is not None]

    col_names = ['pH', 'iron', 'nitrate', 'chloride', 'turbidity', 'fluoride', 'copper', 'odor', 'sulfate', 'conductivity', 'chlorine', 'manganese', 'totalDissolvedSolids', 'waterTemp', 'airTemp', 'day']

    for (value, (min,max),column) in zip(numeric_values, filtered_ranges,col_names):
        if value < min or value > max:
            d = dict()
            d['column'] = column
            d['min'] = min
            d['max'] = max
            outlier.append(d)

    return outlier
