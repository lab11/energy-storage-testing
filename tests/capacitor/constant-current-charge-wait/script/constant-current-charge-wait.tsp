--Initialize SMU

reset()
errorqueue.clear()
status.reset()

smua.nvbuffer1.clear()
smua.nvbuffer1.appendmode = 1
smua.nvbuffer1.collecttimestamps = 1
smua.nvbuffer1.collectsourcevalues = 0

smua.nvbuffer2.clear()
smua.nvbuffer2.appendmode = 1
smua.nvbuffer2.collecttimestamps = 1
smua.nvbuffer2.collectsourcevalues = 0

smua.source.func = smua.OUTPUT_DCVOLTS
smua.source.levelv = 0
smua.source.limiti = 0.1

print("Zeroing capacitor voltage")

smua.source.output = smua.OUTPUT_ON
delay(1)
smua.source.output = smua.OUTPUT_OFF

smua.source.func = smua.OUTPUT_DCAMPS

--Set the constant current voltage of the test here!
smua.source.leveli = 1e-5
smua.measure.count = 1
smua.measure.rangei = 1e-4
smua.measure.rangev = 20

reading = 0
smua.source.output = smua.OUTPUT_ON
-- Set this voltage to as the voltage limit
while reading < 2
    reading = smua.measure.iv(smua.nvbuffer1, smua.nvbuffer2)
end

smua.measure.count = 10000
smua.source.leveli = 0
smua.measure.iv(smua.nvbuffer1, smua.nvbuffer2)
smua.source.output = smua.OUTPUT_OFF
