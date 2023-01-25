import commlib as cl

# Parameters
TS = 1e-6
samples_per_symbol = 20
tinitial = 0
tguard = 10 * TS
#attribute Name for change dynamical 
Name = 'Nikos Karapiperis'

# using join() + ord() + format()
# Converting String to binary
# set bits to be transmitted that are my name
bits = ''.join(format(ord(i), '08b') for i in Name )


# Signal constellation 2-PAM
c = cl.pam_constellation(2)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c)

if(len(bits) % 1 != 0):
    while(len(bits) % 1 != 0):
        bits = bits + '0'

#build waveform from input bits
x.modulate_from_bits( bits, constellation = c )
#set True for close first all plots and 1 for set figure number
x.plot(True,1)


# Signal constellation 4-PAM
c1 = cl.pam_constellation(4)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c1)

if(len(bits) % 2 != 0):
    while(len(bits) % 2 != 0):
        bits = bits + '0'
       
#build waveform from input bits
x.modulate_from_bits( bits, constellation = c1 )
x.plot(False,2)


# Signal constellation 8-PAM
c2 = cl.pam_constellation(8)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c2)

if(len(bits) % 3 != 0):
    while(len(bits) % 3 != 0):
        bits = bits + '0'
 
#build waveform from input bits
x.modulate_from_bits( bits, constellation = c2 )
x.plot(False,3)


# Signal constellation 16-PAM
c3 = cl.pam_constellation(16)

# build input waveform and plot
x = cl.digital_signal(TS = TS, samples_per_symbol = samples_per_symbol, 
                      tinitial = tinitial, tguard = tguard, constellation = c3)

if(len(bits) % 4 != 0):
    while(len(bits) % 4 != 0):
        bits = bits + '0'

#build waveform from input bits
x.modulate_from_bits( bits, constellation = c3 )
x.plot(False,4)




















