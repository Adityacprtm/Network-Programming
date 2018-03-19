try:
    # pick an image file you have in the working directory
    # or give the full file path ...
    image_file = "C:/Users/Aditya C. Pratama/Documents/GitHub/Pemrograman-Jaringan-C/4 - data/img.jpg"
    fin = open(image_file, "rb")
    #data = base64.b64encode(fin.read())
    data = fin.read()
    print(data)
    fin.close()
    fh = open("imageToSave.jpg", "wb")
    fh.write(data)
    #fh.write(base64.b64decode(data))
    fh.close()
except IOError:
    print("Image file %s not found" % image_file)
    raise SystemExit
