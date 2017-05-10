from ConfigParser import SafeConfigParser
import pdb
pdb.set_trace()
parser = SafeConfigParser()
parser.read('setup_env.config')

parser.remove_section('bug_tracker')
print parser.has_section('bug_tracker')
