# This is a sample Python script.
import sys


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def lst_user_data():
    user_data = '1:Kamal:10\n2:Salemallah:20\n3:Rafa:30\n4:Dana:40\n5:Abdulaziz:50'
    user_initial = user_data.split('\n')
    lst_info = [i.split(':') for i in user_initial]
    # for i in user_info :
    #     lst_info.append(i.split(':'))

    return lst_info


def Appexit():
    print('System has been Exit !! Bey Bey !!')
    sys.exit()  # to close program


def get_answer(question):
    while True:
        answer = input(question)
        if answer == 'y' or answer == 'Y':
            print('you are input YES')
            return True
        elif answer == 'n' or answer == 'N':
            print('You are input NO')
            return False
        else:
            print('Please Input y to Yes or n to NO')
            continue


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # isUser = get_answer('Do you have Account in the system ? print (Y/N) :')
    # if isUser:
    #     print("to do this user")
    # else:
    #     print('Not user')
    #     Appexit()

    un_input = input('Enter your Username Please :')
    pw_input = input('Enter your Password Please :')
    fr = open('users_db.txt', 'r', encoding='utf8')
    isUser = False
    n=0
    for line in fr:
        tmp_udb = line.split(':')
        if n != 0:
            if un_input == tmp_udb[1] and (pw_input + '\n') == tmp_udb[2]:
                isUser = True
                break
            else:
                isUser = False
            n+=1
        else :
            n+=1

    print(isUser)
    fr.close()
    # print(lst_user_data())
    print(f'your Username : {un_input} \n your Password : {pw_input}')
