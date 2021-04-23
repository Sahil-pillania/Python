# program to get multiplication tables from 2 to 20 and write it to the different files 
for i in range(2, 21):
    with open(f"tables/multiplication_table_{i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}X{j} = {i*j}")
            if j!=10:
                f.write('\n')
                