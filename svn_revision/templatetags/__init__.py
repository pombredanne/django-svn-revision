import os
import re
from subprocess import Popen, PIPE, STDOUT

def get_revision():
	try:
		trunk_path = os.path.join(os.path.abspath(os.path.dirname(__file__)),"../../../")
		command = ['svnversion',trunk_path]
		stIO = Popen(command, stdout=PIPE, stderr=STDOUT)
		stIO.wait()
		outS = stIO.stdout.read().strip()
		m = re.match(':?(\d*).*[MS]?', outS)
		return m.group(1) or ' '
	except:
		return 'Versioning Unavailable'

REVISION = get_revision()
