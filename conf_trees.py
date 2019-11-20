# Python code of the trees in the ensemble

# Model 1
def tree_1(xs):
	if xs[11] > 73.8:
		if xs[2] > 42821.0:
			if xs[0] > 58.0:
				if xs[8] > 14483.6:
					if xs[3] > 5.44:
						return ["0"]
					else: 
						return ["1"]
				else: 
					if xs[7] > 146205.4:
						if xs[11] > 5661.6:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
			else: 
				if xs[7] > 19207.3:
					if xs[8] > 45.4:
						if xs[8] > 63.2:
							return ["1"]
						else: 
							if xs[9] > 30841.6:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["0"]
				else: 
					if xs[2] > 387570.0:
						return ["0"]
					else: 
						return ["1"]
		else: 
			if xs[9] > 32855.159184:
				return ["1"]
			else: 
				if xs[0] > 40.0:
					return ["0"]
				else: 
					return ["1"]
	else: 
		if xs[8] > 10818.0:
			return ["1"]
		else: 
			if xs[6] > 33254.091667:
				if xs[1] == 'M':
					return ["1"]
				else: 
					return ["0"]
			else: 
				return ["0"]


# Model 2
def tree_2(xs):
	if xs[8] > 33.0:
		if xs[11] > 81.6:
			if xs[2] > 42821.0:
				if xs[10] > 28533.6:
					if xs[8] > 53.1:
						if xs[8] > 15092.9:
							if xs[0] > 58.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
					else: 
						if xs[8] > 52.6:
							return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[6] > 15940.035294:
						if xs[9] > 15904.947368:
							return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[10] > 23948.6:
							if xs[0] > 55.0:
								return ["1"]
							else: 
								if xs[4] > 3120.0:
									return ["0"]
								else: 
									return ["1"]
						else: 
							return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[9] > 31348.011321:
				return ["1"]
			else: 
				if xs[0] > 23.0:
					if xs[8] > 10707.1:
						return ["1"]
					else: 
						if xs[2] > 285387.0:
							if xs[8] > 116.9:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["0"]
				else: 
					return ["1"]
	else: 
		if xs[4] > 4743.0:
			return ["1"]
		else: 
			return ["0"]


# Model 3
def tree_3(xs):
	if xs[0] > 32.0:
		if xs[8] > 40.0:
			if xs[8] > 69.1:
				if xs[0] > 60.0:
					if xs[3] > 1.54:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[11] > 81.6:
						return ["1"]
					else: 
						if xs[3] > 3.35:
							return ["0"]
						else: 
							return ["1"]
			else: 
				if xs[1] == 'M':
					return ["0"]
				else: 
					return ["1"]
		else: 
			return ["0"]
	else: 
		if xs[8] > 52.6:
			if xs[8] > 97.1:
				if xs[6] > 12416.433962:
					if xs[8] > 543.9:
						return ["1"]
					else: 
						if xs[11] > 770.6:
							return ["1"]
						else: 
							if xs[4] > 18696.0:
								return ["1"]
							else: 
								return ["0"]
				else: 
					if xs[3] > 3.56:
						if xs[11] > 200.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["0"]
			else: 
				if xs[0] > 26.0:
					return ["1"]
				else: 
					return ["0"]
		else: 
			return ["0"]


# Model 4
def tree_4(xs):
	if xs[8] > 15.9:
		if xs[8] > 53.1:
			if xs[7] > 137739.3:
				if xs[7] > 148953.8:
					if xs[11] > 800.0:
						return ["1"]
					else: 
						if xs[3] > 3.74:
							return ["1"]
						else: 
							if xs[6] > 48024.188406:
								return ["0"]
							else: 
								return ["1"]
				else: 
					if xs[0] > 26.0:
						if xs[11] > 3400.0:
							return ["1"]
						else: 
							if xs[1] == 'M':
								return ["0"]
							else: 
								if xs[0] > 58.0:
									return ["1"]
								else: 
									return ["0"]
					else: 
						return ["1"]
			else: 
				if xs[11] > 187.6:
					if xs[7] > 28641.8:
						return ["1"]
					else: 
						if xs[3] > 4.72:
							if xs[4] > 2134.0:
								if xs[3] > 5.05:
									return ["1"]
								else: 
									if xs[0] > 50.0:
										return ["0"]
									else: 
										return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[11] > 14.6:
						return ["0"]
					else: 
						return ["1"]
		else: 
			if xs[6] > 36821.547222:
				if xs[1] == 'M':
					return ["0"]
				else: 
					if xs[0] > 26.0:
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["1"]
	else: 
		return ["0"]


# Model 5
def tree_5(xs):
	if xs[10] > 60714.6:
		if xs[11] > 770.6:
			if xs[10] > 61979.6:
				if xs[8] > 48.7:
					if xs[0] > 59.0:
						return ["1"]
					else: 
						if xs[0] > 21.0:
							return ["1"]
						else: 
							if xs[2] > 88757.0:
								return ["1"]
							else: 
								return ["0"]
				else: 
					return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[3] > 3.26:
				if xs[11] > 300.0:
					return ["1"]
				else: 
					if xs[8] > 165.1:
						return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[4] > 1875.0:
					if xs[11] > 26.3:
						return ["0"]
					else: 
						if xs[6] > 40737.607143:
							return ["1"]
						else: 
							return ["0"]
				else: 
					return ["1"]
	else: 
		if xs[10] > 25794.6:
			return ["1"]
		else: 
			if xs[10] > 25069.6:
				return ["0"]
			else: 
				if xs[2] > 75637.0:
					return ["1"]
				else: 
					if xs[3] > 2.01:
						return ["1"]
					else: 
						return ["0"]


# Model 6
def tree_6(xs):
	if xs[7] > 100863.5:
		if xs[9] > 30868.865116:
			if xs[0] > 59.0:
				return ["1"]
			else: 
				if xs[0] > 27.0:
					return ["1"]
				else: 
					if xs[11] > 600.0:
						return ["1"]
					else: 
						return ["0"]
		else: 
			if xs[3] > 7.01:
				return ["1"]
			else: 
				if xs[11] > 300.0:
					if xs[6] > 28829.751515:
						if xs[8] > 71.2:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
				else: 
					return ["0"]
	else: 
		if xs[9] > 12721.018519:
			if xs[2] > 42821.0:
				if xs[8] > 153.3:
					return ["1"]
				else: 
					if xs[2] > 94812.0:
						if xs[2] > 124605.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[3] > 4.72:
				if xs[3] > 5.05:
					return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[4] > 1181.0:
					return ["1"]
				else: 
					return ["0"]


# Model 7
def tree_7(xs):
	if xs[11] > 187.6:
		if xs[6] > 16488.234884:
			if xs[8] > 38.1:
				return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[2] > 75637.0:
				if xs[4] > 6872.0:
					if xs[11] > 2200.0:
						if xs[0] > 29.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
				else: 
					return ["1"]
			else: 
				if xs[2] > 75232.0:
					return ["0"]
				else: 
					if xs[6] > 16318.969231:
						return ["0"]
					else: 
						return ["1"]
	else: 
		if xs[7] > 41760.3:
			if xs[10] > 143200.0:
				if xs[1] == 'M':
					return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[4] > 4595.0:
					return ["1"]
				else: 
					return ["0"]
		else: 
			return ["1"]


# Model 8
def tree_8(xs):
	if xs[7] > 138194.0:
		if xs[0] > 27.0:
			if xs[7] > 144523.9:
				if xs[9] > 28458.316667:
					if xs[2] > 45714.0:
						return ["1"]
					else: 
						if xs[0] > 29.0:
							return ["1"]
						else: 
							return ["0"]
				else: 
					if xs[8] > 71.2:
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[11] > 770.6:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[7] > 19307.4:
			if xs[11] > 114.6:
				if xs[9] > 11833.172222:
					if xs[8] > 132.2:
						if xs[0] > 58.0:
							if xs[2] > 122603.0:
								return ["1"]
							else: 
								if xs[4] > 2122.0:
									if xs[4] > 2618.0:
										return ["1"]
									else: 
										return ["0"]
								else: 
									return ["1"]
						else: 
							return ["1"]
					else: 
						if xs[6] > 25530.419048:
							return ["1"]
						else: 
							if xs[11] > 3000.0:
								return ["1"]
							else: 
								return ["0"]
				else: 
					if xs[9] > 11292.310345:
						return ["0"]
					else: 
						return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[8] > 800.0:
				return ["1"]
			else: 
				if xs[3] > 2.62:
					return ["1"]
				else: 
					return ["0"]


# Model 9
def tree_9(xs):
	if xs[10] > 102414.6:
		if xs[11] > 129.0:
			if xs[10] > 147400.6:
				if xs[8] > 190.7:
					if xs[9] > 50526.426667:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[0] > 33.0:
					return ["1"]
				else: 
					if xs[5] == 'MONTHLY ISSUANCE':
						return ["1"]
					else: 
						if xs[1] == 'M':
							return ["0"]
						else: 
							return ["1"]
		else: 
			if xs[2] > 149893.0:
				if xs[2] > 285387.0:
					if xs[10] > 113514.6:
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[9] > 12721.018519:
			if xs[8] > 80.5:
				if xs[2] > 42821.0:
					if xs[7] > 85490.8:
						if xs[7] > 89026.6:
							return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[8] > 15092.9:
							if xs[0] > 58.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[3] > 3.6:
					return ["0"]
				else: 
					return ["1"]
		else: 
			if xs[2] > 197099.0:
				if xs[2] > 226122.0:
					if xs[11] > 4550.6:
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["0"]
			else: 
				return ["1"]


# Model 10
def tree_10(xs):
	if xs[11] > 187.6:
		if xs[7] > 190543.6:
			if xs[2] > 124605.0:
				return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[6] > 12920.502857:
				if xs[8] > 40.0:
					if xs[11] > 300.0:
						if xs[11] > 2000.0:
							return ["1"]
						else: 
							if xs[11] > 1800.0:
								return ["0"]
							else: 
								return ["1"]
					else: 
						return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[6] > 12912.161765:
					return ["0"]
				else: 
					return ["1"]
	else: 
		if xs[6] > 41248.920588:
			return ["1"]
		else: 
			if xs[10] > 64930.0:
				if xs[8] > 189.4:
					return ["1"]
				else: 
					if xs[6] > 36145.858065:
						if xs[0] > 51.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["0"]
			else: 
				if xs[0] > 49.0:
					return ["1"]
				else: 
					return ["0"]


