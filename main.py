import re
import sys
from looped_experiments.main import run

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    print(sys.argv)
    sys.exit(run())
