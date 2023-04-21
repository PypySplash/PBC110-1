T_nS_nL_qS_qL_rS_rL_list = input().split(',')
T = int(T_nS_nL_qS_qL_rS_rL_list[0])
nS = int(T_nS_nL_qS_qL_rS_rL_list[1])
nL = int(T_nS_nL_qS_qL_rS_rL_list[2])
qS = int(T_nS_nL_qS_qL_rS_rL_list[3])
qL = int(T_nS_nL_qS_qL_rS_rL_list[4])
rS = int(T_nS_nL_qS_qL_rS_rL_list[5])
rL = int(T_nS_nL_qS_qL_rS_rL_list[6])

pS_list = input().split(',')
pL_list = input().split(',')

rev = []

for i in range(T):
    expectS = 0
    expectL = 0
    QL = qL * i
    QS = qS * (T-i)
    if QS >= nS+1:
        QSvsnS = nS+1
    else:
        QSvsnS = QS
    for j in range(QSvsnS):
        pS = float(pS_list[j])
        expectS += pS * j
    revS = rS * expectS
    if QL >= nL+1:
        QLvsnL = nL+1
    else:
        QLvsnL = QL
    for k in range(QLvsnL):
        pL = float(pL_list[k])
        expectL += pL * k
    revL = rL * expectL
    rev_tot_i = revL + revS
    rev.append(rev_tot_i)

rev.sort()
rev.reverse()
print(int(rev[0]))

"""
if T = 2
QL = qL * 2
QS = qS * (T-2) and T - 2 >= 0:
    if QS >= nS+1:
        QSvsnS = nS+1
    else:
        QSvsnS = QS
    for i in range(QSvsnS):
        pS = int(pS_list[i])
        expectS = pS * i
        revS = rS * expectS
    if QL >= nL+1:
        QLvsnL = nL+1
    else:
        QLvsnL = QL
    for i in range(QLvsnL):
        pL = int(pL_list[i])
        expectL = pL * i
        revL = rL * expectL
    rev_tot_i = revL + revS
    rev.append(rev_tot_i)

if QL = qL * 3 and QS = qS * T-3 and T - 3 >= 0:
    if QS >= nS+1:
        QSvsnS = nS+1
    else:
        QSvsnS = QS
    for i in range(QSvsnS):
        pS = int(pS_list[i])
        expectS = pS * i
        revS = rS * expectS
    if QL >= nL+1:
        QLvsnL = nL+1
    else:
        QLvsnL = QL
    for i in range(QLvsnL):
        pL = int(pL_list[i])
        expectL = pL * i
        revL = rL * expectL
    rev_tot_i = revL + revS
    rev.append(rev_tot_i)

if QL = qL * 4 and QS = qS * T-4 and T - 4 >= 0:
    if QS >= nS+1:
        QSvsnS = nS+1
    else:
        QSvsnS = QS
    for i in range(QSvsnS):
        pS = int(pS_list[i])
        expectS = pS * i
        revS = rS * expectS
    if QL >= nL+1:
        QLvsnL = nL+1
    else:
        QLvsnL = QL
    for i in range(QLvsnL):
        pL = int(pL_list[i])
        expectL = pL * i
        revL = rL * expectL
    rev_tot_i = revL + revS
    rev.append(rev_tot_i)

if QL = qL * 5 and QS = qS * T-5 and T - 5 >= 0:
    if QS >= nS+1:
        QSvsnS = nS+1
    else:
        QSvsnS = QS
    for i in range(QSvsnS):
        pS = int(pS_list[i])
        expectS = pS * i
        revS = rS * expectS
    if QL >= nL+1:
        QLvsnL = nL+1
    else:
        QLvsnL = QL
    for i in range(QLvsnL):
        pL = int(pL_list[i])
        expectL = pL * i
        revL = rL * expectL
    rev_tot_i = revL + revS
    rev.append(rev_tot_i)
    
    if QL = qL * 6 and QS = qS * T-6 and T - 6 >= 0:
    if QL = qL * 7 and QS = qS * T-7 and T - 7 >= 0:
    if QL = qL * 8 and QS = qS * T-8 and T - 8 >= 0:
    if QL = qL * 9 and QS = qS * T-9 and T - 9 >= 0:
    if QL = qL * 10 and QS = qS * T-10 and T - 10 >= 0:
    if QL = qL * 11 and QS = qS * T-11 and T - 11 >= 0:
    if QL = qL * 12 and QS = qS * T-12 and T - 12 >= 0:
    if QL = qL * 13 and QS = qS * T-13 and T - 13 >= 0:
    if QL = qL * 14 and QS = qS * T-14 and T - 14 >= 0:
    if QL = qL * 15 and QS = qS * T-15 and T - 15 >= 0:
    if QL = qL * 16 and QS = qS * T-16 and T - 16 >= 0:
    if QL = qL * 17 and QS = qS * T-17 and T - 17 >= 0:
    if QL = qL * 18 and QS = qS * T-18 and T - 18 >= 0:
    if QL = qL * 19 and QS = qS * T-19 and T - 19 >= 0:
    if QL = qL * 20 and QS = qS * T-20 and T - 20 >= 0:
    if QL = qL * 21 and QS = qS * T-21 and T - 21 >= 0:
    if QL = qL * 22 and QS = qS * T-22 and T - 22 >= 0:
    if QL = qL * 23 and QS = qS * T-23 and T - 23 >= 0:
    if QL = qL * 24 and QS = qS * T-24 and T - 24 >= 0:
"""
