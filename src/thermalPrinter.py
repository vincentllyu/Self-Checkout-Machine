import os
#from escpos.printer import Serial
def testESCPOS(items):
    os.system("sudo chmod 666 /dev/usb/lp0")
    p = Serial(devfile = '/dev/usb/lp0',
               baudrate = 9600,
               bytesize = 8,
               parity = 'N',
               stopbits = 1,
               timeout = 1.00,
               dsrdtr = True)
    p.qr("Vincent is not here, can I take a message?")
    
def printReceipt(items,total_price):
    items.pop(0)
    items.pop(0)
    items.pop(0)
    items.pop(0)
    items.pop(0)

    os.system("sudo chmod 666 /dev/usb/lp0")
    
    line = 'sudo echo \"{:^30}\\\\n\" > /dev/usb/lp0'.format('Welcome To Vincent\'s Shop')
    os.system(line)
    print(line)
    
    line = 'echo \"{:-<30}\\\\n\" > /dev/usb/lp0'.format('')
    os.system(line)
    print(line)

    line = 'echo \"{:<20}{:>10}\\\\n\" > /dev/usb/lp0'.format('Item','|    price  ')
    os.system(line)
    print(line)    
    
    for item in items:
        line = 'echo \"{:<20}{:>10.2f}\\\\n\" > /dev/usb/lp0'.format(item[0],item[1])
        os.system(line)
        print(line)

    line = 'echo \"{:-<30}\\\\n\" > /dev/usb/lp0'.format('')
    os.system(line)
    print(line)

    line = 'echo \"{:<20}{:>10.2f}\\\\n\" > /dev/usb/lp0'.format('Total',total_price)
    os.system(line)
    print(line)

    line = 'echo \"{:^30}\\\\n\\\\n\\\\n\\\\n\" > /dev/usb/lp0'.format('See you soon!')
    os.system(line)
    print(line)
    
if __name__ == "__main__":
    printList =[['',''],['',''],['',''],['',''],['',''],['Phone',20],['Brush',10],['Phon1',20],['Brus1',10],['Phon2',20]]
    printReceipt(printList,200.0)
    #testESCPOS(printList)
