# Python code of the trees in the ensemble

# Model 1
def tree_1(xs):
	if xs[2] > 42821.0:
		if xs[11] > 41.2:
			if xs[7] > 187234.4:
				if xs[7] > 192183.2:
					return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[6] > 52208.005:
					if xs[7] > 74170.5:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[11] > 300.0:
						if xs[8] > 37.9:
							if xs[9] > 11988.620896:
								if xs[10] > 39881.6:
									return ["1"]
								else: 
									if xs[10] > 39390.0:
										return ["0"]
									else: 
										return ["1"]
							else: 
								if xs[10] > 35594.6:
									return ["0"]
								else: 
									if xs[6] > 10241.298305:
										if xs[10] > 19449.6:
											return ["0"]
										else: 
											return ["1"]
									else: 
										return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[10] > 100079.8:
							return ["1"]
						else: 
							if xs[7] > 39738.7:
								return ["0"]
							else: 
								return ["1"]
		else: 
			if xs[8] > 16.0:
				if xs[2] > 51428.0:
					if xs[3] > 0.59:
						if xs[4] > 9208.0:
							return ["0"]
						else: 
							if xs[4] > 4265.0:
								return ["0"]
							else: 
								return ["1"]
					else: 
						return ["1"]
				else: 
					return ["0"]
			else: 
				return ["0"]
	else: 
		if xs[1] == 'M':
			return ["0"]
		else: 
			return ["1"]


# Model 2
def tree_2(xs):
	if xs[11] > 41.2:
		if xs[2] > 42821.0:
			if xs[10] > 178391.3:
				if xs[3] > 4.98:
					return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[11] > 200.0:
					if xs[0] > 59.0:
						return ["1"]
					else: 
						if xs[10] > 25074.6:
							return ["1"]
						else: 
							if xs[9] > 11491.064:
								if xs[7] > 19307.4:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["1"]
				else: 
					return ["1"]
		else: 
			if xs[7] > 23346.7:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[9] > 30801.79375:
			return ["1"]
		else: 
			if xs[4] > 18696.0:
				return ["1"]
			else: 
				if xs[8] > 30.5:
					if xs[3] > 3.98:
						if xs[0] > 27.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]


# Model 3
def tree_3(xs):
	if xs[8] > 16.0:
		if xs[11] > 200.0:
			if xs[3] > 5.74:
				return ["1"]
			else: 
				if xs[0] > 59.0:
					if xs[10] > 93914.6:
						return ["0"]
					else: 
						return ["1"]
				else: 
					if xs[8] > 37.9:
						if xs[6] > 17816.08:
							return ["1"]
						else: 
							if xs[6] > 17553.396:
								return ["0"]
							else: 
								if xs[6] > 16522.961111:
									return ["1"]
								else: 
									if xs[3] > 0.59:
										if xs[6] > 15607.443056:
											if xs[3] > 2.01:
												if xs[4] > 1181.0:
													return ["0"]
												else: 
													return ["1"]
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
			if xs[9] > 19195.234286:
				return ["1"]
			else: 
				if xs[7] > 89842.5:
					return ["0"]
				else: 
					if xs[4] > 2305.0:
						if xs[4] > 4433.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["0"]
	else: 
		return ["0"]


# Model 4
def tree_4(xs):
	if xs[8] > 30.5:
		if xs[11] > 30.0:
			if xs[4] > 9208.0:
				if xs[7] > 154222.0:
					return ["0"]
				else: 
					if xs[6] > 52208.005:
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
					return ["1"]
		else: 
			if xs[12] == 'Y':
				if xs[6] > 28598.256:
					if xs[8] > 78.1:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
			else: 
				return ["1"]
	else: 
		return ["0"]


# Model 5
def tree_5(xs):
	if xs[2] > 42821.0:
		if xs[9] > 30801.79375:
			return ["1"]
		else: 
			if xs[11] > 200.0:
				if xs[8] > 53.1:
					if xs[3] > 7.68:
						if xs[0] > 50.0:
							if xs[7] > 21354.4:
								return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[11] > 300.0:
							if xs[6] > 17816.08:
								return ["1"]
							else: 
								if xs[8] > 14966.0:
									return ["0"]
								else: 
									if xs[6] > 17786.444118:
										return ["0"]
									else: 
										return ["1"]
						else: 
							return ["1"]
				else: 
					return ["1"]
			else: 
				if xs[7] > 85474.8:
					if xs[2] > 75637.0:
						if xs[9] > 25445.998551:
							if xs[7] > 137783.3:
								return ["0"]
							else: 
								if xs[3] > 4.48:
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
		if xs[6] > 16488.234884:
			return ["1"]
		else: 
			return ["0"]


# Model 6
def tree_6(xs):
	if xs[11] > 51.2:
		if xs[8] > 37.9:
			if xs[2] > 42821.0:
				if xs[3] > 2.07:
					return ["1"]
				else: 
					if xs[3] > 1.86:
						if xs[7] > 121322.9:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
			else: 
				return ["1"]
		else: 
			if xs[6] > 31833.5:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[6] > 38230.030556:
			return ["1"]
		else: 
			if xs[4] > 2305.0:
				if xs[3] > 5.56:
					return ["1"]
				else: 
					if xs[3] > 0.43:
						if xs[0] > 38.0:
							return ["0"]
						else: 
							if xs[8] > 49.1:
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
			if xs[8] > 12.1:
				if xs[2] > 42821.0:
					if xs[2] > 45714.0:
						if xs[0] > 21.0:
							if xs[12] == 'Y':
								if xs[11] > 129.3:
									if xs[9] > 13387.8875:
										if xs[10] > 145955.0:
											if xs[3] > 1.96:
												return ["1"]
											else: 
												if xs[0] > 40.0:
													return ["0"]
												else: 
													return ["1"]
										else: 
											if xs[0] > 22.0:
												if xs[7] > 21354.4:
													if xs[11] > 300.0:
														if xs[8] > 37.9:
															return ["1"]
														else: 
															if xs[7] > 88371.6:
																return ["0"]
															else: 
																return ["1"]
													else: 
														if xs[3] > 4.02:
															return ["0"]
														else: 
															return ["1"]
												else: 
													return ["1"]
											else: 
												return ["1"]
									else: 
										if xs[6] > 14365.110526:
											return ["0"]
										else: 
											if xs[2] > 75637.0:
												if xs[11] > 1200.0:
													return ["1"]
												else: 
													return ["0"]
											else: 
												if xs[4] > 2813.0:
													return ["0"]
												else: 
													return ["1"]
								else: 
									if xs[6] > 26473.510345:
										if xs[3] > 5.05:
											return ["1"]
										else: 
											if xs[3] > 0.43:
												if xs[5] == 'MONTHLY ISSUANCE':
													return ["0"]
												else: 
													return ["1"]
											else: 
												return ["1"]
									else: 
										return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
					else: 
						if xs[8] > 117.3:
							return ["1"]
						else: 
							return ["0"]
				else: 
					return ["0"]
			else: 
				return ["0"]
	else: 
		if xs[0] > 24.0:
			return ["1"]
		else: 
			return ["0"]


# Model 8
def tree_8(xs):
	if xs[4] > 888.0:
		if xs[0] > 62.0:
			return ["1"]
		else: 
			if xs[10] > 100000.0:
				if xs[10] > 102514.6:
					if xs[8] > 16.0:
						if xs[11] > 30.0:
							if xs[3] > 1.44:
								return ["1"]
							else: 
								if xs[7] > 74170.5:
									return ["1"]
								else: 
									return ["0"]
						else: 
							if xs[9] > 31979.309231:
								return ["1"]
							else: 
								if xs[2] > 110643.0:
									if xs[1] == 'M':
										return ["0"]
									else: 
										if xs[3] > 4.79:
											return ["0"]
										else: 
											return ["1"]
								else: 
									return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
			else: 
				if xs[8] > 19.5:
					if xs[6] > 29237.011765:
						return ["1"]
					else: 
						if xs[7] > 114939.7:
							if xs[1] == 'M':
								return ["0"]
							else: 
								return ["1"]
						else: 
							if xs[10] > 70543.0:
								if xs[11] > 300.0:
									return ["1"]
								else: 
									if xs[4] > 2252.0:
										return ["1"]
									else: 
										return ["0"]
							else: 
								if xs[4] > 1358.0:
									if xs[11] > 7100.0:
										return ["1"]
									else: 
										if xs[7] > 25690.6:
											return ["1"]
										else: 
											if xs[6] > 17451.023077:
												return ["0"]
											else: 
												if xs[3] > 0.59:
													return ["1"]
												else: 
													if xs[0] > 30.0:
														return ["1"]
													else: 
														return ["0"]
								else: 
									return ["1"]
				else: 
					return ["0"]
	else: 
		return ["0"]


# Model 9
def tree_9(xs):
	if xs[8] > 22.3:
		if xs[11] > 30.0:
			if xs[12] == 'Y':
				if xs[0] > 58.0:
					if xs[6] > 17685.511111:
						return ["1"]
					else: 
						if xs[8] > 10741.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[9] > 49229.107143:
						if xs[0] > 37.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[8] > 37.9:
							if xs[3] > 6.55:
								if xs[0] > 48.0:
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
			if xs[9] > 29764.414085:
				return ["1"]
			else: 
				if xs[10] > 83714.6:
					return ["0"]
				else: 
					return ["1"]
	else: 
		return ["0"]


# Model 10
def tree_10(xs):
	if xs[4] > 888.0:
		if xs[2] > 42821.0:
			if xs[11] > 30.0:
				if xs[11] > 200.0:
					if xs[9] > 49726.144444:
						if xs[7] > 79110.5:
							return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[7] > 187234.4:
							if xs[1] == 'M':
								return ["1"]
							else: 
								if xs[0] > 29.0:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[0] > 58.0:
								if xs[0] > 59.0:
									return ["1"]
								else: 
									if xs[6] > 17685.511111:
										return ["1"]
									else: 
										return ["0"]
							else: 
								if xs[8] > 37.9:
									if xs[7] > 24825.8:
										return ["1"]
									else: 
										if xs[7] > 24789.4:
											return ["0"]
										else: 
											if xs[4] > 3198.0:
												if xs[2] > 75637.0:
													return ["1"]
												else: 
													return ["0"]
											else: 
												return ["1"]
								else: 
									return ["0"]
				else: 
					if xs[9] > 17576.35:
						return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[3] > 0.59:
					if xs[3] > 2.21:
						if xs[8] > 129.9:
							return ["1"]
						else: 
							if xs[3] > 5.05:
								return ["1"]
							else: 
								return ["0"]
					else: 
						return ["0"]
				else: 
					return ["1"]
		else: 
			if xs[7] > 23346.7:
				return ["1"]
			else: 
				return ["0"]
	else: 
		return ["0"]


