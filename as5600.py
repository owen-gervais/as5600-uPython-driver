from micropython import const
from machine import I2C
import ustruct


class AS5600:
    
    def __init__(self, i2c):
        
        # ---- Device Address -----
        self.ADDR = const(0x36)

        # ---- Status Registers ----
        self.STATUS = const(0x0B) # MD Bit 5, ML Bit 4, MH Bit 3, R
        self.AGC    = const(0x1A) # Bits 0-7, R
        self.ANGLE1 = const(0x0E) # Bits 0-3, R (Bits 8-11)
        self.ANGLE2 = const(0x0F) # Bits 0-7, R
        
        # ---- I2C Bus ----
        self.i2c = i2c
        
    def isMagnetDetected(self):
        # Read both angle registers
        statusData = self.i2c.readfrom_mem(self.ADDR, self.STATUS, 1)
        
        print(statusData)
        # Unpack the data
        statusData = ustruct.unpack_from("<B", statusData, 0)[0]
        
        print(statusData)
        
        return (statusData & 0x10) >> 5
        
        
    def readAngle(self):
        
        # Read both angle registers
        angleData1 = self.i2c.readfrom_mem(self.ADDR, self.ANGLE1, 1)
        angleData2 = self.i2c.readfrom_mem(self.ADDR, self.ANGLE2, 1)
        
        # Unpack the data
        angleData1 = ustruct.unpack_from("<B", angleData1, 0)[0]
        angleData2 = ustruct.unpack_from("<B", angleData2, 0)[0]
        
        '''
        1. (Read the smalled register and mask out all non data bits) 010101010 & 00001111 -> 000010101
        2. 0000101000000000 | 10001001 -> 0000101010001001 (raw angle in counts)
        '''
        return (((angleData1 & 0x0F) << 8) | angleData2) * (360/4096)
        
