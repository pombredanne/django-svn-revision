import os
import re
from subprocess import Popen, PIPE, STDOUT

from django.conf import settings

def get_revision():
	try:
		command = ['svnversion',settings.PROJECT_ROOT]
		stIO = Popen(command, stdout=PIPE, stderr=STDOUT)
		stIO.wait()
		outS = stIO.stdout.read().strip()
		m = re.match(':?(\d*).*[MS]?', outS)
		return m.group(1) or ' '
	except:
		return 'Versioning Unavailable'

REVISION = get_revision()
