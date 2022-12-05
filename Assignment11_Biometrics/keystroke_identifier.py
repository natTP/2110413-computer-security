import keyboard
import json
import math
import numpy as np
from numpy.linalg import norm

def save_digraph_as_json(filename, digraph):
  digraph_json = json.dumps(digraph, indent=4)
  with open(filename, "w") as file:
    file.write(digraph_json)


def read_digraph_json(filename):
  digraph = {}
  with open(filename, "r") as file:
    digraph = json.load(file)
  return digraph


def record_digraph(digraph, times):
  print('\nType this paragraph, then press esc. on finish: (do not mind errors)\n')
  print('the quick brown fox jumps over the lazy dog.')
  # print('the quick brown fox jumps over the lazy dog. waltz, bad nymph, for quick jigs vex. sphinx of black quartz, judge my vow. how vexingly quick daft zebras jump!')

  events = keyboard.record(until='escape')
  down_events = []
  for e in events:
    if e.event_type == 'down':
      down_events.append(e)

  for i in range(len(down_events)):
    if i == 0: 
      continue
    charpair = down_events[i-1].name + down_events[i].name
    interval = (down_events[i].time - down_events[i-1].time) * 1000
    if charpair in digraph:
      digraph[charpair] += interval
      times[charpair] += 1
    else:
      digraph[charpair] = interval
      times[charpair] = 1

  # total time
  total_time = (down_events[-1].time - down_events[0].time) * 1000
  if '_total' in digraph:
    digraph['_total'] += total_time
    times['_total'] += 1
  else:
    digraph['_total'] = total_time
    times['_total'] = 1

  for key in digraph:
    digraph[key] /= times[key]
    print(key, digraph[key], times[key])
  print()


def compare_digraph_euclidean(input, baseline):
  diff = 0
  for key in baseline.keys():
    if key in input:
      diff += (input[key] - baseline[key]) ** 2
    # else: 
    #   diff += baseline[key] ** 2
  diff = math.sqrt(diff)
  return 1 / (1+diff)


def compare_digraph_cosine(input, baseline):
  input_sorted = dict(sorted(input.items()))
  baseline_sorted = dict(sorted(baseline.items()))

  input_vect = []
  baseline_vect = []

  for key in baseline_sorted.keys():
    if key in input_sorted:
      input_vect.append(input[key])
      baseline_vect.append(baseline[key])
  
  input_vect = np.array(input_vect) 
  baseline_vect = np.array(baseline_vect)
  return np.dot(input_vect, baseline_vect)/(norm(input_vect)*norm(baseline_vect))

# ----- Program Start -----

digraph = {}
times = {}

user = input("Input your name (this is used for identification). ")

for i in range(5):
  record_digraph(digraph, times)

save_digraph_as_json("digraph_" + user + ".json", digraph)

for key in digraph:
    print(key, digraph[key], times[key])

digraph_jop = read_digraph_json("digraph_jop.json")
digraph_anon = read_digraph_json("digraph_Anon.json")
digraph_mom = read_digraph_json("digraph_sonia.json")

diff_jop = compare_digraph_cosine(digraph, digraph_jop)
diff_anon = compare_digraph_cosine(digraph, digraph_anon)
diff_mom = compare_digraph_cosine(digraph, digraph_mom)


print("similarity btw Jop and Anon: ", compare_digraph_cosine(digraph_anon, digraph_jop))
print("similarity btw Jop and Mom: ", compare_digraph_cosine(digraph_mom, digraph_jop))

print("similarity to Jop: ", diff_jop)
print("similarity to Anon: ", diff_anon)
print("similarity to Mom: ", diff_mom)