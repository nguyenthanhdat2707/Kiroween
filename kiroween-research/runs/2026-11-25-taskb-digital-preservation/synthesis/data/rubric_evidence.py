import json,os
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
K=["demand","international","innovation","theme","ai","feasibility","demo","sustainability"]
rows=[]
for x in "abc":
    for o in json.load(open(f"{R}/agent-{x}/opportunities-revised.json"))["opportunities"]:
        e=o["rubric_evidence"]
        rows.append([o["id"],o.get("status")]+[f'{e[k]["provisional_score"]}{e[k]["confidence"]}' for k in K]+[",".join(o["regions_with_direct_evidence"]),", ".join(o["key_claims"][:6])])
print("| Opp | Status | "+" | ".join(K)+" | Regions (direct evidence) | Key claims |")
print("|"+"---|"*(len(K)+4))
for r in rows: print("| "+" | ".join(r)+" |")
