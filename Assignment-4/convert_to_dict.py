keys = ['Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty']
values = [10, 20, 30]

newDict = {key: values[i] if i < len(values) else None for i, key in enumerate(keys)}

print(newDict)
