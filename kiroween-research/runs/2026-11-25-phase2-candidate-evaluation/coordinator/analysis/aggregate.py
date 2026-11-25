"""Phase 2C aggregation and sensitivity analysis. Deterministic (seeded)."""
import json,random,statistics as st,itertools,sys,os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
K=["demand","international","innovation","theme","ai","feasibility","demo","sustainability"]
W0=dict(zip(K,[20,15,15,15,10,10,10,5]))
C=["A-P1","A-P2","A-P4","A-P7","B-P1","B-P4","C-P1","C-P4"]
AG="abc"
pre={x:json.load(open(f"{R}/agent-{x}/scores.json"))["candidates"] for x in AG}
post={x:json.load(open(f"{R}/agent-{x}/scores-revised.json"))["candidates"] for x in AG}
def tot(s,W): return sum(W[k]*s[k] for k in K)/sum(W.values())*100/5
S={c:{k:[post[x][c]["scores"][k]["score"] for x in AG] for k in K} for c in C}
CF={c:{k:[post[x][c]["scores"][k]["confidence"] for x in AG] for k in K} for c in C}
def agg(c,W,mode="mean"):
    f=st.mean if mode=="mean" else st.median
    return tot({k:f(S[c][k]) for k in K},W)
def gate(c): return st.median(S[c]["theme"])>=3
def top3(W,mode="mean",use_gate=True,scores=None):
    sc=scores or {c:agg(c,W,mode) for c in C}
    el=[c for c in C if (gate(c) or not use_gate)]
    return tuple(sorted(el,key=lambda c:-sc[c])[:3]),sc
out={}
# 1. base
base,bs=top3(W0); out["base_top3"]=base
out["table"]={c:{"pre_totals":[pre[x][c]["weighted_total"] for x in AG],"post_totals":[post[x][c]["weighted_total"] for x in AG],
  "mean_total":round(bs[c],1),"median_crit_total":round(agg(c,W0,"median"),1),"theme_scores":S[c]["theme"],"gate_pass_median":gate(c),
  "gate_by_agent":[post[x][c]["theme_gate_pass"] for x in AG],
  "spread_criteria":{k:S[c][k] for k in K if max(S[c][k])-min(S[c][k])>=2},
  "low_conf_count":sum(cf.count("L") for cf in CF[c].values())} for c in C}
# changes pre->post
out["changes"]={x:{c:post[x][c].get("changes",[]) for c in C if post[x][c].get("changes")} for x in AG}
# 2. median-aggregation top3
out["median_top3"]=top3(W0,"median")[0]
# 3. per-agent top3
out["per_agent_top3"]={x:tuple(sorted([c for c in C if post[x][c]["theme_gate_pass"]],key=lambda c:-post[x][c]["weighted_total"])[:3]) for x in AG}
# 4. ±5pp one-at-a-time
oat=[]
for k in K:
    for d in (-5,5):
        W=dict(W0); W[k]=max(0,W[k]+d)
        t=top3(W)[0]; oat.append((k,d,t,t==base, set(t)==set(base)))
out["oat_pm5"]=oat
# 5. leave-one-out and equal
loo=[]
for k in K:
    W=dict(W0); W[k]=0; t=top3(W)[0]; loo.append((k,t,set(t)==set(base)))
out["leave_one_out"]=loo
out["equal_weights"]=top3({k:1 for k in K})[0]
out["no_gate"]=top3(W0,use_gate=False)[0]
# 6. Dirichlet weight draws around W0
random.seed(20261125); N=20000; cnt={c:0 for c in C}; same=0; alpha=40
for _ in range(N):
    g={k:random.gammavariate(alpha*W0[k]/100,1) for k in K}; s=sum(g.values()); W={k:g[k]/s*100 for k in K}
    t=top3(W)[0]; same+= set(t)==set(base)
    for c in t: cnt[c]+=1
out["dirichlet_weights"]={"N":N,"alpha":alpha,"top3_set_same_as_base":round(same/N,3),"freq_in_top3":{c:round(v/N,3) for c,v in cnt.items()}}
# 7. score uncertainty: per criterion pick one agent's score at random (agent disagreement as uncertainty)
random.seed(7); cnt={c:0 for c in C}; same=0
for _ in range(N):
    sc={}
    for c in C:
        sc[c]=tot({k:random.choice(S[c][k]) for k in K},W0)
    t=top3(W0,scores=sc)[0]; same+=set(t)==set(base)
    for c in t: cnt[c]+=1
out["score_resampling"]={"N":N,"top3_set_same_as_base":round(same/N,3),"freq_in_top3":{c:round(v/N,3) for c,v in cnt.items()}}
# 8. joint: weights + scores + low-confidence +/-1 jitter
random.seed(11); cnt={c:0 for c in C}; same=0
for _ in range(N):
    g={k:random.gammavariate(alpha*W0[k]/100,1) for k in K}; s=sum(g.values()); W={k:g[k]/s*100 for k in K}
    sc={}
    for c in C:
        d={}
        for k in K:
            i=random.randrange(3); v=S[c][k][i]
            if CF[c][k][i]=="L": v=min(5,max(0,v+random.choice((-1,0,1))))
            d[k]=v
        sc[c]=tot(d,W)
    t=top3(W,scores=sc)[0]; same+=set(t)==set(base)
    for c in t: cnt[c]+=1
out["joint_uncertainty"]={"N":N,"top3_set_same_as_base":round(same/N,3),"freq_in_top3":{c:round(v/N,3) for c,v in cnt.items()}}
json.dump(out,open(f"{R}/coordinator/analysis/aggregate-results.json","w"),indent=1,ensure_ascii=False,default=list)
print(json.dumps({k:out[k] for k in ("base_top3","median_top3","per_agent_top3","equal_weights","no_gate","dirichlet_weights","score_resampling","joint_uncertainty")},indent=1,default=list))
for c in C: print(c,out["table"][c])
print("OAT changes:",[o[:3] for o in oat if not o[4]])
print("LOO changes:",[l[:2] for l in loo if not l[2]])
