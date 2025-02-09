# ---------------------------------------------------------------------------

def getdict(d, n, defv):
	if d.has_key(n): return d[n]
	return defv

def read_settings(fn):
	KNH_DATA = {}
	try:
		f = open(fn)
		exec(f)
		f.close()
		return KNH_DATA
	except OSError, e:
		print e
		return KNH_DATA

# ---------------------------------------------------------------------------

def nz_fname(fname):