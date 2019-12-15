# Python code of the trees in the ensemble

# Model 1
def tree_1(xs):
	if xs[7] > 70609.8:
		if xs[7] > 70717.5:
			if xs[10] > 166430.0:
				return ["1"]
			else: 
				if xs[8] > 35.5:
					if xs[3] > 8.23:
						return ["1"]
					else: 
						if xs[6] > 17441.124:
							if xs[5] == 'ISSUANCE AFTER TRANSACTION':
								return ["1"]
							else: 
								if xs[9] > 16011.016216:
									if xs[8] > 43.3:
										if xs[8] > 52.4:
											if xs[0] > 58.0:
												if xs[9] > 40655.753333:
													return ["1"]
												else: 
													if xs[11] > 1814.6:
														return ["1"]
													else: 
														if xs[3] > 0.43:
															return ["0"]
														else: 
															return ["1"]
											else: 
												if xs[4] > 10108.0:
													if xs[0] > 22.0:
														return ["1"]
													else: 
														if xs[0] > 18.0:
															if xs[6] > 38351.69697:
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
									return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[11] > 129.0:
						if xs[11] > 300.0:
							if xs[8] > 15.8:
								if xs[3] > 3.74:
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
	else: 
		if xs[9] > 13355.055556:
			if xs[3] > 6.55:
				if xs[7] > 23346.7:
					return ["1"]
				else: 
					if xs[11] > 5300.0:
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["1"]
		else: 
			return ["1"]


# Model 2
def tree_2(xs):
	if xs[8] > 1.0:
		if xs[10] > 77669.6:
			if xs[0] > 21.0:
				if xs[10] > 77798.8:
					if xs[8] > 35.5:
						if xs[2] > 285387.0:
							if xs[0] > 22.0:
								if xs[5] == 'MONTHLY ISSUANCE':
									if xs[0] > 60.0:
										return ["0"]
									else: 
										if xs[8] > 210.3:
											if xs[7] > 74422.9:
												if xs[6] > 40609.5:
													if xs[3] > 0.43:
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
								if xs[11] > 2700.0:
									return ["0"]
								else: 
									if xs[2] > 323870.0:
										return ["1"]
									else: 
										return ["0"]
						else: 
							if xs[9] > 16011.016216:
								if xs[0] > 26.0:
									if xs[9] > 50066.470588:
										if xs[2] > 125236.0:
											return ["1"]
										else: 
											return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[6] > 32449.724615:
										return ["1"]
									else: 
										if xs[2] > 125236.0:
											return ["1"]
										else: 
											return ["0"]
							else: 
								return ["0"]
					else: 
						return ["0"]
				else: 
					return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[7] > 82406.6:
				return ["1"]
			else: 
				if xs[6] > 30673.52:
					if xs[6] > 30954.12963:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[7] > 19241.0:
						if xs[6] > 11192.512903:
							if xs[7] > 19307.4:
								if xs[3] > 7.68:
									if xs[10] > 27502.6:
										return ["1"]
									else: 
										if xs[0] > 45.0:
											return ["1"]
										else: 
											return ["0"]
								else: 
									if xs[0] > 58.0:
										if xs[4] > 2354.0:
											return ["1"]
										else: 
											if xs[8] > 14395.0:
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
		return ["0"]


# Model 3
def tree_3(xs):
	if xs[2] > 42821.0:
		if xs[8] > 1.0:
			if xs[8] > 37.9:
				if xs[9] > 50066.470588:
					if xs[9] > 50462.202778:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[7] > 101117.1:
						if xs[0] > 58.0:
							if xs[3] > 3.49:
								return ["0"]
							else: 
								if xs[10] > 146830.0:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[10] > 77798.8:
								if xs[2] > 51313.0:
									return ["1"]
								else: 
									if xs[7] > 101744.8:
										return ["1"]
									else: 
										return ["0"]
							else: 
								return ["1"]
					else: 
						return ["1"]
			else: 
				if xs[0] > 59.0:
					return ["1"]
				else: 
					if xs[3] > 1.25:
						return ["0"]
					else: 
						if xs[8] > 13.5:
							if xs[10] > 115914.6:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["0"]
		else: 
			return ["0"]
	else: 
		return ["0"]


# Model 4
def tree_4(xs):
	if xs[8] > 1.0:
		if xs[8] > 16.0:
			if xs[7] > 101117.1:
				if xs[7] > 101744.8:
					if xs[0] > 62.0:
						return ["0"]
					else: 
						if xs[8] > 37.9:
							if xs[8] > 43.7:
								if xs[8] > 136.0:
									if xs[0] > 22.0:
										return ["1"]
									else: 
										if xs[4] > 6132.0:
											if xs[7] > 126435.8:
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
							if xs[4] > 4505.0:
								return ["1"]
							else: 
								return ["0"]
				else: 
					return ["0"]
			else: 
				if xs[9] > 11264.191304:
					if xs[9] > 11321.55:
						if xs[10] > 24520.6:
							if xs[7] > 23365.3:
								return ["1"]
							else: 
								if xs[7] > 23338.6:
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
			if xs[9] > 35926.595:
				return ["1"]
			else: 
				return ["0"]
	else: 
		return ["0"]


# Model 5
def tree_5(xs):
	if xs[10] > 97014.6:
		if xs[11] > 100.0:
			if xs[9] > 49726.144444:
				if xs[9] > 50462.202778:
					return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[6] > 38821.082979:
					if xs[9] > 33680.003125:
						if xs[8] > 21.6:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
		else: 
			if xs[8] > 150.6:
				return ["1"]
			else: 
				if xs[3] > 0.59:
					if xs[12] == 'Y':
						return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
	else: 
		if xs[6] > 12019.9:
			if xs[11] > 14.6:
				if xs[10] > 24520.6:
					if xs[7] > 112762.0:
						if xs[8] > 37.9:
							return ["1"]
						else: 
							if xs[0] > 29.0:
								return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[4] > 2471.0:
							return ["1"]
						else: 
							if xs[3] > 4.52:
								if xs[11] > 4506.6:
									return ["1"]
								else: 
									if xs[0] > 59.0:
										return ["0"]
									else: 
										return ["1"]
							else: 
								return ["1"]
				else: 
					if xs[10] > 24464.6:
						return ["0"]
					else: 
						return ["1"]
			else: 
				return ["0"]
		else: 
			return ["1"]


# Model 6
def tree_6(xs):
	if xs[7] > 161527.4:
		if xs[7] > 162345.4:
			if xs[0] > 49.0:
				if xs[0] > 53.0:
					return ["1"]
				else: 
					if xs[5] == 'ISSUANCE AFTER TRANSACTION':
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["1"]
		else: 
			return ["0"]
	else: 
		if xs[6] > 12019.9:
			if xs[6] > 12226.657895:
				if xs[10] > 24247.6:
					if xs[8] > 6.4:
						if xs[2] > 42821.0:
							if xs[0] > 58.0:
								if xs[10] > 120274.6:
									if xs[3] > 1.85:
										return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[9] > 17444.82093:
										return ["1"]
									else: 
										if xs[8] > 14483.6:
											return ["0"]
										else: 
											return ["1"]
							else: 
								if xs[9] > 11321.55:
									if xs[3] > 8.23:
										return ["1"]
									else: 
										if xs[10] > 24520.6:
											if xs[8] > 21.6:
												if xs[8] > 43.7:
													if xs[10] > 27502.6:
														if xs[9] > 49726.144444:
															return ["1"]
														else: 
															if xs[4] > 3529.0:
																return ["1"]
															else: 
																if xs[6] > 30481.898592:
																	if xs[10] > 60269.3:
																		return ["1"]
																	else: 
																		return ["0"]
																else: 
																	return ["1"]
													else: 
														if xs[2] > 226122.0:
															return ["0"]
														else: 
															return ["1"]
												else: 
													return ["1"]
											else: 
												if xs[7] > 127556.0:
													return ["1"]
												else: 
													return ["0"]
										else: 
											return ["1"]
								else: 
									if xs[10] > 29400.0:
										return ["1"]
									else: 
										if xs[0] > 46.0:
											return ["0"]
										else: 
											return ["1"]
						else: 
							if xs[8] > 200.0:
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
			return ["1"]


# Model 7
def tree_7(xs):
	if xs[10] > 77669.6:
		if xs[6] > 21785.407843:
			if xs[8] > 0.5:
				if xs[8] > 21.7:
					if xs[0] > 61.0:
						if xs[11] > 7000.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[7] > 106179.4:
							return ["1"]
						else: 
							if xs[8] > 77.7:
								if xs[4] > 4846.0:
									if xs[11] > 7521.0:
										if xs[5] == 'MONTHLY ISSUANCE':
											if xs[9] > 44952.554286:
												if xs[4] > 18347.0:
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
					if xs[8] > 15.8:
						if xs[4] > 4433.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[11] > 1000.0:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[7] > 112762.0:
			return ["1"]
		else: 
			if xs[7] > 82587.6:
				return ["1"]
			else: 
				if xs[2] > 285387.0:
					return ["1"]
				else: 
					if xs[7] > 20617.1:
						if xs[0] > 59.0:
							if xs[4] > 5887.0:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[4] > 6872.0:
								if xs[11] > 2214.6:
									return ["1"]
								else: 
									return ["0"]
							else: 
								if xs[10] > 60230.0:
									if xs[9] > 27558.555556:
										if xs[7] > 43571.7:
											return ["1"]
										else: 
											return ["0"]
									else: 
										return ["1"]
								else: 
									return ["1"]
					else: 
						return ["1"]


# Model 8
def tree_8(xs):
	if xs[7] > 74153.1:
		if xs[0] > 63.0:
			return ["1"]
		else: 
			if xs[9] > 16732.980328:
				if xs[9] > 21182.56:
					if xs[9] > 21182.88:
						if xs[6] > 32798.893443:
							if xs[8] > 30.5:
								if xs[8] > 279.2:
									if xs[9] > 49132.523077:
										if xs[0] > 23.0:
											return ["0"]
										else: 
											return ["1"]
									else: 
										return ["1"]
								else: 
									return ["1"]
							else: 
								if xs[0] > 29.0:
									return ["0"]
								else: 
									if xs[7] > 137137.3:
										return ["0"]
									else: 
										return ["1"]
						else: 
							if xs[11] > 57.5:
								if xs[9] > 21446.354545:
									if xs[10] > 60800.0:
										return ["1"]
									else: 
										return ["0"]
								else: 
									return ["1"]
							else: 
								if xs[12] == 'Y':
									return ["0"]
								else: 
									if xs[0] > 26.0:
										return ["1"]
									else: 
										return ["0"]
					else: 
						return ["0"]
				else: 
					return ["1"]
			else: 
				if xs[9] > 14846.113043:
					if xs[7] > 101309.0:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
	else: 
		if xs[9] > 9192.260606:
			if xs[9] > 9215.375:
				if xs[2] > 42821.0:
					if xs[0] > 39.0:
						if xs[11] > 734.6:
							if xs[3] > 7.68:
								if xs[7] > 21277.3:
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
				return ["0"]
		else: 
			return ["1"]


# Model 9
def tree_9(xs):
	if xs[10] > 89214.6:
		if xs[9] > 16732.980328:
			if xs[10] > 90301.6:
				if xs[8] > 0.5:
					if xs[9] > 22767.237255:
						if xs[8] > 30.5:
							return ["1"]
						else: 
							if xs[2] > 133777.0:
								return ["0"]
							else: 
								if xs[11] > 2100.0:
									return ["1"]
								else: 
									return ["0"]
					else: 
						return ["0"]
				else: 
					return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[5] == 'ISSUANCE AFTER TRANSACTION':
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[7] > 21002.5:
			if xs[7] > 21277.3:
				if xs[8] > 20.4:
					if xs[8] > 300.0:
						return ["1"]
					else: 
						if xs[6] > 30508.665385:
							if xs[6] > 30954.12963:
								return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
				else: 
					return ["1"]
			else: 
				if xs[0] > 53.0:
					return ["1"]
				else: 
					if xs[3] > 5.66:
						return ["0"]
					else: 
						return ["1"]
		else: 
			return ["1"]


# Model 10
def tree_10(xs):
	if xs[10] > 59989.6:
		if xs[10] > 60269.3:
			if xs[2] > 42821.0:
				if xs[6] > 16568.382813:
					if xs[8] > 21.7:
						if xs[9] > 16732.980328:
							if xs[11] > 14.6:
								if xs[0] > 58.0:
									if xs[1] == 'M':
										if xs[11] > 1814.6:
											return ["1"]
										else: 
											return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[0] > 50.0:
										return ["1"]
									else: 
										if xs[6] > 52099.760714:
											if xs[6] > 52828.943243:
												return ["1"]
											else: 
												if xs[12] == 'Y':
													if xs[11] > 8214.8:
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
							if xs[3] > 2.66:
								return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[0] > 58.0:
							return ["1"]
						else: 
							return ["0"]
				else: 
					return ["1"]
			else: 
				return ["0"]
		else: 
			return ["0"]
	else: 
		return ["1"]


# Model 11
def tree_11(xs):
	if xs[8] > 1.0:
		if xs[9] > 46953.508108:
			if xs[9] > 47712.531034:
				if xs[7] > 79110.5:
					return ["1"]
				else: 
					if xs[0] > 38.0:
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[3] > 5.56:
				return ["1"]
			else: 
				if xs[8] > 19.7:
					if xs[0] > 62.0:
						return ["1"]
					else: 
						if xs[2] > 45714.0:
							if xs[8] > 43.7:
								if xs[0] > 61.0:
									if xs[10] > 85253.6:
										return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[3] > 5.44:
										if xs[0] > 59.0:
											return ["0"]
										else: 
											return ["1"]
									else: 
										if xs[7] > 154140.5:
											if xs[2] > 228848.0:
												if xs[8] > 118.6:
													return ["0"]
												else: 
													return ["1"]
											else: 
												return ["1"]
										else: 
											return ["1"]
							else: 
								if xs[10] > 70393.3:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[11] > 14.6:
								return ["1"]
							else: 
								return ["0"]
				else: 
					return ["0"]
	else: 
		return ["0"]


# Model 12
def tree_12(xs):
	if xs[8] > 1.0:
		if xs[7] > 138443.2:
			if xs[11] > 57.5:
				if xs[11] > 2100.0:
					return ["1"]
				else: 
					if xs[8] > 15.5:
						return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[9] > 29784.148718:
					if xs[2] > 387570.0:
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
		else: 
			if xs[10] > 135218.6:
				if xs[9] > 21382.92623:
					return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[8] > 6.4:
					if xs[8] > 19.5:
						if xs[6] > 12863.857143:
							if xs[11] > 1280.0:
								if xs[0] > 58.0:
									if xs[6] > 49782.267143:
										return ["1"]
									else: 
										if xs[8] > 14483.6:
											return ["0"]
										else: 
											return ["1"]
								else: 
									if xs[2] > 42821.0:
										if xs[2] > 77963.0:
											return ["1"]
										else: 
											if xs[4] > 2813.0:
												if xs[8] > 800.0:
													return ["0"]
												else: 
													if xs[3] > 0.59:
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
						return ["1"]
				else: 
					return ["0"]
	else: 
		return ["0"]


# Model 13
def tree_13(xs):
	if xs[7] > 73666.4:
		if xs[11] > 57.5:
			if xs[8] > 15.5:
				if xs[10] > 77798.8:
					return ["1"]
				else: 
					if xs[7] > 98908.7:
						if xs[2] > 110643.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
			else: 
				if xs[4] > 1117.0:
					return ["1"]
				else: 
					return ["0"]
		else: 
			if xs[3] > 0.59:
				return ["0"]
			else: 
				return ["1"]
	else: 
		if xs[10] > 28242.6:
			if xs[4] > 1358.0:
				return ["1"]
			else: 
				if xs[3] > 3.98:
					return ["0"]
				else: 
					return ["1"]
		else: 
			return ["1"]


# Model 14
def tree_14(xs):
	if xs[2] > 42821.0:
		if xs[8] > 0.5:
			if xs[6] > 26539.684375:
				if xs[6] > 26548.862162:
					if xs[8] > 35.5:
						if xs[2] > 285387.0:
							if xs[6] > 39379.355072:
								if xs[9] > 29988.672222:
									if xs[7] > 143125.5:
										if xs[10] > 135214.6:
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
							if xs[6] > 32575.573684:
								return ["1"]
							else: 
								if xs[8] > 300.0:
									return ["1"]
								else: 
									if xs[7] > 43571.7:
										if xs[0] > 26.0:
											return ["1"]
										else: 
											return ["0"]
									else: 
										return ["0"]
					else: 
						if xs[0] > 56.0:
							return ["1"]
						else: 
							if xs[7] > 88371.6:
								if xs[0] > 29.0:
									return ["0"]
								else: 
									if xs[10] > 89814.6:
										return ["0"]
									else: 
										return ["1"]
							else: 
								return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[10] > 96183.0:
					return ["1"]
				else: 
					if xs[9] > 9212.270588:
						if xs[8] > 1.0:
							if xs[8] > 15001.3:
								if xs[3] > 5.44:
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
			return ["0"]
	else: 
		if xs[6] > 38918.676:
			return ["1"]
		else: 
			return ["0"]


# Model 15
def tree_15(xs):
	if xs[9] > 9192.260606:
		if xs[8] > 1.0:
			if xs[8] > 24.1:
				if xs[10] > 77620.8:
					if xs[9] > 23436.696721:
						if xs[10] > 149330.0:
							return ["1"]
						else: 
							if xs[7] > 142530.1:
								if xs[8] > 43.7:
									if xs[2] > 323870.0:
										if xs[9] > 31745.223881:
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
						if xs[4] > 4743.0:
							return ["1"]
						else: 
							return ["0"]
				else: 
					if xs[0] > 58.0:
						if xs[2] > 103347.0:
							return ["1"]
						else: 
							if xs[2] > 93931.0:
								return ["0"]
							else: 
								return ["1"]
					else: 
						if xs[3] > 4.72:
							if xs[6] > 16234.575:
								return ["1"]
							else: 
								if xs[3] > 4.79:
									return ["1"]
								else: 
									return ["0"]
						else: 
							return ["1"]
			else: 
				if xs[8] > 20.1:
					if xs[5] == 'WEEKLY ISSUANCE':
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
		else: 
			return ["0"]
	else: 
		return ["1"]


# Model 16
def tree_16(xs):
	if xs[10] > 86661.0:
		if xs[9] > 16732.980328:
			if xs[8] > 0.4:
				if xs[8] > 35.5:
					if xs[2] > 285387.0:
						if xs[11] > 6009.0:
							if xs[4] > 18347.0:
								if xs[5] == 'MONTHLY ISSUANCE':
									if xs[0] > 22.0:
										return ["1"]
									else: 
										return ["0"]
								else: 
									return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[6] > 32628.212903:
							return ["1"]
						else: 
							if xs[12] == 'Y':
								return ["1"]
							else: 
								if xs[0] > 26.0:
									return ["1"]
								else: 
									return ["0"]
				else: 
					if xs[10] > 103113.6:
						return ["0"]
					else: 
						if xs[0] > 58.0:
							return ["1"]
						else: 
							return ["0"]
			else: 
				return ["0"]
		else: 
			if xs[10] > 104630.0:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[6] > 12416.433962:
			if xs[7] > 105793.4:
				if xs[4] > 2252.0:
					return ["1"]
				else: 
					return ["0"]
			else: 
				if xs[11] > 700.0:
					if xs[2] > 103347.0:
						return ["1"]
					else: 
						if xs[6] > 12918.380952:
							if xs[0] > 58.0:
								if xs[0] > 60.0:
									return ["1"]
								else: 
									if xs[11] > 3017.9:
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


# Model 17
def tree_17(xs):
	if xs[7] > 78871.9:
		if xs[7] > 79110.5:
			if xs[7] > 177559.9:
				return ["1"]
			else: 
				if xs[8] > 0.5:
					if xs[9] > 38522.04:
						return ["1"]
					else: 
						if xs[8] > 37.9:
							if xs[9] > 16732.980328:
								if xs[4] > 1542.0:
									return ["1"]
								else: 
									if xs[7] > 146593.9:
										return ["1"]
									else: 
										return ["0"]
							else: 
								if xs[5] == 'ISSUANCE AFTER TRANSACTION':
									return ["1"]
								else: 
									return ["0"]
						else: 
							if xs[11] > 221.6:
								if xs[10] > 79030.0:
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
		if xs[8] > 1.0:
			if xs[0] > 63.0:
				return ["1"]
			else: 
				if xs[2] > 42821.0:
					if xs[9] > 13629.668657:
						if xs[7] > 21277.3:
							if xs[0] > 58.0:
								if xs[6] > 17626.546667:
									return ["1"]
								else: 
									if xs[8] > 14483.6:
										return ["0"]
									else: 
										return ["1"]
							else: 
								return ["1"]
						else: 
							if xs[7] > 21245.3:
								return ["0"]
							else: 
								return ["1"]
					else: 
						return ["1"]
				else: 
					return ["0"]
		else: 
			return ["0"]


# Model 18
def tree_18(xs):
	if xs[8] > 30.5:
		if xs[9] > 50066.470588:
			if xs[9] > 50462.202778:
				return ["1"]
			else: 
				return ["0"]
		else: 
			if xs[9] > 11264.191304:
				if xs[10] > 90014.6:
					if xs[0] > 59.0:
						if xs[6] > 32233.656716:
							return ["0"]
						else: 
							return ["1"]
					else: 
						if xs[3] > 8.23:
							return ["0"]
						else: 
							if xs[8] > 150.6:
								return ["1"]
							else: 
								if xs[9] > 21382.92623:
									if xs[10] > 126175.3:
										return ["1"]
									else: 
										if xs[11] > 57.5:
											if xs[0] > 22.0:
												return ["1"]
											else: 
												return ["0"]
										else: 
											return ["0"]
								else: 
									return ["0"]
				else: 
					if xs[12] == 'Y':
						if xs[10] > 28547.6:
							if xs[0] > 40.0:
								if xs[4] > 1358.0:
									return ["1"]
								else: 
									if xs[3] > 3.98:
										return ["0"]
									else: 
										return ["1"]
							else: 
								return ["1"]
						else: 
							if xs[8] > 800.0:
								return ["1"]
							else: 
								if xs[8] > 500.0:
									if xs[0] > 18.0:
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
		if xs[11] > 1400.0:
			if xs[6] > 37437.298462:
				return ["0"]
			else: 
				return ["1"]
		else: 
			return ["0"]


# Model 19
def tree_19(xs):
	if xs[7] > 70609.8:
		if xs[7] > 70717.5:
			if xs[10] > 60800.0:
				if xs[6] > 53603.743939:
					return ["1"]
				else: 
					if xs[2] > 42821.0:
						if xs[6] > 17441.124:
							if xs[10] > 178978.6:
								return ["1"]
							else: 
								if xs[5] == 'ISSUANCE AFTER TRANSACTION':
									return ["1"]
								else: 
									if xs[10] > 178414.6:
										return ["0"]
									else: 
										if xs[9] > 16732.980328:
											if xs[8] > 0.4:
												if xs[12] == 'Y':
													if xs[9] > 22441.051064:
														if xs[2] > 58796.0:
															if xs[2] > 70646.0:
																if xs[0] > 59.0:
																	return ["0"]
																else: 
																	if xs[7] > 192183.2:
																		return ["1"]
																	else: 
																		if xs[6] > 25294.125806:
																			if xs[4] > 1913.0:
																				if xs[2] > 75232.0:
																					if xs[7] > 183198.8:
																						if xs[11] > 727.8:
																							return ["1"]
																						else: 
																							return ["0"]
																					else: 
																						if xs[10] > 126175.3:
																							return ["1"]
																						else: 
																							if xs[10] > 122452.6:
																								return ["0"]
																							else: 
																								if xs[11] > 2100.0:
																									return ["1"]
																								else: 
																									if xs[10] > 79030.0:
																										if xs[0] > 43.0:
																											return ["0"]
																										else: 
																											if xs[0] > 33.0:
																												return ["1"]
																											else: 
																												return ["0"]
																									else: 
																										return ["1"]
																				else: 
																					return ["0"]
																			else: 
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
		else: 
			return ["0"]
	else: 
		if xs[2] > 42821.0:
			if xs[10] > 24468.6:
				if xs[10] > 28382.0:
					if xs[2] > 107870.0:
						return ["1"]
					else: 
						if xs[10] > 60229.6:
							if xs[10] > 60269.3:
								return ["1"]
							else: 
								return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[8] > 500.0:
						if xs[7] > 19289.6:
							if xs[6] > 11871.272414:
								if xs[8] > 700.0:
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
			return ["0"]


# Model 20
def tree_20(xs):
	if xs[8] > 37.9:
		if xs[6] > 12863.857143:
			if xs[6] > 12918.380952:
				if xs[4] > 2218.0:
					if xs[11] > 2322.7:
						return ["1"]
					else: 
						if xs[4] > 2354.0:
							if xs[2] > 170449.0:
								if xs[6] > 13680.847368:
									if xs[10] > 125314.6:
										if xs[0] > 57.0:
											return ["1"]
										else: 
											return ["0"]
									else: 
										if xs[2] > 226122.0:
											return ["1"]
										else: 
											if xs[8] > 800.0:
												return ["1"]
											else: 
												if xs[11] > 14.6:
													if xs[3] > 2.31:
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
							if xs[11] > 1500.0:
								if xs[0] > 53.0:
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
			return ["1"]
	else: 
		if xs[11] > 221.6:
			if xs[0] > 29.0:
				return ["0"]
			else: 
				return ["1"]
		else: 
			return ["0"]


# Model 21
def tree_21(xs):
	if xs[2] > 70646.0:
		if xs[8] > 35.5:
			if xs[9] > 50066.470588:
				return ["1"]
			else: 
				if xs[6] > 12863.857143:
					if xs[6] > 12918.380952:
						if xs[0] > 58.0:
							if xs[11] > 1814.6:
								return ["1"]
							else: 
								if xs[11] > 1800.0:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[10] > 27463.6:
								if xs[8] > 82.6:
									if xs[10] > 28382.0:
										return ["1"]
									else: 
										return ["0"]
								else: 
									if xs[0] > 33.0:
										return ["1"]
									else: 
										if xs[4] > 2305.0:
											return ["1"]
										else: 
											if xs[2] > 107911.0:
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
			if xs[9] > 30843.8:
				if xs[8] > 34.5:
					return ["0"]
				else: 
					if xs[11] > 1800.0:
						if xs[9] > 31715.627586:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[7] > 99754.1:
			if xs[6] > 44979.418519:
				return ["1"]
			else: 
				return ["0"]
		else: 
			return ["1"]


# Model 22
def tree_22(xs):
	if xs[6] > 27252.271429:
		if xs[9] > 24619.016:
			if xs[2] > 42821.0:
				if xs[6] > 31172.686364:
					if xs[10] > 151814.8:
						return ["1"]
					else: 
						if xs[10] > 151430.0:
							return ["0"]
						else: 
							if xs[8] > 6.0:
								if xs[9] > 25913.44127:
									if xs[9] > 49726.144444:
										return ["0"]
									else: 
										if xs[0] > 59.0:
											return ["1"]
										else: 
											if xs[8] > 35.5:
												return ["1"]
											else: 
												if xs[2] > 197099.0:
													return ["1"]
												else: 
													return ["0"]
								else: 
									return ["0"]
							else: 
								return ["0"]
				else: 
					if xs[9] > 28097.333333:
						if xs[4] > 1668.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["1"]
			else: 
				if xs[0] > 29.0:
					return ["1"]
				else: 
					return ["0"]
		else: 
			if xs[11] > 800.0:
				return ["1"]
			else: 
				return ["0"]
	else: 
		if xs[11] > 14.6:
			if xs[11] > 25.0:
				return ["1"]
			else: 
				if xs[1] == 'M':
					return ["0"]
				else: 
					return ["1"]
		else: 
			return ["0"]


# Model 23
def tree_23(xs):
	if xs[10] > 77669.6:
		if xs[8] > 0.4:
			if xs[8] > 35.5:
				if xs[2] > 51313.0:
					if xs[10] > 149330.0:
						return ["1"]
					else: 
						if xs[0] > 59.0:
							if xs[4] > 9208.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							if xs[6] > 29613.735849:
								return ["1"]
							else: 
								if xs[0] > 58.0:
									return ["0"]
								else: 
									if xs[9] > 16732.980328:
										return ["1"]
									else: 
										return ["0"]
				else: 
					if xs[6] > 29916.512903:
						return ["1"]
					else: 
						return ["0"]
			else: 
				if xs[10] > 79030.0:
					if xs[9] > 36381.457143:
						if xs[2] > 117897.0:
							return ["0"]
						else: 
							return ["1"]
					else: 
						return ["0"]
				else: 
					return ["1"]
		else: 
			return ["0"]
	else: 
		if xs[7] > 19297.8:
			if xs[6] > 11192.512903:
				if xs[7] > 19307.4:
					if xs[8] > 1.0:
						if xs[0] > 58.0:
							if xs[8] > 14395.0:
								if xs[4] > 6295.0:
									return ["1"]
								else: 
									return ["0"]
							else: 
								return ["1"]
						else: 
							if xs[2] > 45714.0:
								if xs[10] > 57480.6:
									if xs[8] > 300.0:
										return ["1"]
									else: 
										if xs[4] > 2906.0:
											if xs[9] > 27895.732353:
												return ["0"]
											else: 
												return ["1"]
										else: 
											return ["1"]
								else: 
									if xs[7] > 22278.8:
										return ["1"]
									else: 
										if xs[9] > 11321.55:
											return ["1"]
										else: 
											return ["0"]
							else: 
								return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
			else: 
				return ["1"]
		else: 
			return ["1"]


# Model 24
def tree_24(xs):
	if xs[8] > 0.4:
		if xs[8] > 1.0:
			if xs[6] > 48440.8875:
				if xs[0] > 61.0:
					return ["0"]
				else: 
					if xs[3] > 5.39:
						if xs[0] > 44.0:
							if xs[0] > 52.0:
								return ["0"]
							else: 
								if xs[11] > 7825.6:
									return ["0"]
								else: 
									return ["1"]
						else: 
							return ["1"]
					else: 
						return ["1"]
			else: 
				if xs[10] > 77669.6:
					if xs[8] > 6.4:
						if xs[6] > 42347.5875:
							return ["1"]
						else: 
							if xs[7] > 56212.9:
								if xs[3] > 8.23:
									if xs[9] > 16732.980328:
										return ["1"]
									else: 
										return ["0"]
								else: 
									if xs[7] > 177099.7:
										return ["1"]
									else: 
										if xs[10] > 78650.6:
											if xs[8] > 19.7:
												if xs[8] > 30.5:
													if xs[10] > 123831.3:
														return ["1"]
													else: 
														if xs[1] == 'M':
															if xs[10] > 122952.6:
																return ["0"]
															else: 
																return ["1"]
														else: 
															return ["1"]
												else: 
													return ["1"]
											else: 
												if xs[11] > 930.6:
													return ["1"]
												else: 
													return ["0"]
										else: 
											return ["1"]
							else: 
								return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[6] > 13677.823729:
						if xs[9] > 17452.427027:
							return ["1"]
						else: 
							if xs[1] == 'M':
								return ["1"]
							else: 
								if xs[9] > 17437.9:
									if xs[4] > 2354.0:
										return ["1"]
									else: 
										return ["0"]
								else: 
									return ["1"]
					else: 
						return ["1"]
		else: 
			return ["0"]
	else: 
		return ["0"]


# Model 25
def tree_25(xs):
	if xs[9] > 13844.437037:
		if xs[8] > 35.5:
			if xs[2] > 42821.0:
				if xs[0] > 58.0:
					if xs[11] > 3017.9:
						return ["1"]
					else: 
						if xs[0] > 60.0:
							return ["1"]
						else: 
							if xs[11] > 800.0:
								if xs[8] > 166.2:
									if xs[11] > 1814.6:
										return ["0"]
									else: 
										if xs[7] > 33434.9:
											return ["0"]
										else: 
											return ["1"]
								else: 
									return ["1"]
							else: 
								return ["0"]
				else: 
					if xs[8] > 63.2:
						if xs[9] > 13890.721429:
							if xs[9] > 50066.470588:
								if xs[8] > 654.6:
									return ["1"]
								else: 
									return ["0"]
							else: 
								if xs[7] > 43179.2:
									if xs[6] > 23375.869697:
										if xs[9] > 18021.232075:
											if xs[0] > 22.0:
												if xs[7] > 43571.7:
													return ["1"]
												else: 
													return ["0"]
											else: 
												if xs[8] > 150.6:
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
						if xs[10] > 97052.8:
							return ["1"]
						else: 
							return ["0"]
			else: 
				if xs[7] > 23346.7:
					return ["1"]
				else: 
					return ["0"]
		else: 
			if xs[2] > 387570.0:
				return ["1"]
			else: 
				if xs[11] > 1400.0:
					if xs[5] == 'MONTHLY ISSUANCE':
						return ["1"]
					else: 
						return ["0"]
				else: 
					return ["0"]
	else: 
		return ["1"]


