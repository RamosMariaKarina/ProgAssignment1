import pandas as p

data = {'Box': ['Box 1', 'Box 1', 'Box 1', 'Box 2', 'Box 2', 'Box 2'], 
        'Dimensions': ['Length', 'Width', 'Height', 'Length', 'Width', 'Height'],
        'Value': [6, 4, 2, 5, 3, 4]}
dfData = p.DataFrame (data, columns = ['Box', 'Dimensions', 'Value'])

tidy1 = dfData.pivot_table(index = ['Box'], columns = 'Dimensions', values = 'Value').reset_index()

tidy1 = tidy1.assign(Volume = [48, 60])
print(tidy1)