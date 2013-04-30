import re, sys
open(sys.argv[2],'w').write("\n".join(map(str,sorted([(c,w) for (w,c) in reduce(lambda d,k : (d.update({k:1+d.get(k,0)}), d)[1], re.split('\W+', open(sys.argv[1],'r').read().lower()), {}).items()]))))
