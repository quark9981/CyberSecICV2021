import exifread,hashlib,os,sys
# Open image file for reading (must be in binary mode)
def sumPngmd5(dirPath):
    print("USE PATH:"+dirPath)
    intXorAll=""
    for num in range(1,251):
        jpgPath = dirPath + "flag" + str(num) + ".jpg"          
        with open(jpgPath, "rb") as pngFile:
            tags = exifread.process_file(pngFile)
            for tag in tags.keys():
                if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
                    if tag == "GPS GPSLatitude":     
                        intXor_1 = int(str(tags[tag])[1:4])
                    if tag == "GPS GPSLongitude":
                        intXor_2 = int(str(tags[tag])[1:4])
            intXor=intXor_1^intXor_2
            strToXor = hashlib.md5(str(intXor).encode('utf8')).hexdigest()
        intXorAll = intXorAll+strToXor
    strToXor = hashlib.md5(str(intXorAll).encode('utf8')).hexdigest()
    return strToXor
    
if __name__ == "__main__":
    if len(sys.argv)<2:
        print("use:python getFlag.py yourPngPath")
        sys.exit(0)
    flagText = sumPngmd5(sys.argv[1])
    print("getFlag:")
    print("flag{"+flagText+"}")