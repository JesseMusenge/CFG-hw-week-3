import time

base_url = "https://codefirstgirls.com/"
courses_url = base_url + "courses" 
opportunities_url = base_url + "opportunities"
cfgdegree_url = courses_url + "/cfgdegree"
ambassadors_url = opportunities_url + "/ambassadors"

url = base_url

while True:

  print("You are currently on the URL", url)
  
  if url == base_url:
    print("Where are you clicking? Options: Courses, Opportunities")
    choice = input()
    if choice == "Courses":
      url = courses_url
    elif choice == "Opportunities":
      url = opportunities_url

  elif url == courses_url:
    print("Where are you clicking? Options: CFGDegree, Back")
    choice = input()
    if choice == "CFGDegree":
      url = cfgdegree_url
    elif choice == "Back":
      url = base_url

  elif url == opportunities_url:
    print("Where are you clicking? Options: Ambassadors, Back")
    choice = input()
    if choice == "Ambassadors":
      url = ambassadors_url
    elif choice == "Back":
      url = base_url

  elif url == cfgdegree_url or url == ambassadors_url:
    print("Where are you clicking? Options: Back")
    input()
    url = base_url

  print()
  time.sleep(1)

""" 
The time complexity of the above solution is O(n), where n is the number of times the user clicks on a link. This is because the code has to iterate over the list of available options each time the user clicks on a link. Each iteration does O(1) work printing, getting input, updating the URL. So overall it is linear time O(N).

The space complexity of the above solution is O(1), where 1 is the number of URLs that we need to consider. This is because the code only needs to store the current URL, and this can be done in constant space.

Assumptions:
The user will always provide valid input when prompted. No input validation is done.
Only a limited set of hard-coded URL options are supported.
The user will not try to go back to the base URL from the base URL. The backing website is assumed to be stable and not fail. 
 """
