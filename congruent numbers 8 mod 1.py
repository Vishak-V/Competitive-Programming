import math
conjecture_congruent_numbers = []
for n in range(1, 1000, 8): #tqdm
    An = 0
    Bn = 0
    # An_flag = 0
    # Bn_flag = 0

    An_Set = []
    Bn_Set = []
    An_Unique = []
    Bn_Unique = []
    Test_Set = []

    x_max = int(sqrt(n / 2))
    y_max = int(sqrt(n))
    z_max = int(sqrt(n / 8))

    # print(x_max, y_max, z_max)
    for i in range(-x_max, x_max + 1):
        for j in range(-y_max, y_max + 1):
            for k in range(-z_max, z_max + 1):
                # print(i, j, k)
                An_num = 2 * pow(i, 2) + pow(j, 2) + 32 * pow(k, 2)
                Bn_num = 2 * pow(i, 2) + pow(j, 2) + 8 * pow(k, 2)

                if An_num == n: #An_flag == 0 and
                    An = An + 1
                    An_Set.append([i, j, k])
                    if not XcontainsY(An_Unique, [abs(i), abs(j), abs(k)]):
                        An_Unique.append([abs(i), abs(j), abs(k)])

                if Bn_num == n: #Bn_flag == 0 and
                    Bn = Bn + 1
                    Bn_Set.append([i, j, k])
                    if not XcontainsY(Bn_Unique, [abs(i), abs(j), abs(k)]):
                        Bn_Unique.append([abs(i), abs(j), abs(k)])

    flag_print = False
    flag_multiple_two = False
    flag_multiple_two_number = 0
    y_coordinate_multiple_four = []
    
    
    if isSquareFree(n) is True:
        for coord_a in An_Unique:
            if coord_a[0] % 4 == 0 and coord_a[2] == 0:
                y_coordinate_multiple_four.append(coord_a[1])

                flag_print = True
            if coord_a[0] % 4 != 0 and coord_a[2] == 0:
                flag_print = False
                break

        for coord_b in Bn_Unique:
            if coord_b[0] == 2 * coord_b[2]:
                flag_multiple_two_number += 1
                flag_multiple_two = True

    if flag_print and An * 2 == Bn: #flag_print and 
        conjecture_congruent_numbers.append(n)
        print('n:', n)
#         print('n mod 128:',n % 128)
#         print('y^3 mod n:',np.array(y_coordinate_multiple_four)**3 % n)
#         print("Congruent")
#         print(An_Set)
#         print(Bn_Set)
        print(An_Unique)
        print(Bn_Unique)
        
        AIndToRemove = []
        BIndToRemove = []
        for i in range(len(An_Unique)):
            setA = An_Unique[i]
            if (setA[0] != 0 and setA[2] != 0):
                AIndToRemove.append(i)
                for j in range(len(Bn_Unique)):
                    if(Bn_Unique[j][1] == setA[1]):
                        BIndToRemove.append(j)

        for i in AIndToRemove[::-1]:
            An_Unique.pop(i)

        for i in BIndToRemove[::-1]:
            Bn_Unique.pop(i)
        
        print(An_Unique)
        print(Bn_Unique)
#         print('1-1:', len(y_coordinate_multiple_four) == flag_multiple_two_number)
#         print('2n, n existence:',flag_multiple_two)
        print('\n')
#     else:
#         print("NOT Congruent")
