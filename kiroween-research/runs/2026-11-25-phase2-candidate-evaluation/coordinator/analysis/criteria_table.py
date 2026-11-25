import json,os,sys
R=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
K=["demand","international","innovation","theme","ai","feasibility","demo","sustainability"]
P={x:json.load(open(f"{R}/agent-{x}/scores-revised.json"))["candidates"] for x in "abc"}
print("| Candidate | "+" | ".join(K)+" |"); print("|---"*(len(K)+1)+"|")
for c in ["A-P1","A-P2","A-P4","A-P7","B-P1","B-P4","C-P1","C-P4"]:
    print(f"| {c} | "+" | ".join("/".join(str(P[x][c]["scores"][k]["score"]) for x in "abc") for k in K)+" |")
