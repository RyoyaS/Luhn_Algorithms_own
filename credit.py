credit_num = 4003600000000014
credit_list = []
for num in range(len(str(credit_num))):
    credit_list.append(str(credit_num)[0-(num+1)])

credit_num_2 = 0
credit_num_another = 0
for i, v in enumerate(credit_list):
    if i % 2 == 1:
        if int(v)*2 < 10:
            credit_num_2 = credit_num_2 + (int(v)*2)
        else:
            num = int(v)*2
            s1 = str(num)[-1]
            s10 = str(num)[-2]
            credit_num_2 = credit_num_2 + int(s1) + int(s10)
    else:
        credit_num_another = credit_num_another+int(v)

result = credit_num_another+credit_num_2
print(result)

if str(result)[-1] == "0":
    print("OK!")
else:
    print("None!")
