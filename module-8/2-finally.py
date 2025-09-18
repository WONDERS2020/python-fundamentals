#/usr/bin/python3
""" A module that handle a final statement"""
try:
    with open ("newfile.txt", 'w+r') as f:
        f.write("in the domain of module edge computer security, significant stripes as been made thrugh the integration of artificial intelligence and machine learning")
        print (f.read())
except Exception as e:
    print (e)
finally:
    print ("file close")