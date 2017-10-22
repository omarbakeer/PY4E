text = "X-DSPAM-Confidence:    0.8475"
nspace = text.find(":")
subtext = text[nspace+1:]
snum = subtext.strip()
fnum = float(snum)
print(fnum)
