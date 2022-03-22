#!/usr/bin/env python
# coding: utf-8

# In[1]:


from autoencoder_train_real import *


#가중치를준 음식들 INPUT에 넣고 맛있는 순서대로 나오게끔 하기
def train_model(model, include, exclude):
    aaa=[]
    lists = include
    arr=[0 for i in range(1, 310)]
    count=0
    for i in lists:
        if count<4:
            arr[i]=5
        elif count<8:
            arr[i]=3
        elif count<12:
            arr[i]=1
        count+=1


    aaa.append(arr)
    bb=torch.FloatTensor(aaa)
    new_user_input = bb
    output = model(new_user_input)

    output = (output+1)


    # 가장 맛있는 음식 순서대로 나열하기
    sort_food_id = np.argsort(-output.detach().numpy())

    # array to list
    sort_food_id_list=sort_food_id.tolist()

    # 차원 줄이기
    food_real_list=np.ravel(sort_food_id_list, order='C').tolist()
    print(food_real_list)
    # return

    file=pd.read_excel('food_label.xlsx')

    rm_list=set()

    for j in exclude:
        for i in range(309):
            if file[j][i]==1:
                rm_list.add(file['f_num'][i])

    #타입 리스트로 바꾸기
    rm_real_list = list(rm_list)

    for i in food_real_list:
        if i in rm_list or i in include:
            food_real_list.remove(i)

    top_10 = food_real_list[:10]

    count1 = 2
    sampleList1 = include
    random_list1 = random.sample(sampleList1, count1)

    count = 4
    sampleList = top_10
    random_list2 = random.sample(sampleList, count)

    final_list = random_list1 + random_list2
    return final_list


# remove_random(include, exclude)
