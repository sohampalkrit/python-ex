def add_me_to_the_queue(express_queue,normal_queue,ticket_type,personal_name):
    if ticket_type==1:
        s1=str(personal_name)
        express_queue.append(s1)
        return (express_queue)
    else:
        s1=str(personal_name)
        normal_queue.append(s1)
        return (normal_queue)
def find_my_friend(queue,friend_name):
    n=len(queue)
    i=0
    while i<n:
        if queue[i]==friend_name:
            return i
        i+=1
def add_me_with_my_friends(queue,index,person_name):
    l1=list(queue)
    l1.insert(int(index),str(person_name))
    return l1
def remove_the_mean_person(queue,person_name):
    l1=list(queue)
    l1.remove(str(person_name))
    return l1
def how_many_namefellows(queue,person_name):
    n=len(queue)
    i=0
    c=0
    while i<n:
        if queue[i]==person_name:
            c+=1
        i+=1
    return c
def remove_the_last_person(queue):
    n=len(queue)-1
    return queue[n]
def sorted_names(queue):
    l1=sorted(list(queue))
    return l1


    

