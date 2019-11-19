# Python code of the trees in the ensemble

# Model 1
def tree_1(xs):
	if xs[2] > 42821.0:
		if xs[11] > 51.2:
			if xs[4] > 1117.0:
				if xs[11] > 300.0:
					if xs[0] > 61.0:
						if xs[8] > 800.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[5] == 'ISSUANCE AFTER TRANSACTION':
							if xs[7] > 27304.7:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[8] > 6.0:
								if xs[9] > 19102.13913:
									return ["1"]
								else: 
									if xs[7] > 22564.4:
										return ["1"]
									else: 
										if xs[9] > 14110.241379:
											return ["0"]
										else: 
											if xs[7] > 21970.7:
												return ["0"]
											else: 
												return ["1"]
							else: 
								return ["0"]
				else: 
					if xs[6] > 25294.125806:
						return ["1"]
					else: 
						if xs[10] > 23768.6:
							return ["0"]
						else: 
							return ["1"]
			else: 
				if xs[2] > 51428.0:
					return ["0"]
				else: 
					return ["1"]
		else: 
			if xs[6] > 39429.048214:
				return ["1"]
			else: 
				if xs[0] > 27.0:
					if xs[8] > 23.2:
						return ["0"]
					else: 
						if xs[3] > 3.56:
							return ["1"]
						else: 
							return ["0"]
				else: 
					if xs[3] > 5.44:
						return ["1"]
					else: 
						if xs[2] > 323870.0:
							return ["1"]
						else: 
							return ["0"]
	else: 
		return ["1"]


# Model 2
def tree_2(xs):
	if xs[11] > 30.0:
		if xs[9] > 13387.8875:
			if xs[4] > 1117.0:
				if xs[8] > 19.7:
					if xs[10] > 96391.4:
						return ["1"]
					else: 
						if xs[10] > 93914.6:
							return ["1"]
						else: 
							if xs[11] > 300.0:
								if xs[7] > 114939.7:
									return ["1"]
								else: 
									if xs[3] > 4.72:
										if xs[0] > 36.0:
											return ["1"]
										else: 
											if xs[9] > 34776.723404:
												return ["0"]
											else: 
												if xs[2] > 148545.0:
													if xs[8] > 700.0:
														return ["0"]
													else: 
														return ["1"]
												else: 
													return ["1"]
									else: 
										return ["1"]
							else: 
								if xs[4] > 6132.0:
									return ["0"]
								else: 
									return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[0] > 48.0:
					if xs[2] > 51428.0:
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
		else: 
			if xs[7] > 17628.4:
				if xs[11] > 1114.6:
					if xs[4] > 3198.0:
						return ["0"]
					else: 
						if xs[8] > 500.0:
							return ["1"]
						else: 
							if xs[12] == 'Y':
								if xs[7] > 21171.3:
									return ["0"]
								else: 
									return ["1"]
							else: 
								return ["1"]
				else: 
					return ["1"]
			else: 
				return ["1"]
	else: 
		if xs[4] > 2134.0:
			if xs[3] > 3.74:
				return ["1"]
			else: 
				if xs[6] > 27930.427941:
					return ["1"]
				else: 
					return ["0"]
		else: 
			return ["0"]


# Model 3
def tree_3(xs):
	if xs[8] > 6.4:
		if xs[8] > 30.5:
			if xs[10] > 17114.6:
				if xs[11] > 14.6:
					if xs[0] > 61.0:
						return ["1"]
					else: 
						if xs[12] == 'Y':
							if xs[8] > 63.2:
								if xs[9] > 11770.021667:
									if xs[0] > 22.0:
										if xs[4] > 6872.0:
											if xs[9] > 19102.13913:
												return ["1"]
											else: 
												if xs[4] > 10108.0:
													return ["1"]
												else: 
													if xs[10] > 32807.6:
														return ["0"]
													else: 
														return ["1"]
										else: 
											return ["1"]
									else: 
										return ["1"]
								else: 
									if xs[5] == 'MONTHLY ISSUANCE':
										if xs[6] > 12473.256364:
											return ["0"]
										else: 
											return ["1"]
									else: 
										return ["0"]
							else: 
								if xs[8] > 62.7:
									return ["0"]
								else: 
									return ["1"]
						else: 
							return ["1"]
				else: 
					if xs[6] > 28598.256:
						if xs[8] > 150.6:
							return ["1"]
						else: 
							if xs[2] > 387570.0:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[8] > 6.8:
				if xs[10] > 149562.0:
					return ["1"]
				else: 
					return ["0"]
			else: 
				return ["1"]
	else: 
		return ["0"]


# Model 4
def tree_4(xs):
	if xs[8] > 6.0:
		if xs[11] > 30.0:
			if xs[4] > 1117.0:
				if xs[8] > 37.9:
					if xs[6] > 17373.398462:
						return ["1"]
					else: 
						if xs[6] > 17190.125:
							return ["0"]
						else: 
							if xs[10] > 42368.4:
								return ["1"]
							else: 
								if xs[3] > 5.05:
									if xs[9] > 14054.135484:
										return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[10] > 40614.6:
										return ["1"]
									else: 
										if xs[3] > 0.59:
											return ["1"]
										else: 
											if xs[11] > 2700.0:
												return ["0"]
											else: 
												return ["1"]
				else: 
					if xs[4] > 2487.0:
						return ["0"]
					else: 
						return ["1"]
			else: 
				return ["1"]
		else: 
			if xs[9] > 31979.309231:
				return ["1"]
			else: 
				if xs[1] == 'M':
					return ["0"]
				else: 
					if xs[2] > 148545.0:
						return ["1"]
					else: 
						if xs[0] > 38.0:
							return ["0"]
						else: 
							return ["1"]
	else: 
		return ["0"]


# Model 5
def tree_5(xs):
	if xs[2] > 42821.0:
		if xs[9] > 39846.785:
			return ["1"]
		else: 
			if xs[8] > 22.3:
				if xs[6] > 46870.02:
					return ["1"]
				else: 
					if xs[11] > 30.0:
						if xs[7] > 22564.4:
							if xs[8] > 63.2:
								if xs[3] > 4.72:
									if xs[0] > 20.0:
										if xs[7] > 24825.8:
											return ["1"]
										else: 
											return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
							else: 
								if xs[8] > 52.4:
									if xs[9] > 22373.99:
										return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
						else: 
							if xs[2] > 387570.0:
								return ["0"]
							else: 
								if xs[7] > 22519.6:
									return ["0"]
								else: 
									return ["1"]
					else: 
						if xs[12] == 'Y':
							if xs[9] > 24506.712281:
								if xs[3] > 3.49:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["0"]
						else: 
							return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[8] > 200.0:
			return ["1"]
		else: 
			if xs[0] > 41.0:
				return ["1"]
			else: 
				return ["0"]


# Model 6
def tree_6(xs):
	if xs[11] > 51.2:
		if xs[8] > 22.3:
			if xs[3] > 5.88:
				if xs[3] > 6.55:
					if xs[8] > 53.1:
						return ["1"]
					else: 
						if xs[2] > 119895.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[6] > 12918.380952:
					if xs[8] > 37.9:
						if xs[6] > 25294.125806:
							return ["1"]
						else: 
							if xs[7] > 102988.4:
								return ["0"]
							else: 
								if xs[9] > 12084.414286:
									if xs[9] > 17208.9:
										if xs[7] > 24825.8:
											return ["1"]
										else: 
											return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
					else: 
						return ["1"]
				else: 
					if xs[6] > 12473.256364:
						return ["0"]
					else: 
						if xs[9] > 11288.451429:
							if xs[11] > 1200.0:
								return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
		else: 
			if xs[2] > 117897.0:
				return ["0"]
			else: 
				return ["1"]
	else: 
		if xs[6] > 27967.306897:
			if xs[2] > 387570.0:
				return ["1"]
			else: 
				if xs[4] > 10108.0:
					return ["0"]
				else: 
					if xs[7] > 117282.2:
						if xs[0] > 43.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
		else: 
			return ["0"]


# Model 7
def tree_7(xs):
	if xs[6] > 7604.107143:
		if xs[0] > 62.0:
			return ["1"]
		else: 
			if xs[8] > 37.9:
				if xs[11] > 14.6:
					if xs[3] > 5.88:
						if xs[0] > 20.0:
							if xs[4] > 5190.0:
								if xs[5] == 'MONTHLY ISSUANCE':
									if xs[10] > 81600.0:
										return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
							else: 
								return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[6] > 16522.961111:
							return ["1"]
						else: 
							if xs[5] == 'MONTHLY ISSUANCE':
								if xs[7] > 29023.8:
									return ["0"]
								else: 
									if xs[3] > 0.59:
										if xs[9] > 11561.647619:
											return ["1"]
										else: 
											if xs[7] > 22519.6:
												return ["0"]
											else: 
												return ["1"]
									else: 
										if xs[11] > 2700.0:
											return ["0"]
										else: 
											return ["1"]
							else: 
								return ["1"]
				else: 
					if xs[7] > 141985.9:
						return ["1"]
					else: 
						if xs[7] > 114380.5:
							return ["0"]
						else: 
							return ["1"]
			else: 
				if xs[0] > 58.0:
					return ["1"]
				else: 
					return ["0"]
	else: 
		return ["0"]


# Model 8
def tree_8(xs):
	if xs[0] > 61.0:
		if xs[4] > 6295.0:
			return ["0"]
		else: 
			return ["1"]
	else: 
		if xs[8] > 7.0:
			if xs[11] > 14.6:
				if xs[3] > 7.68:
					if xs[7] > 21354.4:
						if xs[1] == 'M':
							if xs[0] > 44.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[9] > 25591.85625:
						return ["1"]
					else: 
						if xs[10] > 93114.6:
							if xs[6] > 26473.510345:
								return ["1"]
							else: 
								if xs[7] > 89842.5:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[6] > 28748.380303:
								if xs[6] > 29237.011765:
									return ["1"]
								else: 
									return ["0"]
							else: 
								if xs[11] > 300.0:
									if xs[9] > 11561.647619:
										if xs[10] > 39881.6:
											return ["1"]
										else: 
											if xs[9] > 17452.427027:
												if xs[4] > 6295.0:
													if xs[6] > 17816.08:
														return ["1"]
													else: 
														return ["0"]
												else: 
													return ["1"]
											else: 
												return ["1"]
									else: 
										if xs[7] > 22519.6:
											return ["0"]
										else: 
											if xs[6] > 12473.256364:
												return ["0"]
											else: 
												return ["1"]
								else: 
									if xs[8] > 132.2:
										return ["1"]
									else: 
										return ["0"]
			else: 
				if xs[7] > 165422.1:
					return ["1"]
				else: 
					if xs[0] > 38.0:
						return ["0"]
					else: 
						if xs[9] > 21957.978261:
							return ["1"]
						else: 
							return ["0"]
		else: 
			return ["0"]


# Model 9
def tree_9(xs):
	if xs[8] > 22.3:
		if xs[11] > 30.0:
			if xs[7] > 24825.8:
				if xs[11] > 300.0:
					if xs[6] > 16522.961111:
						if xs[0] > 61.0:
							if xs[3] > 0.43:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[3] > 5.88:
								if xs[0] > 20.0:
									if xs[8] > 53.1:
										return ["1"]
									else: 
										return ["0"]
								else: 
									return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[0] > 25.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[8] > 132.2:
						return ["1"]
					else: 
						if xs[3] > 2.43:
							return ["0"]
						else: 
							return ["1"]
			else: 
				if xs[7] > 24797.7:
					return ["0"]
				else: 
					if xs[2] > 42821.0:
						if xs[11] > 7010.6:
							if xs[2] > 112065.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							if xs[3] > 0.59:
								if xs[8] > 500.0:
									return ["1"]
								else: 
									if xs[11] > 2300.0:
										return ["1"]
									else: 
										if xs[10] > 28488.6:
											return ["0"]
										else: 
											if xs[2] > 88757.0:
												if xs[4] > 3158.0:
													return ["1"]
												else: 
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
			if xs[10] > 132114.6:
				return ["1"]
			else: 
				if xs[7] > 101117.1:
					if xs[10] > 83714.6:
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
	else: 
		return ["0"]


# Model 10
def tree_10(xs):
	if xs[9] > 37592.240625:
		return ["1"]
	else: 
		if xs[11] > 129.3:
			if xs[11] > 7500.0:
				return ["1"]
			else: 
				if xs[10] > 145514.6:
					if xs[2] > 58400.0:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[9] > 32731.228571:
						return ["1"]
					else: 
						if xs[12] == 'Y':
							if xs[2] > 177686.0:
								if xs[0] > 57.0:
									return ["1"]
								else: 
									if xs[0] > 48.0:
										return ["0"]
									else: 
										if xs[8] > 19.7:
											if xs[7] > 24825.8:
												return ["1"]
											else: 
												if xs[6] > 15557.852459:
													return ["0"]
												else: 
													return ["1"]
										else: 
											return ["0"]
							else: 
								if xs[8] > 37.9:
									if xs[5] == 'ISSUANCE AFTER TRANSACTION':
										return ["1"]
									else: 
										if xs[2] > 58796.0:
											if xs[7] > 19307.4:
												return ["1"]
											else: 
												if xs[1] == 'M':
													if xs[10] > 19449.6:
														return ["0"]
													else: 
														return ["1"]
												else: 
													return ["1"]
										else: 
											if xs[1] == 'M':
												if xs[8] > 200.0:
													return ["1"]
												else: 
													return ["0"]
											else: 
												return ["1"]
								else: 
									if xs[3] > 3.64:
										return ["1"]
									else: 
										return ["0"]
						else: 
							return ["1"]
		else: 
			if xs[8] > 5.1:
				if xs[2] > 70646.0:
					if xs[7] > 117282.2:
						if xs[7] > 173693.5:
							return ["1"]
						else: 
							if xs[6] > 32844.934783:
								if xs[2] > 122603.0:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["0"]
					else: 
						return ["1"]
				else: 
					return ["0"]
			else: 
				return ["0"]


# Model 11
def tree_11(xs):
	if xs[11] > 51.2:
		if xs[6] > 17816.08:
			if xs[9] > 36075.660526:
				return ["1"]
			else: 
				if xs[11] > 300.0:
					if xs[0] > 20.0:
						return ["1"]
					else: 
						if xs[6] > 28748.380303:
							return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[3] > 4.28:
						return ["0"]
					else: 
						return ["1"]
		else: 
			if xs[5] == 'ISSUANCE AFTER TRANSACTION':
				return ["0"]
			else: 
				if xs[2] > 42821.0:
					if xs[3] > 5.88:
						if xs[6] > 15622.227273:
							return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[9] > 18581.157143:
							return ["0"]
						else: 
							if xs[9] > 17167.873913:
								return ["1"]
							else: 
								if xs[4] > 1879.0:
									if xs[8] > 800.0:
										return ["1"]
									else: 
										if xs[4] > 5892.0:
											return ["0"]
										else: 
											return ["1"]
								else: 
									if xs[10] > 31450.4:
										if xs[4] > 1668.0:
											return ["0"]
										else: 
											if xs[10] > 31614.6:
												return ["1"]
											else: 
												return ["0"]
									else: 
										return ["1"]
				else: 
					return ["0"]
	else: 
		if xs[7] > 165422.1:
			return ["1"]
		else: 
			if xs[9] > 29988.672222:
				return ["1"]
			else: 
				if xs[10] > 104830.0:
					return ["0"]
				else: 
					if xs[2] > 148545.0:
						return ["1"]
					else: 
						if xs[6] > 22520.205882:
							return ["1"]
						else: 
							return ["0"]


# Model 12
def tree_12(xs):
	if xs[11] > 200.0:
		if xs[8] > 37.9:
			if xs[7] > 19307.4:
				return ["1"]
			else: 
				if xs[7] > 18423.3:
					return ["0"]
				else: 
					return ["1"]
		else: 
			if xs[0] > 53.0:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[4] > 1542.0:
			if xs[8] > 30.5:
				if xs[0] > 59.0:
					return ["0"]
				else: 
					if xs[11] > 100.0:
						return ["0"]
					else: 
						if xs[8] > 150.6:
							return ["1"]
						else: 
							if xs[9] > 31979.309231:
								return ["1"]
							else: 
								if xs[10] > 132114.6:
									return ["1"]
								else: 
									if xs[1] == 'M':
										return ["0"]
									else: 
										return ["1"]
			else: 
				return ["0"]
		else: 
			return ["0"]


# Model 13
def tree_13(xs):
	if xs[6] > 43274.473684:
		return ["1"]
	else: 
		if xs[10] > 122628.4:
			if xs[10] > 126175.3:
				if xs[11] > 2100.0:
					return ["1"]
				else: 
					if xs[7] > 141652.9:
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[7] > 154222.0:
				return ["0"]
			else: 
				if xs[11] > 51.2:
					if xs[6] > 43072.372:
						return ["0"]
					else: 
						if xs[3] > 5.88:
							if xs[7] > 23346.7:
								if xs[10] > 71770.6:
									if xs[0] > 36.0:
										return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[9] > 13387.8875:
								return ["1"]
							else: 
								if xs[3] > 0.59:
									if xs[5] == 'MONTHLY ISSUANCE':
										if xs[1] == 'M':
											if xs[8] > 500.0:
												return ["1"]
											else: 
												if xs[11] > 1400.0:
													if xs[0] > 34.0:
														return ["0"]
													else: 
														return ["1"]
												else: 
													return ["1"]
										else: 
											return ["1"]
									else: 
										return ["0"]
								else: 
									if xs[1] == 'M':
										return ["0"]
									else: 
										return ["1"]
				else: 
					if xs[10] > 105398.3:
						return ["0"]
					else: 
						if xs[7] > 45601.0:
							if xs[3] > 3.09:
								return ["1"]
							else: 
								if xs[4] > 6261.0:
									return ["1"]
								else: 
									return ["0"]
						else: 
							return ["0"]


# Model 14
def tree_14(xs):
	if xs[7] > 177099.7:
		return ["1"]
	else: 
		if xs[11] > 51.2:
			if xs[7] > 174961.8:
				return ["0"]
			else: 
				if xs[8] > 22.3:
					if xs[8] > 63.2:
						if xs[9] > 13387.8875:
							if xs[7] > 22564.4:
								if xs[11] > 300.0:
									if xs[6] > 43072.372:
										if xs[7] > 63374.3:
											if xs[0] > 61.0:
												return ["0"]
											else: 
												return ["1"]
										else: 
											return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[0] > 51.0:
										return ["0"]
									else: 
										return ["1"]
							else: 
								if xs[11] > 2491.4:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[9] > 13044.533333:
								return ["0"]
							else: 
								if xs[5] == 'MONTHLY ISSUANCE':
									if xs[6] > 10903.258824:
										if xs[8] > 500.0:
											return ["1"]
										else: 
											if xs[3] > 2.87:
												if xs[9] > 11288.451429:
													return ["0"]
												else: 
													return ["1"]
											else: 
												return ["1"]
									else: 
										return ["1"]
								else: 
									return ["0"]
					else: 
						if xs[6] > 25294.125806:
							return ["1"]
						else: 
							return ["0"]
				else: 
					return ["0"]
		else: 
			if xs[8] > 12.1:
				if xs[7] > 154696.7:
					return ["1"]
				else: 
					if xs[10] > 105398.3:
						if xs[9] > 29988.672222:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
			else: 
				return ["0"]


# Model 15
def tree_15(xs):
	if xs[7] > 101117.1:
		if xs[6] > 29613.735849:
			if xs[8] > 30.5:
				if xs[11] > 14.6:
					if xs[9] > 28739.808824:
						return ["1"]
					else: 
						if xs[8] > 53.1:
							return ["1"]
						else: 
							return ["0"]
				else: 
					if xs[6] > 39429.048214:
						return ["1"]
					else: 
						if xs[3] > 5.44:
							return ["1"]
						else: 
							return ["0"]
			else: 
				if xs[8] > 6.8:
					return ["0"]
				else: 
					return ["1"]
		else: 
			if xs[10] > 86990.7:
				if xs[7] > 141985.9:
					return ["1"]
				else: 
					return ["0"]
			else: 
				return ["1"]
	else: 
		if xs[5] == 'ISSUANCE AFTER TRANSACTION':
			return ["1"]
		else: 
			if xs[3] > 1.86:
				if xs[8] > 132.2:
					if xs[0] > 36.0:
						return ["1"]
					else: 
						if xs[10] > 30226.6:
							if xs[0] > 33.0:
								if xs[1] == 'M':
									return ["0"]
								else: 
									return ["1"]
							else: 
								if xs[2] > 106054.0:
									return ["1"]
								else: 
									if xs[9] > 34948.638889:
										return ["1"]
									else: 
										if xs[3] > 3.22:
											return ["0"]
										else: 
											return ["1"]
						else: 
							return ["1"]
				else: 
					return ["1"]
			else: 
				return ["1"]


# Model 16
def tree_16(xs):
	if xs[0] > 62.0:
		if xs[4] > 4433.0:
			return ["1"]
		else: 
			return ["0"]
	else: 
		if xs[8] > 5.1:
			if xs[4] > 1117.0:
				if xs[10] > 132014.6:
					return ["1"]
				else: 
					if xs[11] > 30.0:
						if xs[8] > 37.9:
							if xs[4] > 6872.0:
								if xs[11] > 300.0:
									if xs[6] > 47215.479412:
										return ["0"]
									else: 
										if xs[7] > 24825.8:
											return ["1"]
										else: 
											if xs[9] > 15615.394286:
												return ["0"]
											else: 
												return ["1"]
								else: 
									return ["0"]
							else: 
								if xs[2] > 42821.0:
									if xs[9] > 13387.8875:
										return ["1"]
									else: 
										if xs[10] > 36964.6:
											return ["0"]
										else: 
											if xs[4] > 3198.0:
												if xs[8] > 400.0:
													return ["0"]
												else: 
													return ["1"]
											else: 
												return ["1"]
								else: 
									return ["1"]
						else: 
							if xs[0] > 48.0:
								return ["1"]
							else: 
								return ["0"]
					else: 
						if xs[0] > 27.0:
							if xs[10] > 83714.6:
								if xs[2] > 148545.0:
									if xs[9] > 24506.712281:
										return ["1"]
									else: 
										return ["0"]
								else: 
									return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
			else: 
				if xs[3] > 1.25:
					return ["1"]
				else: 
					return ["0"]
		else: 
			return ["0"]


# Model 17
def tree_17(xs):
	if xs[11] > 30.0:
		if xs[2] > 387570.0:
			if xs[10] > 35004.6:
				if xs[9] > 35116.14:
					return ["0"]
				else: 
					return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[11] > 200.0:
				if xs[7] > 187318.8:
					return ["1"]
				else: 
					if xs[8] > 37.9:
						if xs[9] > 13387.8875:
							if xs[6] > 15622.227273:
								if xs[3] > 4.72:
									if xs[11] > 6900.0:
										if xs[3] > 6.55:
											return ["1"]
										else: 
											if xs[0] > 36.0:
												return ["1"]
											else: 
												if xs[11] > 8300.0:
													return ["1"]
												else: 
													return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
							else: 
								return ["1"]
						else: 
							if xs[6] > 14666.582609:
								if xs[3] > 3.6:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[4] > 4743.0:
					return ["0"]
				else: 
					return ["1"]
	else: 
		if xs[8] > 12.1:
			if xs[10] > 97914.6:
				if xs[10] > 126175.3:
					if xs[0] > 47.0:
						return ["1"]
					else: 
						if xs[0] > 40.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					return ["0"]
			else: 
				return ["1"]
		else: 
			return ["0"]


# Model 18
def tree_18(xs):
	if xs[9] > 39846.785:
		return ["1"]
	else: 
		if xs[9] > 39789.647059:
			return ["0"]
		else: 
			if xs[3] > 8.23:
				if xs[7] > 38262.6:
					return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[8] > 7.0:
					if xs[8] > 37.9:
						if xs[0] > 62.0:
							if xs[6] > 26548.862162:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[7] > 101117.1:
								if xs[3] > 1.85:
									if xs[3] > 1.96:
										if xs[6] > 25294.125806:
											if xs[0] > 22.0:
												if xs[7] > 137440.1:
													return ["1"]
												else: 
													if xs[11] > 2491.4:
														return ["1"]
													else: 
														if xs[0] > 40.0:
															return ["0"]
														else: 
															return ["1"]
											else: 
												return ["0"]
										else: 
											return ["0"]
									else: 
										return ["0"]
								else: 
									return ["1"]
							else: 
								if xs[7] > 27304.7:
									return ["1"]
								else: 
									if xs[8] > 1100.0:
										return ["1"]
									else: 
										if xs[7] > 26402.2:
											return ["0"]
										else: 
											if xs[9] > 10544.744:
												if xs[10] > 28382.0:
													return ["1"]
												else: 
													if xs[8] > 300.0:
														if xs[0] > 49.0:
															return ["1"]
														else: 
															return ["0"]
													else: 
														return ["1"]
											else: 
												return ["1"]
					else: 
						if xs[7] > 165422.1:
							return ["1"]
						else: 
							if xs[0] > 46.0:
								return ["0"]
							else: 
								return ["1"]
				else: 
					return ["0"]


# Model 19
def tree_19(xs):
	if xs[8] > 6.0:
		if xs[8] > 37.9:
			if xs[2] > 42821.0:
				if xs[11] > 14.6:
					if xs[8] > 63.2:
						if xs[0] > 62.0:
							return ["1"]
						else: 
							if xs[9] > 19102.13913:
								return ["1"]
							else: 
								if xs[9] > 19071.13125:
									return ["0"]
								else: 
									if xs[7] > 58177.3:
										return ["1"]
									else: 
										if xs[2] > 387570.0:
											if xs[9] > 16723.606897:
												return ["0"]
											else: 
												return ["1"]
										else: 
											if xs[0] > 48.0:
												if xs[11] > 2300.0:
													return ["1"]
												else: 
													if xs[0] > 51.0:
														return ["1"]
													else: 
														return ["0"]
											else: 
												return ["1"]
					else: 
						if xs[8] > 59.4:
							return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[0] > 47.0:
						return ["1"]
					else: 
						if xs[0] > 40.0:
							return ["1"]
						else: 
							return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[0] > 53.0:
				return ["1"]
			else: 
				if xs[3] > 3.74:
					return ["1"]
				else: 
					return ["0"]
	else: 
		return ["0"]


# Model 20
def tree_20(xs):
	if xs[6] > 50273.102439:
		return ["1"]
	else: 
		if xs[8] > 30.5:
			if xs[6] > 49989.158621:
				return ["1"]
			else: 
				if xs[8] > 900.0:
					return ["1"]
				else: 
					if xs[11] > 30.0:
						if xs[7] > 23346.7:
							if xs[8] > 53.1:
								if xs[0] > 20.0:
									return ["1"]
								else: 
									if xs[3] > 4.72:
										return ["0"]
									else: 
										return ["1"]
							else: 
								return ["1"]
						else: 
							if xs[2] > 387570.0:
								return ["0"]
							else: 
								if xs[2] > 42821.0:
									if xs[7] > 22519.6:
										if xs[3] > 2.01:
											return ["0"]
										else: 
											return ["1"]
									else: 
										if xs[4] > 2822.0:
											if xs[9] > 13387.8875:
												return ["1"]
											else: 
												if xs[10] > 20426.6:
													return ["0"]
												else: 
													return ["1"]
										else: 
											return ["1"]
								else: 
									return ["0"]
					else: 
						if xs[2] > 70646.0:
							if xs[3] > 3.74:
								return ["1"]
							else: 
								if xs[2] > 387570.0:
									return ["1"]
								else: 
									if xs[0] > 40.0:
										return ["1"]
									else: 
										return ["0"]
						else: 
							return ["0"]
		else: 
			return ["0"]


# Model 21
def tree_21(xs):
	if xs[8] > 6.0:
		if xs[4] > 888.0:
			if xs[4] > 1542.0:
				if xs[8] > 30.5:
					if xs[8] > 64.8:
						if xs[7] > 22564.4:
							if xs[6] > 26548.862162:
								return ["1"]
							else: 
								if xs[7] > 70805.4:
									if xs[4] > 6872.0:
										return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
						else: 
							if xs[9] > 14610.248:
								return ["0"]
							else: 
								if xs[0] > 30.0:
									return ["1"]
								else: 
									if xs[11] > 2900.0:
										return ["0"]
									else: 
										return ["1"]
					else: 
						if xs[11] > 2491.4:
							return ["1"]
						else: 
							if xs[5] == 'MONTHLY ISSUANCE':
								return ["0"]
							else: 
								return ["1"]
				else: 
					if xs[0] > 50.0:
						return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[11] > 30.0:
					if xs[2] > 70646.0:
						return ["1"]
					else: 
						if xs[11] > 7000.0:
							return ["1"]
						else: 
							if xs[4] > 1452.0:
								return ["0"]
							else: 
								if xs[8] > 200.0:
									return ["1"]
								else: 
									if xs[2] > 58400.0:
										return ["1"]
									else: 
										if xs[5] == 'MONTHLY ISSUANCE':
											return ["0"]
										else: 
											return ["1"]
				else: 
					return ["0"]
		else: 
			return ["0"]
	else: 
		return ["0"]


# Model 22
def tree_22(xs):
	if xs[8] > 30.5:
		if xs[8] > 64.8:
			if xs[7] > 23346.7:
				if xs[6] > 17277.883871:
					if xs[11] > 300.0:
						return ["1"]
					else: 
						if xs[12] == 'Y':
							if xs[6] > 26473.510345:
								if xs[9] > 31979.309231:
									return ["1"]
								else: 
									if xs[2] > 387570.0:
										return ["1"]
									else: 
										return ["0"]
							else: 
								if xs[4] > 18696.0:
									return ["1"]
								else: 
									return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[11] > 200.0:
						if xs[9] > 11770.021667:
							return ["1"]
						else: 
							if xs[6] > 11337.319231:
								return ["0"]
							else: 
								return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[3] > 5.88:
					return ["0"]
				else: 
					if xs[4] > 1099.0:
						if xs[3] > 0.43:
							if xs[7] > 21755.1:
								if xs[11] > 2214.6:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["1"]
						else: 
							if xs[8] > 900.0:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["0"]
		else: 
			if xs[4] > 1913.0:
				if xs[8] > 52.4:
					if xs[3] > 4.48:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["1"]
			else: 
				return ["1"]
	else: 
		if xs[6] > 34316.46:
			return ["0"]
		else: 
			return ["1"]


# Model 23
def tree_23(xs):
	if xs[8] > 6.4:
		if xs[11] > 300.0:
			if xs[9] > 13387.8875:
				if xs[9] > 47217.891667:
					if xs[11] > 3823.0:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[10] > 164414.6:
						return ["1"]
					else: 
						if xs[2] > 228848.0:
							if xs[0] > 61.0:
								return ["1"]
							else: 
								if xs[8] > 53.1:
									return ["1"]
								else: 
									return ["0"]
						else: 
							return ["1"]
			else: 
				if xs[3] > 0.59:
					if xs[8] > 500.0:
						return ["1"]
					else: 
						if xs[6] > 13851.956667:
							return ["0"]
						else: 
							if xs[7] > 22519.6:
								if xs[6] > 10962.066667:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["1"]
				else: 
					return ["0"]
		else: 
			if xs[12] == 'Y':
				if xs[2] > 387570.0:
					return ["1"]
				else: 
					if xs[5] == 'WEEKLY ISSUANCE':
						if xs[0] > 43.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[6] > 11694.359259:
							return ["0"]
						else: 
							return ["1"]
			else: 
				return ["1"]
	else: 
		return ["0"]


# Model 24
def tree_24(xs):
	if xs[10] > 17114.6:
		if xs[11] > 30.0:
			if xs[3] > 4.72:
				if xs[10] > 28382.0:
					if xs[12] == 'Y':
						if xs[11] > 600.0:
							if xs[6] > 35966.3:
								if xs[8] > 53.1:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
					else: 
						return ["1"]
				else: 
					if xs[0] > 44.0:
						return ["0"]
					else: 
						return ["1"]
			else: 
				if xs[8] > 37.9:
					if xs[0] > 61.0:
						if xs[0] > 62.0:
							return ["1"]
						else: 
							if xs[10] > 85253.6:
								return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[4] > 6295.0:
							if xs[8] > 132.2:
								return ["1"]
							else: 
								if xs[6] > 21474.115:
									return ["1"]
								else: 
									return ["0"]
						else: 
							if xs[4] > 1879.0:
								return ["1"]
							else: 
								if xs[6] > 15725.233871:
									return ["1"]
								else: 
									if xs[10] > 30690.6:
										if xs[4] > 1127.0:
											return ["0"]
										else: 
											return ["1"]
									else: 
										return ["1"]
				else: 
					if xs[6] > 29237.011765:
						return ["1"]
					else: 
						return ["0"]
		else: 
			if xs[10] > 135950.4:
				return ["1"]
			else: 
				if xs[9] > 29988.672222:
					return ["1"]
				else: 
					return ["0"]
	else: 
		if xs[4] > 1099.0:
			return ["1"]
		else: 
			return ["0"]


# Model 25
def tree_25(xs):
	if xs[11] > 51.2:
		if xs[11] > 7500.0:
			return ["1"]
		else: 
			if xs[9] > 46901.890909:
				return ["1"]
			else: 
				if xs[8] > 19.7:
					if xs[6] > 25294.125806:
						return ["1"]
					else: 
						if xs[11] > 7010.6:
							if xs[11] > 7100.0:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[7] > 102988.4:
								return ["1"]
							else: 
								if xs[1] == 'M':
									if xs[5] == 'ISSUANCE AFTER TRANSACTION':
										return ["0"]
									else: 
										if xs[7] > 29977.9:
											return ["1"]
										else: 
											if xs[4] > 1668.0:
												return ["1"]
											else: 
												if xs[3] > 2.01:
													return ["0"]
												else: 
													return ["1"]
								else: 
									return ["1"]
				else: 
					return ["0"]
	else: 
		if xs[2] > 75232.0:
			if xs[9] > 31979.309231:
				return ["1"]
			else: 
				if xs[7] > 173693.5:
					return ["1"]
				else: 
					if xs[9] > 31745.223881:
						return ["0"]
					else: 
						if xs[0] > 38.0:
							return ["0"]
						else: 
							if xs[1] == 'M':
								if xs[2] > 127369.0:
									return ["0"]
								else: 
									return ["1"]
							else: 
								return ["1"]
		else: 
			return ["0"]


