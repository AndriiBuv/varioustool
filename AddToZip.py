
import zipfile

exampleZip = zipfile.ZipFile('example.zip', 'w')
exampleZip.write('Program_1.py', compress_type=zipfile.ZIP_DEFLATED)
print (exampleZip.namelist())
exampleZip.close()












