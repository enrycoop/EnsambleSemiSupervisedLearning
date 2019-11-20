# Python code of the trees in the ensemble

# Model 1
def tree_1(xs):
	if xs[6] > 44744.189286:
		return ["1"]
	else: 
		if xs[7] > 60815.0:
			if xs[7] > 63374.3:
				if xs[2] > 323870.0:
					if xs[8] > 83.1:
						return ["0"]
					else: 
						if xs[7] > 101117.1:
							if xs[11] > 37.0:
								return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[11] > 300.0:
						if xs[8] > 15.5:
							return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[8] > 129.9:
							return ["1"]
						else: 
							if xs[12] == 'Y':
								return ["0"]
							else: 
								return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[9] > 12468.285484:
				if xs[7] > 22564.4:
					return ["1"]
				else: 
					if xs[6] > 16436.096774:
						return ["0"]
					else: 
						return ["1"]
			else: 
				if xs[10] > 41334.6:
					return ["0"]
				else: 
					if xs[6] > 14852.536:
						return ["0"]
					else: 
						if xs[11] > 14.6:
							return ["1"]
						else: 
							if xs[0] > 24.0:
								return ["1"]
							else: 
								return ["0"]


# Model 2
def tree_2(xs):
	if xs[11] > 37.0:
		if xs[2] > 70646.0:
			if xs[12] == 'Y':
				if xs[8] > 53.1:
					if xs[10] > 145258.0:
						if xs[3] > 4.02:
							return ["1"]
						else: 
							if xs[8] > 208.5:
								return ["0"]
							else: 
								return ["1"]
					else: 
						return ["1"]
				else: 
					if xs[10] > 96391.4:
						if xs[6] > 38229.233333:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[10] > 147035.0:
				if xs[9] > 34060.754545:
					return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[8] > 200.0:
					return ["1"]
				else: 
					if xs[4] > 1358.0:
						return ["0"]
					else: 
						return ["1"]
	else: 
		if xs[9] > 31979.309231:
			return ["1"]
		else: 
			if xs[3] > 0.59:
				if xs[3] > 3.98:
					if xs[0] > 27.0:
						if xs[3] > 5.44:
							return ["0"]
						else: 
							if xs[0] > 35.0:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["1"]
				else: 
					return ["0"]
			else: 
				return ["1"]


# Model 3
def tree_3(xs):
	if xs[8] > 37.9:
		if xs[11] > 30.0:
			if xs[10] > 147035.0:
				if xs[8] > 200.0:
					if xs[3] > 4.02:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[2] > 109164.0:
					if xs[8] > 63.2:
						if xs[11] > 300.0:
							if xs[5] == 'ISSUANCE AFTER TRANSACTION':
								if xs[0] > 42.0:
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
					return ["1"]
		else: 
			if xs[6] > 35062.811111:
				return ["1"]
			else: 
				if xs[0] > 52.0:
					return ["0"]
				else: 
					if xs[9] > 24957.4:
						return ["0"]
					else: 
						if xs[4] > 3868.0:
							if xs[1] == 'M':
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
	else: 
		return ["0"]


# Model 4
def tree_4(xs):
	if xs[8] > 6.4:
		if xs[11] > 37.0:
			if xs[4] > 18347.0:
				if xs[6] > 11393.674286:
					if xs[0] > 22.0:
						if xs[11] > 300.0:
							return ["1"]
						else: 
							if xs[0] > 35.0:
								return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[0] > 21.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[9] > 11561.647619:
					if xs[3] > 5.72:
						if xs[2] > 85852.0:
							if xs[2] > 106054.0:
								if xs[6] > 36083.868116:
									return ["0"]
								else: 
									return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
				else: 
					if xs[1] == 'M':
						if xs[9] > 10010.130435:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
		else: 
			if xs[9] > 28472.625532:
				return ["1"]
			else: 
				if xs[3] > 3.98:
					return ["1"]
				else: 
					if xs[2] > 387570.0:
						return ["1"]
					else: 
						if xs[7] > 141652.9:
							return ["1"]
						else: 
							return ["0"]
	else: 
		return ["0"]


# Model 5
def tree_5(xs):
	if xs[2] > 70646.0:
		if xs[7] > 77824.6:
			if xs[11] > 14.6:
				if xs[0] > 61.0:
					return ["1"]
				else: 
					if xs[7] > 79110.5:
						if xs[8] > 63.2:
							return ["1"]
						else: 
							if xs[10] > 96391.4:
								return ["1"]
							else: 
								if xs[8] > 20.4:
									return ["0"]
								else: 
									return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[9] > 22014.64375:
					if xs[9] > 28472.625532:
						return ["1"]
					else: 
						if xs[3] > 0.43:
							return ["0"]
						else: 
							return ["1"]
				else: 
					return ["0"]
		else: 
			if xs[1] == 'M':
				if xs[7] > 27304.7:
					return ["1"]
				else: 
					if xs[6] > 10292.630435:
						if xs[4] > 5410.0:
							return ["0"]
						else: 
							if xs[6] > 10963.049231:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["1"]
			else: 
				return ["1"]
	else: 
		if xs[2] > 67298.0:
			return ["0"]
		else: 
			if xs[7] > 172864.2:
				return ["0"]
			else: 
				if xs[6] > 26498.476923:
					return ["1"]
				else: 
					if xs[8] > 117.3:
						if xs[2] > 58796.0:
							return ["1"]
						else: 
							if xs[6] > 15725.233871:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["0"]


# Model 6
def tree_6(xs):
	if xs[11] > 51.2:
		if xs[8] > 37.9:
			if xs[10] > 145258.0:
				if xs[8] > 200.0:
					if xs[3] > 4.02:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[11] > 2214.6:
					if xs[7] > 157969.7:
						if xs[9] > 33680.003125:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
				else: 
					if xs[3] > 2.31:
						if xs[11] > 2200.0:
							return ["0"]
						else: 
							if xs[3] > 2.43:
								if xs[4] > 2252.0:
									return ["1"]
								else: 
									if xs[8] > 80.7:
										return ["1"]
									else: 
										return ["0"]
							else: 
								return ["0"]
					else: 
						return ["1"]
		else: 
			if xs[8] > 20.4:
				return ["0"]
			else: 
				return ["1"]
	else: 
		if xs[6] > 35062.811111:
			return ["1"]
		else: 
			if xs[2] > 75232.0:
				if xs[2] > 107870.0:
					if xs[0] > 22.0:
						if xs[10] > 115914.6:
							if xs[4] > 18347.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
			else: 
				return ["0"]


# Model 7
def tree_7(xs):
	if xs[6] > 35062.811111:
		if xs[10] > 95414.0:
			if xs[10] > 96614.6:
				if xs[9] > 43368.87931:
					if xs[3] > 3.97:
						if xs[9] > 50462.202778:
							return ["1"]
						else: 
							if xs[7] > 74490.7:
								if xs[4] > 3120.0:
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
				return ["1"]
		else: 
			return ["1"]
	else: 
		if xs[11] > 51.2:
			if xs[4] > 1879.0:
				if xs[7] > 22564.4:
					return ["1"]
				else: 
					if xs[9] > 15140.064151:
						return ["0"]
					else: 
						if xs[1] == 'M':
							if xs[3] > 2.26:
								if xs[3] > 4.98:
									return ["1"]
								else: 
									if xs[2] > 124605.0:
										return ["1"]
									else: 
										return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
			else: 
				if xs[8] > 80.7:
					if xs[4] > 1875.0:
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["0"]
		else: 
			if xs[3] > 3.98:
				if xs[4] > 9208.0:
					return ["1"]
				else: 
					if xs[0] > 27.0:
						if xs[9] > 12338.8125:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
			else: 
				return ["0"]


# Model 8
def tree_8(xs):
	if xs[0] > 62.0:
		return ["0"]
	else: 
		if xs[10] > 23768.6:
			if xs[10] > 23999.6:
				if xs[8] > 16.0:
					if xs[7] > 17653.3:
						if xs[5] == 'ISSUANCE AFTER TRANSACTION':
							if xs[7] > 94885.4:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[9] > 11770.021667:
								if xs[8] > 53.1:
									if xs[10] > 75030.0:
										if xs[6] > 21627.159375:
											if xs[6] > 35062.811111:
												return ["1"]
											else: 
												if xs[11] > 14.6:
													return ["1"]
												else: 
													if xs[0] > 27.0:
														return ["0"]
													else: 
														return ["1"]
										else: 
											return ["1"]
									else: 
										return ["1"]
								else: 
									if xs[9] > 28739.808824:
										return ["1"]
									else: 
										return ["0"]
							else: 
								if xs[2] > 162580.0:
									if xs[6] > 11483.972059:
										return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
					else: 
						if xs[0] > 30.0:
							return ["1"]
						else: 
							return ["0"]
				else: 
					return ["0"]
			else: 
				return ["0"]
		else: 
			return ["1"]


# Model 9
def tree_9(xs):
	if xs[8] > 16.0:
		if xs[11] > 30.0:
			if xs[12] == 'Y':
				if xs[0] > 59.0:
					if xs[6] > 25442.532857:
						return ["0"]
					else: 
						return ["1"]
				else: 
					if xs[0] > 22.0:
						if xs[8] > 53.1:
							if xs[2] > 58796.0:
								if xs[9] > 49361.25:
									if xs[10] > 124714.6:
										return ["1"]
									else: 
										return ["0"]
								else: 
									if xs[6] > 25294.125806:
										return ["1"]
									else: 
										if xs[5] == 'ISSUANCE AFTER TRANSACTION':
											return ["0"]
										else: 
											if xs[0] > 56.0:
												return ["1"]
											else: 
												if xs[9] > 23143.925:
													return ["1"]
												else: 
													if xs[0] > 48.0:
														if xs[3] > 4.5:
															if xs[11] > 2300.0:
																return ["1"]
															else: 
																return ["0"]
														else: 
															return ["1"]
													else: 
														return ["1"]
							else: 
								if xs[9] > 11770.021667:
									return ["1"]
								else: 
									return ["0"]
						else: 
							if xs[3] > 2.31:
								return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[7] > 137137.3:
							return ["0"]
						else: 
							if xs[11] > 2316.6:
								if xs[3] > 2.5:
									return ["0"]
								else: 
									if xs[9] > 17707.549206:
										return ["1"]
									else: 
										if xs[1] == 'M':
											return ["1"]
										else: 
											return ["0"]
							else: 
								return ["1"]
			else: 
				return ["1"]
		else: 
			if xs[10] > 135950.4:
				return ["1"]
			else: 
				if xs[0] > 23.0:
					if xs[3] > 0.43:
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
	else: 
		return ["0"]


# Model 10
def tree_10(xs):
	if xs[4] > 888.0:
		if xs[5] == 'ISSUANCE AFTER TRANSACTION':
			return ["1"]
		else: 
			if xs[11] > 30.0:
				if xs[6] > 11393.674286:
					if xs[11] > 8300.0:
						return ["1"]
					else: 
						if xs[4] > 1117.0:
							if xs[2] > 58796.0:
								if xs[4] > 9208.0:
									return ["1"]
								else: 
									if xs[11] > 8000.0:
										return ["1"]
									else: 
										if xs[8] > 37.9:
											return ["1"]
										else: 
											if xs[8] > 17.1:
												return ["0"]
											else: 
												return ["1"]
							else: 
								if xs[2] > 53921.0:
									return ["0"]
								else: 
									return ["1"]
						else: 
							return ["1"]
				else: 
					if xs[10] > 22480.6:
						if xs[2] > 105058.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
			else: 
				if xs[4] > 2305.0:
					if xs[10] > 123814.6:
						return ["1"]
					else: 
						if xs[3] > 5.56:
							return ["1"]
						else: 
							if xs[6] > 20922.705455:
								return ["0"]
							else: 
								return ["1"]
				else: 
					return ["0"]
	else: 
		return ["0"]


