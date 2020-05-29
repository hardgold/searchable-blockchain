# jae_in_space
# a little example of what i am doing in my scheme
import hashlib
import random
import json
import numpy as np
vistual_list=['monday','tuesday','wednesday']
simhash_list=[10000,10001,10011,10100,10101,10111,11000,11001,11010,11011,11100]
v2s_dictionnary={'monday':[10000,10001],'tuesday':[10011,10100,10101],'wednesday':[10111,11000,11001,11010,11011,11100]}
# print(v2s_dictionnary['monday'][1])


# there are #G=#simhash pictures in the A_s
A_s={}
# there are #W linked list in the T_s
T_s={}
ctr=1


for w in vistual_list:
    # len(v2s_dictionnary[w]) just like how many nodes in linke list with the same word;
    for i in range(len(v2s_dictionnary[w])):

        id_information=hashlib.md5((w).encode('utf-8')).hexdigest()
        next_node_location=hashlib.md5(str(ctr+1).encode('utf-8')).hexdigest()
        Node=id_information+'='+str(ctr)+'=0='+str(v2s_dictionnary[w][i])+'='+next_node_location

        #  R←{0,1}
        R=bin(random.randrange(65,127))
        R=R.split('b',1)[1]


        #A_s_location=hashlib.md5(str(ctr).encode('utf-8')).hexdigest()
        #A_s_index=bin(ctr).split('b')[1]
        if(i==0):
            head_node_addr = hashlib.md5(str(ctr).encode('utf-8')).hexdigest()
        A_s_index=hashlib.md5(str(ctr).encode('utf-8')).hexdigest()
        A_s[A_s_index]=Node

        ctr+=1
    T_s_index=hashlib.md5(w.encode('utf-8')).hexdigest()
    #T_s_index=int(T_s_index,16)
    T_s[T_s_index] = head_node_addr



#start searching
search_w=input("input the vistual-word:")
t_1=hashlib.md5(search_w.encode('utf-8')).hexdigest()
now_node=A_s[T_s[t_1]]
fake_id=now_node.split('=',4)[0]


# ouput the simhash with the same word(fake_id)
result=[]
while(t_1==fake_id):
    now_node_simhash=now_node.split('=',4)[3]
    string2array=[]
    for c in now_node_simhash:
        string2array.append(c)

    # simhash of search picture
    t_2=['1','1','1','1','1']

    #compute hammingdistance
    hamdis=0
    for k in  range(len(t_2)):
        if(t_2[k]!=string2array[k]):
            hamdis+=1
    #print('ham:',hamdis)

    # if hamdis<=z ,that is a similar picture
    if(hamdis<=3):
        result.append(now_node_simhash)

    search_next_node_location=now_node.split('=',4)[4]
    if(search_next_node_location in A_s.keys()):
        now_node=A_s[search_next_node_location]
        fake_id=now_node.split('=',4)[0]
    else:
        break

# simhash
print('result:',result)

# save index={A_s,T_s} to json file
with open('index.json','w') as f2w:
    json.dump((A_s,T_s),f2w,indent=4)


# read json file to get index={A_s,T_s}
with open('index.json','r') as f2r:
    a_s,t_s=json.load(f2r)


print('a_s:',a_s)
print('t_s:',t_s)