for i in range(1, 6): # i에 1, 2, 3, 4, 5 값을 넣으며 반복
    if i == 1 or i == 5: #i가 1 또는 5인 경우, *을 10개 출력
        print('*' * 10)
    else: # i가 1이나 5가 아닌 경우, 공백 8칸을 사이에 두고 *을 출력
        print('*', ' ' * 8, '*', sep='')