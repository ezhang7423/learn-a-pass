#!/usr/bin/env python
# coding: utf-8

# In[1]:


import time
import sys
import os 


# In[2]:


#helper functions


def clear():
    if os.name == 'nt': 
        _ = os.system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = os.system('clear') 

#takes a list and combines the first two elements, next two, and so on. if the list length is odd, it will leave the last element be
def mergeList(liste):
    newList = []
    lenl = len(liste)
    for x in range(0, lenl-lenl//2):
        newList.append(liste[2*x:2*x+2])
    if lenl % 2 == 0:
        for x in range(len(newList)):
            newList[x] = newList[x][0]+newList[x][1]
    else: 
        for x in range(len(newList)-1):
            newList[x] = newList[x][0]+newList[x][1]
            newList[len(newList)-1] = newList[len(newList)-1][0]
    return newList


#recursive practice function that takes a list of subpasswords and drills each one sequentially
def practice(div_pas, right):
    if len(div_pas) != 0:
        sub = div_pas[0]
        print('this is the sub:', sub)
        if right == 0:
            print("DON'T TOUCH THE KEYBOARD! You can cheat, but won't learn anything")
        time.sleep(5-right*(1.1**right)) #waiting gets faster as user gets better
        clear()
        ans = input('Type it back in\n')
        if ans == sub:
            right += 1
            if right == 3:
                print('good, let\'s move on.')
                time.sleep(0.5)
                clear()
                practice(div_pas[1:], 0)
            else:
                print('good job')
                time.sleep(0.5)
                clear()
                practice(div_pas, right)
        else:
            print("try again")
            time.sleep(0.5)
            clear()
            practice(div_pas, right)
    else:
        return 
        

#builds upon practice and merges subsections into larger subsections
def test(divided_pas, times=2):
    if len(divided_pas) != 1:
        for x in range(len(divided_pas)):
            practice([divided_pas[x]], times)
        print('good job, let\'s put the subs together now.\n')
        time.sleep(2)
        clear()
        divided_pas = mergeList(divided_pas)
        test(divided_pas, 0)
    else:
        print('final practice!')
        time.sleep(.5)
        practice(divided_pas, 0)
        return
#get a password from the user
def getpass():
    ans = input('do you have a super secure password yet? (y/n)\n')
    if ans == 'n':
        wait = input('go get one here\nhttps://passwordsgenerator.net/\nand come back. Don\'t worry, just press enter when you\'re back.\n')
    else:
        pas = input('enter you password now. Don\'t worry, it won\'t be stored and we won\'t steal it!\n:')
    return pas


# In[3]:


def main():
    #variables
    pas = "CG_NRh9n6Ms:G:-H" #replace getpassword if you already have one
    num_divides = len(pas)//4
    divided_pas = []
    #get divided up password
    for x in range(1, num_divides+1):
        divided_pas.append(pas[4*x-4:4*x])
    if len(pas)/4 != len(pas)//4:
        divided_pas.append(pas[4*num_divides:len(pas)+1])
    test(["CG_NRh9n6Ms:G:-H"])
    test(["CG_NRh9n6Ms:G:-H"])
    test(["CG_NRh9n6Ms:G:-H"])
    print('you have now learned a new password, and quickly at that.')


# In[4]:

main()


