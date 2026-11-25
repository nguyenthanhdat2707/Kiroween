import json,statistics as st
W=[20,20,20,15,10,10,5]; K=["Auth","Tech","Mech","Ctx","Fresh","Repro","Bias"]
def w(s): return sum(a*b for a,b in zip(W,s))/5
# (pair, claim, agent scores, coordinator scores, note)
P=[
("A·R02","A-P1-C1",[4,3,4,5,5,5,4],[3,4,4,5,5,4,5],"trade press relaying Yahoo announcement"),
("A·R05","A-P1-C2",[5,5,4,4,5,5,5],[5,5,3,3,5,4,5],"platform-use data; does not measure overload of professional monitors"),
("A·R06","A-P1-C2",[5,5,4,4,5,5,5],[5,5,3,3,5,4,5],"US adults' news fatigue; fatigue != demand for tools"),
("A·R12","A-P2-C2",[5,4,4,4,4,5,2],[5,4,3,3,3,5,3],"enterprise deal (2024) used for end-user gap claim"),
("A·R19","A-P4-C1",[5,5,5,5,5,5,3],[5,4,4,5,5,5,4],"Mozilla's own shutdown notice"),
("A·R21","A-P4-C2",[5,5,5,5,4,5,5],[5,5,5,4,4,5,5],"general web pages, not personal bookmark sets"),
("A·R22","A-P4-C3",[5,5,5,5,5,5,4],[5,4,4,5,5,4,4],"vendor policy page; may change"),
("A·R39","A-P7-C1",[3,4,4,5,5,5,3],[2,3,3,5,5,3,3],"SEO-agency blog relaying counts"),
("A·R40","A-P7-C2",[5,5,4,5,5,5,3],[5,5,3,4,5,4,3],"self-reported survey; publisher has a stake"),
("B·R01","B-P1-C5",[4,5,4,5,5,3,3],[4,5,4,5,5,3,3],"workshop paper; advocacy framing; not reproduced"),
("B·R02","B-P1-C1",[3,2,3,5,4,4,4],[3,4,4,5,5,4,5],"relays Spotify's dates verbatim"),
("B·R03","B-P1-C2",[3,3,4,5,5,4,4],[3,4,4,5,5,4,5],"news report of App Store change"),
("B·R04","B-P1-C4",[3,3,4,4,5,4,4],[3,4,4,5,5,4,5],"news report with Google date"),
("B·R13","B-P4-C1",[4,3,4,5,2,4,5],[4,3,4,4,2,4,5],"Nature feature 2021; anecdotal; stale for 2026"),
("B·R14","B-P4-C2",[4,4,5,5,4,4,5],[5,4,5,5,4,4,5],"institution documenting its own practice"),
("B·R20","B-P6-C2",[5,5,4,3,4,5,5],[5,5,5,4,4,5,5],"SAME SOURCE as A·R21"),
("C·R01","C-P1-C1",[5,2,3,5,5,5,3],[5,4,3,5,5,5,3],"official notice; stated reasons unevidenced"),
("C·R04","C-P1-C5",[5,4,4,5,4,4,2],[5,4,4,5,4,4,3],"vendor doc of own feature limits"),
("C·R05","C-P1-C4",[5,3,4,4,4,4,2],[5,3,3,4,4,4,2],"marketing feature page"),
("C·R21","C-P4-C3",[5,4,4,5,5,4,5],[5,4,4,5,5,5,5],"DHSC guidance with commissioned sample data"),
("C·R25","C-P4-C5",[5,3,4,4,5,2,1],[5,3,3,4,4,4,2],"provider PR on own pilot"),
("C·R26","C-P4-C5",[5,4,5,5,5,4,5],[5,4,4,5,4,5,5],"gov action plan Feb 2025"),
]
res={}
rows=[]
for pid,cl,a,c,n in P:
    ag=pid[0]; d=w(a)-w(c)
    res.setdefault(ag,[]).append((d,[x-y for x,y in zip(a,c)]))
    rows.append((pid,cl,a,round(w(a)),c,round(w(c)),round(d),n))
for r in rows: print("|".join(map(str,r)))
print()
summ={}
for ag,v in sorted(res.items()):
    ds=[x[0] for x in v]; crit=[round(st.mean([x[1][i] for x in v]),2) for i in range(7)]
    summ[ag]=dict(n=len(v),mean_offset=round(st.mean(ds),1),median_offset=round(st.median(ds),1),min=round(min(ds)),max=round(max(ds)),per_criterion=dict(zip(K,crit)))
    print(ag,summ[ag])
json.dump(dict(rows=rows,summary=summ),open(__import__("sys").argv[1],"w"),ensure_ascii=False,indent=1)
