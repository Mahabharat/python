from collections import Counter
text=" Communications System Toolbox Support Package for RTL-SDR Radio  15.1.0 - glnxa64 maci64 win32 win64"\
   "Communications System Toolbox Support Package for SDR Base  15.1.0 - glnxa64 maci64 win32 win64"\
   "Communications System Toolbox Support Package for SDR FZBase  15.1.0 - glnxa64 win32 win64"\
   "Communications System Toolbox Support Package for SDR Plugin Base  15.1.0 - glnxa64 win32 win64"\
   
print(list(text))			#list of letters

words=text.split()			#list of words



print(words)


count=Counter(words)
print "\n",count

print('\n')
top_three=count.most_common(3)
print(top_three)
