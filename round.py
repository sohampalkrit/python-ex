def round_scores(student_scores):
    n=len(student_scores)
    i=0
    l1=[]
    while i<n:
        l1.append(round(student_scores[i]))
        i+=1
    return l1
def count_failed_students(students_scores):
    n=len(students_scores)
    i=0
    c=0
    while i<n:
        if students_scores[i]<=40:
            c=c+1
        i+=1
    return c
def above_threshold(student_scores,threshold):
    n=len(student_scores)
    l1=[]
    i=0
    while i<n:
        if student_scores[i]>=threshold:
            l1.append(student_scores[i])
        i+=1
    return l1
def letter_grades(highest):
    n=(highest-40)//4
    return [41,41+n,41+n+n,41+n+n+n]
def student_ranking(student_scores,student_names):
    n=len(student_scores)
    i=0
    l1=[]
    while i<n:
        s1=str(i+1)+'.'+' '+student_names[i]+':'+' '+str(student_scores[i])
        l1.append(s1)
        i+=1
    return l1
def perfect_score(student_info):
  i=0
  if student_info!=[]:
    n=len(student_info)
    while i<n:
        if student_info[i][1]==100:
            return student_info[i]
        
        i+=1
    else:
        return []
  else:
      return []
    


    

