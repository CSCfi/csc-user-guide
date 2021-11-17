import sys
import re
section_name=sys.argv[1]
mid=section_name.lower().replace('.','').replace(' ','-')
mid2=re.sub('[^0-9a-zA-Z-]+','-',mid)
print(re.sub('[-]+','-',mid2))
