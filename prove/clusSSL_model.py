"""
Script for testing the CLUS algorithm.
"""

import subprocess
import os

# number of folds
K = 5

if os.path.exists("resources/results.txt"):
    os.remove("resources/results.txt")
    print("Old file removed")

for i in range(K):
    # changing train and test file into dataset
    with open('external_libraries/conf.s','r') as file:
        first = file.readlines()
    first[first.index('[Data]\n') + 1] = f"File = {K}_fold/train{i}.arff\n"
    first[first.index('[Data]\n') + 2] = f"TestSet = {K}_fold/test{i}.arff\n"

    with open('external_libraries/conf.s','w') as file:
        file.writelines(first)

    with open('external_libraries/conf_2.s', 'r') as file:
        first = file.readlines()
    first[first.index('[Data]\n') + 1] = f"File = {K}_fold/train{i}.arff\n"
    first[first.index('[Data]\n') + 2] = f"TestSet = {K}_fold/test{i}.arff\n "

    with open('external_libraries/conf_2.s', 'w') as file:
        file.writelines(first)
    # running the subprocess
    subprocess.run(['java','-jar','external_libraries/clusSSL.jar','-forest',
                    'external_libraries/conf.s'])
    with open('external_libraries/conf.out','r') as file:
        first = file.readlines()

    subprocess.run(['java','-jar','external_libraries/clusSSL.jar','-ssl','-forest',
                    'external_libraries/conf_2.s'])

    with open('external_libraries/conf_2.out','r') as file:
        second = file.readlines()

    with open('resources/results.txt','a') as file:
        file.write(f'--------------------------------------FOLD-{i}---------------------------------------------\n')
        file.writelines(first[first.index('Testing error\n'):])
        file.write('------------------------------------------------------------------------------------\n')
        file.writelines(second[second.index('Testing error\n'):])
