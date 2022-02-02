print("\u001b[31m"+"""
\t   _____                      ____                  _     
\t  / ____|      _             |  _ \                | |    
\t | (___  _ __ (_)_ __   ___  | |_) | ___  __ _  ___| |__  
\t  \___ \| '_ \| | '_ \ / _ \ |  _ < / _ \/ _` |/ __| '_ \ 
\t  ____) | |_) | | | | |  __/ | |_) |  __/ (_| | (__| | | |  
\t |_____/| .__/|_|_| |_|\___| |____/ \___|\__,_|\___|_| |_| 
\t        | |                                               
\t        |_|                                               
"""+"\u001b[0m")
print("\t\t\t\t\tCreated by "+"\033[3m"+"Andre Anuszkiewcz"+"\033[0m")
print("\t\t\t\t\t(Please play in Full Screen)")
input("\n\t\t\t\t\t\tPress Enter to Begin ")
print("""\n\n\t\t\t\t\t\t\t6:30 AM, June 6th 1944. \nYou, your brother, and thousands of other men have been bearing the freezing cold of ice and wind on a ship with no roof for hours. Spine Beach finally comes into sight.""")

input()

# ----------------------------------------------------------------
from world import game

def find_current_location(world, pid):
  if "passages" in world:
    for passage in world["passages"]:
      if pid == passage["pid"]:
        return passage
  return {}

# ----------------------------------------------------------------

def render(world, current_location, score, moves):
  if "name" in current_location and "cleanText" in current_location and "links" in current_location:
    print("\n\033[4m" + "Moves: {}, Score: {}".format(moves, score) + "\033[0m")
    print(current_location["cleanText"])
    print()
    for link in current_location["links"]:
      print("({}) {}".format(link["selection"], link["label"]))
        
def get_input():
  response = input("\nWhat do you want to do? "+"\033[2m"+"(type quit to exit) "+"\033[0m")
  return response.upper().strip()

def update(world, current_location, current_pid, response):
  if response == "":
    return current_pid
  if "links" in current_location:
    for link in current_location["links"]:
      if response == link["selection"]:
        return link["pid"]
      if response == link["label"].upper().strip():
        return link["pid"]
  print("I don't know what you are trying to do.")
  return current_pid

# ----------------------------------------------------------------
quit = False
while not quit:
  pid = 0
  if "startnode" in game:
    pid = game["startnode"]
  current_location = {}
  response = ""
  moves = 0
  score = 0

  scores = {
    "9":10
    ,"18":10
    ,"10":10
  }

  while True:
    if response == "QUIT":
      break
    pid = update(game, current_location, pid, response)
    current_location = find_current_location(game, pid)
    render(game, current_location, score, moves)
    if "links" in current_location and len(current_location["links"])== 0:
      break
    response = get_input()
    if pid in scores:
      score += scores[pid]
    
    moves += 1
  print("\nGame Over, thanks for playing!")
  selection = input("\nWould you like to play again?"+"\033[2m"+"(y/n) "+"\033[0m")
  if selection.lower() == "n":
    quit = True
