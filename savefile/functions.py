from os.path import splitext



import os
def handle_uploaded_file(f,e):
    
    file_name,extension = splitext(f.name)
    
    username=e+extension
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj",e+extension)
    with open(''+username,'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
    