# USAGE
# python barcode_scanner.py

from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
from datetime import datetime
import imutils
import time
import cv2
import winsound
frequency = 2500  # Set Frequency To 2500 Hertz
duration = 800  # Set Duration To 1000 ms == 1 second


ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type=str, default="barcodesData.csv",
	help="path to output CSV file ")
args = vars(ap.parse_args())


print("Starting webcam")

vs = VideoStream(src=0).start()
time.sleep(2.0)
csvWrite = open(args["output"], "w")
found = set()
while True:
	frameData = vs.read()
	frameData = imutils.resize(frameData, width=600)
	barcodes = pyzbar.decode(frameData)
	for barcode in barcodes:
		(x, y, width, height) = barcode.rect
		cv2.rectangle(frameData, (x, y), (x + width, y + height), (0, 0, 255), 2)
		barcodeData = barcode.data.decode("utf-8")
		barcodeType = barcode.type
		textData = "{} ({})".format(barcodeData, barcodeType)
		cv2.putText(frameData, textData, (x, y - 10),
			cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
		if barcodeData not in found:
			csvWrite.write("{},{}\n".format(datetime.today().strftime('%Y-%m-%d'),
				barcodeData))
			csvWrite.flush()
			found.add(barcodeData)
			winsound.Beep(frequency, duration)
	cv2.imshow("Barcode Scanner", frameData)
	key = cv2.waitKey(1) & 0xFF
	if key == ord("e"):
		break

# close the output CSV file do a bit of cleanup
print("\nWait while we calculate cost...")
csvWrite.close()
cv2.destroyAllWindows()
vs.stop()




time.sleep(1.0)
import numpy as np
import pandas as pd
from datetime import datetime
import re
import time
data = pd.read_csv('barcodesData.csv', names = ['Date', 'item'])
col1 = data['Date']
col2 = data['item'].values
#print(col2)
regex = re.compile(r'(\d+|\s+)')
total = 0

with open('saleid.txt','r') as f1:
#f1 = open("saleid.txt", "r")

#    if f1.read() == ' ':
#        with open('saleid.txt','w') as fw1:
#            fw1.write(str(1))
            #fw1.close()

    saleid = f1.read()
    saleID = int(saleid)

    print('\n\n Sale ID: ' + str(saleID))
    print('----------------------------------------------------')
    print('\n                      Big Bazar ')
    print('               Sector 2, Rourkela, INDIA\n\n')
    print('----------------------------------------------------')
    print('Date                Item code           Cost (in $)')
    print('----------------------------------------------------')
    for x in col2:

        row = str(col1[1]) + '\t \t' + str(regex.split(x)[0])+ '\t \t' + str(regex.split(x)[1])
        total = total + int(regex.split(x)[1])
        print("\n" + row)

    print('----------------------------------------------------')      
    print('Toatl amount to be paid (in $)         :'+ str(total))
    print('\n')

    # erite result to csv

    f = open('saledata.txt','a')

    regex = re.compile(r'(\d+|\s+)')
    total = 0
    f.write('\n\n Sale ID: ' + str(saleID))
    f.write('\n----------------------------------------------------\n')
    f.write('                   Big Bazar\n ')
    f.write('               Sector 2, Rourkela, INDIA\n')
    f.write('----------------------------------------------------\n')
    f.write('Date                Item code           Cost (in $)\n')
    f.write('----------------------------------------------------\n')
    for x in col2:

        row = str(col1[1]) + '\t \t \t' + str(regex.split(x)[0])+ '\t\t\t\t\t' + str(regex.split(x)[1])
        total = total + int(regex.split(x)[1])
        f.write("\n" + row)

    f.write('\n----------------------------------------------------')   
    f.write('\nToatl amount to be paid                :'+ str(total))
    f.write('\n\n\n')

    #sid = open('saleid.txt','w')

    saleID = saleID +1
    
with open('saleid.txt','w') as fw:
    fw.write(str(saleID))

#fw.close()
#f1.close()

f.close()