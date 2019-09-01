
with open('new_collected.txt', 'a') as f:
        for i in range(151, 600):
            # quest_ran = ''
            # right_ran = ''
            # ans_ran = ''
            ran = str(i)
            quest_ran = '\n' + 'quest' + ran + '=' + '0' + '=' + '\n'
            right_ran = 'r' + ran + 'right' + '=' + '0' + '=' + '\n'
            ans_ran1 = 'a' + ran + 'ans' + '1' + '=' + '0' + '=' + '\n'
            ans_ran2 = 'a' + ran + 'ans' + '2' + '=' + '0' + '=' + '\n'
            ans_ran3 = 'a' + ran + 'ans' + '3' + '=' + '0' + '=' + '\n'
            ans_ran4 = 'a' + ran + 'ans' + '4' + '=' + '0' + '=' + '\n'
            ans_ran5 = 'a' + ran + 'ans' + '5' + '=' + '0' + '=' + '\n'
            ans_ran6 = 'a' + ran + 'ans' + '6' + '=' + '0' + '=' + '\n'
            ans_ran7 = 'a' + ran + 'ans' + '7' + '=' + '0' + '=' + '\n'
            ans_ran8 = 'a' + ran + 'ans' + '8' + '=' + '0' + '=' + '\n'
            ans_ran9 = 'a' + ran + 'ans' + '9' + '=' + '0' + '=' + '\n'
            ans_ran10 = 'a' + ran + 'ans' + '10' + '=' + '0' + '=' + '\n'
            ans_ran11 = 'a' + ran + 'ans' + '11' + '=' + '0' + '=' + '\n'
            f.write(quest_ran)
            f.write(right_ran)
            f.write(ans_ran1)
            f.write(ans_ran2)
            f.write(ans_ran3)
            f.write(ans_ran4)
            f.write(ans_ran5)
            f.write(ans_ran6)
            f.write(ans_ran7)
            f.write(ans_ran8)
            f.write(ans_ran9)
            f.write(ans_ran10)
            f.write(ans_ran11)
# quest1=Вопрос 1 п.1.2.6. С какой периодичностью ответственный за электрохозяйство обязан обеспечивать проверку соответствия схем электроснабжения фактическим эксплуатационным с отметкой на них о  проверке?
# a1ans1=Не реже 1 раза в 2 года
# a1ans2=Не реже 1 раза в 3 года.
# a1ans3=Не реже 1 раза в 5 лет
# r1right =1