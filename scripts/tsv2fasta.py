import sys, os

if __name__ == "__main__":

	list_fastaID = []
	ll_seq = ''
	sitesOfInterest = ["S", "EQ", "X", "D"]
	with open(sys.argv[1]) as fin:
		count = 0
		for line in fin:
			if line.startswith("#"):
				continue
			line = line.strip().split()

			if len(line) != 9:
				continue

			newID = line[0] + "_" + line[1]

			if newID not in list_fastaID:
				if ll_seq != '':
					print (ll_seq)
				ll_seq = ''
				if line[8] in sitesOfInterest:
					ll_seq += line[7]
				list_fastaID.append(newID)
				print (">%s" % newID)
			else:
				if line[8] in sitesOfInterest:
					ll_seq += line[7]
		print (ll_seq)

