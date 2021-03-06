from mysql_wrapper import mysql_wrapper

## Query 1
q1 = "DB1(s1) :- gtd(_, 2013, 12, _, _, _, _, _,'Iraq', _, _, _, _, _, _, _, _, _, s1, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _)"

## Query 2
q2 = "DB1(s1,g1,gs1) :- gtd(_, 2014, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, s1,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, g1, gs1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _)"

## Query 3
q3 = "meta_DB1(I1, Y1, M1, Day1, C1) :- gtd(I1, Y1, M1, Day1, _, _, _, _,C1, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _)"

## Query 4
q4 = "DB1(s1) :- gtd(_, T1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, s1, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, 'Taliban', _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _),\
T1<= 2014, T1 >= 2013"

## Query 5
q5 = "meta_DB1(I1a,Y1,M1,D1,C1,g1,gs1) :- gtd(I1a, 2016, M1, D1, _, _, _, _, C1, _, _, _, _, _, _, \
_, _,  _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, g1, gs1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _)"

## Query with all functions
q6 = "DB1(s1,p) :- gtd(_, T1, 12, d, _, _, _, _,'Iraq', _, _, _, _, _, _, _, _, _, s1, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _), T1<= 2014, GROUP_BY([s1], p = MAX(d)), SORT_BY (p, 'DESC'), p > 40,LIMIT (10)"


# ## Query with all functions
q7 = "DB1(s1,p) :- gtd(_, T1, 12, d, s2, _, _, _,'Iraq', _, _, _, _, _, _, _, _, _, s1, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _,\
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, _, \
_, _, _, _, _, _, _, _, _, _, _, _, _, _, _), s2 > 10, T1<= 2014, GROUP_BY([s1], p = MAX(d)),SORT_BY (p, 'DESC'), LIMIT (10)"


queries = [q1, q2, q3, q4, q5, q6, q7]
for query in queries:
  wrapper = mysql_wrapper.MysqlWrapper()
  print query
  print ""
  dataframe = wrapper.execute(query)
  print dataframe
  print ""