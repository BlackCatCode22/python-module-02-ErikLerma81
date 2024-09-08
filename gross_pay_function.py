def computepay (hours, rate):
    print ("in compute pay", hours, rate)
    if hours > 40:
        reg = rate * hours
        otp = (hours - 40.0) * (rate * 0.5)
        pay = reg + otp
    else:
        pay =hours * rate
    print("returning", pay)
    return pay


sh = input ("Enter hours: ")
sr = input ("Enter rate: ")
try:
    fh = float(sh)
    fr = float (sr)
except:
    print ("Error, please enter numeric input")
    quit()

xp = computepay(fh,fr)

print ("Pay:" , xp)
