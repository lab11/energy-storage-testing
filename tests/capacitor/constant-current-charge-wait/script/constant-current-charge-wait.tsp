
function measureCapacitor(current, voltage, filename)

    --Initialize SMU
    reset()
    errorqueue.clear()
    status.reset()
    display.screen = display.SMUA

    --Setup Buffers
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
    delay(2)
    smua.source.output = smua.OUTPUT_OFF

    smua.source.func = smua.OUTPUT_DCAMPS

    --Set the constant current voltage of the test here!
    smua.source.leveli = current
    smua.measure.count = 1
    smua.measure.rangei = 1e-4
    smua.measure.rangev = 20

    --This sets the measurement time to 1ms
    smua.measure.nplc = 0.06

    print("Charging capacitor...")
    smua.source.output = smua.OUTPUT_ON

    repeat 
        c, v = smua.measure.iv(smua.nvbuffer1, smua.nvbuffer2)
    until v >= voltage
    
    print("Measuring absorption...")
    smua.source.leveli = 0
    smua.measure.count = 55000
    smua.measure.iv(smua.nvbuffer1, smua.nvbuffer2)
    smua.source.output = smua.OUTPUT_OFF

    print("Saving data...")
    savebuffer(smua.nvbuffer2,"csv",filename)
    print("Done.
end

measureCapacitor(0.00001, 2, "nichon_100uf_10ua_2v_1.csv")
