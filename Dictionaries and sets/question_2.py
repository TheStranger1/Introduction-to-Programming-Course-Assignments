def uniqueItems(list1,list2):
    s1= set(list1)
    s2 = set(list2)
    s3 = s1.union(s2)
    return s3
