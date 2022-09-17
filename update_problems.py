import os
import requests

result = os.listdir('./')

all_problems = []

for i in result:
    if i.split()[0] != "Week": continue
    all_files = os.listdir(f'./{i}')
    py_files = [i for i in all_files if i[-3:] == ".py"]
    link = [i.strip() for i in open(f'./{i}/problem.txt').readlines()]
    difficulty = [int(i.strip()) for i in open(f'./{i}/difficulty.txt').readlines()]

    week_prob = {}
    for j in range(len(link)):
        res_diff = 0
        if j < len(difficulty):
            res_diff = difficulty[j]
        prob_name = py_files[j].split('-')[1][:-3]
        week_prob[prob_name] = {
            "number": j+1,
            "name": prob_name,
            "link": link[j],
            "difficulty": res_diff
        }
    
    all_problems.append({
        "week_no": int(i.split()[1]),
        "title": i[10:],
        "problems": week_prob
    })

requests.put('http://192.168.0.2:8000/mint-tutor/problems',json=all_problems)
# requests.put('http://localhost:8000/mint-tutor/problems',json=all_problems)
print("***UPDATE COMPLETED!***")