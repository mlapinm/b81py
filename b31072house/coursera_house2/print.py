import zipfile

with zipfile.ZipFile('coree.zip', 'w') as myzip:
    myzip.write('manage.py')
    myzip.write('process.py')

print(123)
