
function holdVoltage(voltage, filename)

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
    
    print("Setting voltage...")
    smua.source.func = smua.OUTPUT_DCVOLTS
    smua.source.levelv = voltage
    smua.source.limiti = 0.1

    smua.measure.count = 80000
    smua.measure.rangei = 1e-4
    smua.measure.rangev = 20

    --This sets the measurement time to 10ms
    smua.measure.nplc = 0.6

    --Turn on the source meter and delay for a while to let it stabilize
    smua.source.output = smua.OUTPUT_ON
    delay(30)
    
    print("Collecting data...")
    smua.measure.iv(smua.nvbuffer1, smua.nvbuffer2)

    print("Saving data...")
    savebuffer(smua.nvbuffer2,"csv",filename)
    print("Done.")
end

holdVoltage(2.5666, "LTO_hold_2.5666v.csv")
