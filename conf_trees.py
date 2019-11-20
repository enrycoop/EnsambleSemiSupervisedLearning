# Python code of the trees in the ensemble

# Model 1
def tree_1(xs):
	if xs[7] > 19207.3:
		if xs[7] > 19307.4:
			if xs[10] > 28250.6:
				if xs[8] > 12.6:
					if xs[10] > 28382.0:
						if xs[0] > 62.0:
							if xs[8] > 124.1:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[6] > 10760.775362:
								if xs[6] > 11483.972059:
									if xs[7] > 23425.9:
										if xs[8] > 15.8:
											if xs[9] > 11770.021667:
												if xs[8] > 37.9:
													if xs[10] > 66730.0:
														if xs[10] > 66814.6:
															return ["1"]
														else: 
															return ["0"]
													else: 
														if xs[3] > 2.07:
															return ["1"]
														else: 
															if xs[3] > 2.01:
																return ["0"]
															else: 
																return ["1"]
												else: 
													return ["1"]
											else: 
												if xs[8] > 12722.9:
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
						if xs[0] > 47.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					if xs[9] > 25445.998551:
						return ["1"]
					else: 
						return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[3] > 0.59:
				return ["1"]
			else: 
				return ["0"]
	else: 
		return ["1"]


# Model 2
def tree_2(xs):
	if xs[8] > 0.5:
		if xs[6] > 10882.266:
			if xs[0] > 59.0:
				if xs[10] > 87130.0:
					if xs[8] > 83.2:
						if xs[8] > 700.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
				else: 
					return ["1"]
			else: 
				if xs[6] > 10962.066667:
					if xs[8] > 7.0:
						if xs[7] > 78850.7:
							if xs[6] > 16739.402564:
								if xs[3] > 8.23:
									if xs[0] > 34.0:
										return ["0"]
									else: 
										return ["1"]
								else: 
									if xs[10] > 127313.3:
										return ["1"]
									else: 
										if xs[11] > 14.6:
											if xs[0] > 45.0:
												if xs[7] > 79110.5:
													if xs[11] > 30.0:
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
							if xs[10] > 35004.6:
								return ["1"]
							else: 
								if xs[0] > 22.0:
									if xs[10] > 33727.6:
										if xs[7] > 21354.4:
											return ["1"]
										else: 
											if xs[6] > 14836.088235:
												return ["0"]
											else: 
												return ["1"]
									else: 
										return ["1"]
								else: 
									if xs[10] > 34795.6:
										return ["0"]
									else: 
										return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[0] > 41.0:
						return ["1"]
					else: 
						return ["0"]
		else: 
			return ["1"]
	else: 
		return ["0"]


# Model 3
def tree_3(xs):
	if xs[0] > 63.0:
		return ["1"]
	else: 
		if xs[8] > 12.6:
			if xs[8] > 21.7:
				if xs[9] > 50066.470588:
					if xs[9] > 50462.202778:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[10] > 28274.6:
						if xs[6] > 15612.132:
							if xs[10] > 28382.0:
								if xs[9] > 13239.333333:
									if xs[8] > 15743.0:
										return ["1"]
									else: 
										if xs[8] > 52.6:
											if xs[6] > 15692.557576:
												if xs[0] > 60.0:
													if xs[11] > 30.0:
														return ["1"]
													else: 
														return ["0"]
												else: 
													if xs[11] > 3100.0:
														return ["1"]
													else: 
														if xs[3] > 8.23:
															return ["1"]
														else: 
															if xs[6] > 16626.281481:
																if xs[8] > 10991.2:
																	return ["1"]
																else: 
																	if xs[6] > 17373.398462:
																		if xs[8] > 138.1:
																			return ["1"]
																		else: 
																			if xs[9] > 19195.234286:
																				if xs[2] > 138032.0:
																					if xs[2] > 387570.0:
																						return ["1"]
																					else: 
																						if xs[8] > 129.4:
																							return ["0"]
																						else: 
																							if xs[1] == 'M':
																								if xs[9] > 31979.309231:
																									return ["1"]
																								else: 
																									if xs[8] > 68.9:
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
						return ["1"]
			else: 
				if xs[10] > 132014.6:
					return ["1"]
				else: 
					if xs[1] == 'M':
						return ["1"]
					else: 
						return ["0"]
		else: 
			if xs[2] > 110643.0:
				return ["0"]
			else: 
				if xs[2] > 107911.0:
					return ["1"]
				else: 
					return ["0"]


# Model 4
def tree_4(xs):
	if xs[8] > 21.7:
		if xs[3] > 8.23:
			if xs[7] > 72167.0:
				return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[9] > 50066.470588:
				if xs[11] > 7825.6:
					if xs[6] > 52828.943243:
						return ["1"]
					else: 
						if xs[2] > 127369.0:
							return ["0"]
						else: 
							return ["1"]
				else: 
					return ["1"]
			else: 
				if xs[6] > 7567.598571:
					if xs[6] > 7663.73:
						if xs[5] == 'WEEKLY ISSUANCE':
							if xs[11] > 30.0:
								return ["1"]
							else: 
								return ["0"]
						else: 
							if xs[0] > 58.0:
								if xs[0] > 60.0:
									return ["1"]
								else: 
									if xs[3] > 2.07:
										return ["1"]
									else: 
										if xs[7] > 47451.5:
											if xs[0] > 59.0:
												return ["0"]
											else: 
												return ["1"]
										else: 
											return ["0"]
							else: 
								if xs[7] > 22221.6:
									if xs[6] > 17816.08:
										return ["1"]
									else: 
										if xs[7] > 22278.8:
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
		if xs[10] > 167534.0:
			return ["1"]
		else: 
			if xs[8] > 20.1:
				if xs[1] == 'M':
					return ["1"]
				else: 
					return ["0"]
			else: 
				return ["0"]


# Model 5
def tree_5(xs):
	if xs[10] > 85930.0:
		if xs[7] > 53727.2:
			if xs[10] > 86071.8:
				if xs[8] > 6.0:
					if xs[9] > 17604.368421:
						if xs[6] > 27547.50303:
							if xs[11] > 15300.0:
								return ["1"]
							else: 
								if xs[4] > 2471.0:
									if xs[2] > 77963.0:
										if xs[6] > 27874.3875:
											if xs[8] > 50.1:
												if xs[9] > 22528.285714:
													if xs[10] > 151814.8:
														return ["1"]
													else: 
														if xs[6] > 53401.54:
															return ["1"]
														else: 
															if xs[8] > 53.1:
																if xs[5] == 'MONTHLY ISSUANCE':
																	if xs[10] > 149914.6:
																		return ["1"]
																	else: 
																		if xs[11] > 11102.6:
																			return ["1"]
																		else: 
																			if xs[11] > 10400.0:
																				return ["1"]
																			else: 
																				if xs[10] > 145469.1:
																					return ["1"]
																				else: 
																					if xs[6] > 39429.048214:
																						return ["1"]
																					else: 
																						if xs[6] > 34033.076389:
																							if xs[7] > 151451.2:
																								return ["0"]
																							else: 
																								if xs[2] > 139012.0:
																									return ["1"]
																								else: 
																									if xs[6] > 34440.385417:
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
							if xs[11] > 200.0:
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
		if xs[7] > 20998.9:
			if xs[6] > 9667.290741:
				if xs[5] == 'ISSUANCE AFTER TRANSACTION':
					if xs[4] > 3651.0:
						return ["0"]
					else: 
						return ["1"]
				else: 
					if xs[4] > 6872.0:
						if xs[7] > 21354.4:
							if xs[0] > 50.0:
								if xs[4] > 18696.0:
									return ["1"]
								else: 
									if xs[12] == 'Y':
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
			return ["1"]


# Model 6
def tree_6(xs):
	if xs[9] > 7482.216:
		if xs[9] > 7495.315385:
			if xs[2] > 42821.0:
				if xs[3] > 8.23:
					if xs[7] > 144523.9:
						return ["1"]
					else: 
						return ["0"]
				else: 
					if xs[9] > 10357.832432:
						if xs[11] > 3500.0:
							if xs[2] > 70646.0:
								return ["1"]
							else: 
								if xs[2] > 67298.0:
									return ["0"]
								else: 
									return ["1"]
						else: 
							if xs[0] > 20.0:
								if xs[9] > 44051.489744:
									return ["1"]
								else: 
									if xs[2] > 387570.0:
										return ["1"]
									else: 
										if xs[12] == 'Y':
											if xs[8] > 0.5:
												if xs[8] > 12.6:
													if xs[3] > 0.59:
														if xs[11] > 2491.4:
															return ["1"]
														else: 
															if xs[3] > 1.86:
																if xs[2] > 95616.0:
																	if xs[6] > 34033.076389:
																		if xs[9] > 28472.625532:
																			if xs[7] > 161527.4:
																				return ["1"]
																			else: 
																				return ["0"]
																		else: 
																			return ["0"]
																	else: 
																		if xs[2] > 106054.0:
																			if xs[11] > 14.6:
																				if xs[3] > 4.79:
																					return ["1"]
																				else: 
																					if xs[8] > 19.5:
																						if xs[0] > 49.0:
																							if xs[9] > 21815.812903:
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
																	return ["1"]
															else: 
																return ["1"]
													else: 
														if xs[11] > 3436.1:
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
				if xs[7] > 35190.1:
					return ["1"]
				else: 
					return ["0"]
		else: 
			return ["0"]
	else: 
		return ["1"]


# Model 7
def tree_7(xs):
	if xs[10] > 60777.6:
		if xs[6] > 17277.883871:
			if xs[8] > 6.4:
				if xs[9] > 16732.980328:
					if xs[0] > 60.0:
						if xs[4] > 5887.0:
							if xs[8] > 800.0:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["0"]
					else: 
						if xs[9] > 19180.59375:
							if xs[8] > 12.6:
								if xs[9] > 19195.234286:
									if xs[10] > 61794.6:
										if xs[6] > 27252.271429:
											if xs[9] > 21957.978261:
												if xs[8] > 128.0:
													if xs[8] > 131.2:
														if xs[11] > 7677.6:
															if xs[0] > 21.0:
																return ["1"]
															else: 
																if xs[12] == 'Y':
																	return ["0"]
																else: 
																	return ["1"]
														else: 
															return ["1"]
													else: 
														if xs[8] > 130.9:
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
			return ["0"]
	else: 
		if xs[4] > 1099.0:
			return ["1"]
		else: 
			if xs[8] > 9781.1:
				return ["1"]
			else: 
				return ["0"]


# Model 8
def tree_8(xs):
	if xs[7] > 74153.1:
		if xs[0] > 21.0:
			if xs[7] > 74170.5:
				if xs[9] > 16165.8:
					if xs[9] > 32731.228571:
						if xs[3] > 5.72:
							if xs[9] > 45891.716667:
								return ["0"]
							else: 
								return ["1"]
						else: 
							return ["1"]
					else: 
						if xs[0] > 22.0:
							if xs[8] > 301.0:
								return ["0"]
							else: 
								if xs[10] > 56114.6:
									if xs[3] > 1.86:
										if xs[8] > 0.5:
											if xs[8] > 6.4:
												if xs[8] > 19.5:
													if xs[2] > 323870.0:
														if xs[11] > 14.6:
															return ["1"]
														else: 
															return ["0"]
													else: 
														if xs[4] > 2799.0:
															return ["1"]
														else: 
															if xs[4] > 2718.0:
																return ["0"]
															else: 
																return ["1"]
												else: 
													if xs[4] > 4433.0:
														return ["0"]
													else: 
														if xs[5] == 'MONTHLY ISSUANCE':
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
		if xs[5] == 'ISSUANCE AFTER TRANSACTION':
			return ["1"]
		else: 
			if xs[9] > 7480.280645:
				if xs[10] > 17114.6:
					if xs[8] > 134.5:
						if xs[11] > 414.6:
							if xs[9] > 11138.823256:
								if xs[7] > 19307.4:
									if xs[9] > 11561.647619:
										return ["1"]
									else: 
										return ["0"]
								else: 
									if xs[3] > 0.59:
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


# Model 9
def tree_9(xs):
	if xs[6] > 7599.006977:
		if xs[11] > 41.2:
			if xs[6] > 12912.161765:
				if xs[6] > 12918.380952:
					if xs[9] > 11770.021667:
						if xs[8] > 0.5:
							if xs[6] > 52502.0125:
								if xs[2] > 285387.0:
									return ["0"]
								else: 
									return ["1"]
							else: 
								if xs[6] > 17076.383824:
									if xs[7] > 23439.7:
										if xs[7] > 25690.6:
											if xs[6] > 36821.547222:
												if xs[2] > 323870.0:
													return ["1"]
												else: 
													if xs[6] > 37074.886111:
														if xs[9] > 34948.638889:
															return ["1"]
														else: 
															if xs[0] > 20.0:
																return ["1"]
															else: 
																return ["0"]
													else: 
														return ["0"]
											else: 
												return ["1"]
										else: 
											if xs[0] > 57.0:
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
						if xs[2] > 95616.0:
							return ["1"]
						else: 
							return ["0"]
				else: 
					return ["0"]
			else: 
				return ["1"]
		else: 
			if xs[10] > 97414.6:
				if xs[10] > 132114.6:
					return ["1"]
				else: 
					if xs[7] > 110571.3:
						return ["0"]
					else: 
						if xs[10] > 114914.6:
							return ["0"]
						else: 
							return ["1"]
			else: 
				return ["0"]
	else: 
		return ["1"]


# Model 10
def tree_10(xs):
	if xs[10] > 17100.0:
		if xs[10] > 17114.6:
			if xs[9] > 10913.706667:
				if xs[0] > 60.0:
					if xs[2] > 177686.0:
						if xs[11] > 8202.0:
							return ["1"]
						else: 
							return ["0"]
					else: 
						return ["1"]
				else: 
					if xs[8] > 6.4:
						if xs[7] > 63181.8:
							if xs[7] > 63374.3:
								if xs[6] > 21474.115:
									if xs[3] > 8.23:
										return ["1"]
									else: 
										if xs[11] > 6995.0:
											if xs[10] > 60800.0:
												if xs[6] > 52165.267647:
													if xs[4] > 4505.0:
														return ["0"]
													else: 
														return ["1"]
												else: 
													return ["1"]
											else: 
												return ["0"]
										else: 
											if xs[6] > 22839.023529:
												return ["1"]
											else: 
												if xs[8] > 8.2:
													return ["1"]
												else: 
													return ["0"]
								else: 
									return ["0"]
							else: 
								return ["0"]
						else: 
							if xs[5] == 'ISSUANCE AFTER TRANSACTION':
								if xs[9] > 10920.69375:
									return ["1"]
								else: 
									return ["0"]
							else: 
								if xs[9] > 11770.021667:
									if xs[6] > 18125.941176:
										return ["1"]
									else: 
										if xs[9] > 16528.487179:
											if xs[9] > 16721.680645:
												return ["1"]
											else: 
												return ["0"]
										else: 
											return ["1"]
								else: 
									if xs[8] > 500.0:
										return ["1"]
									else: 
										if xs[7] > 22435.1:
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
		return ["1"]


