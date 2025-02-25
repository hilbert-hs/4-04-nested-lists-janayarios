# shopping list
shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]

# functions

def updateItem(_shoppingList):
    row = int(input("Which list do you want to update?: "))
    col = int(input("Which item in the list do you want to update?: "))
    new_item = input("What is the new item?: ")
    _shoppingList[row - 1][col - 1] = new_item
    print(_shoppingList)

def viewItem(_list):
    row = int(input("Which list do you want to select?: "))
    col = int(input("Which item in the list do you want to see?: "))
    print(_list[row - 1][col - 1])

def viewList(_list):
  row = int(input("What list do you want to see?"))
  # print(_list[row - 1])
  viewFormatList = ""
  for item in _list[row - 1]:
    viewFormatList += f" {item}"
  return(viewFormatList)


def consolidateLists(_list):
  newList = []
  for list in _list:
    for item in list:
      newList.append(item)
  return(newList)

def numItem(_list):
  count = 0
  userItem = input("What item do you want a count of?: ")
  for list in _list:
    for item in list:
      if item == userItem:
         count += 1
  return(count)

def addMilk(_list):
  for list in _list:
    if 'milk' not in list:
      list.append("milk")
  return(_list)

def milkAndCookies(_list):
  for i in range(0, len(_list)):
    for j in range(0, len(_list[i])):
      if _list[i][j] == "milk":
        _list[i][j] += " and cookies"
  return(_list)
         
# user inputs

updateItem(shopping_cart)
viewItem(shopping_cart)
print(viewList(shopping_cart))
print({consolidateLists(shopping_cart)})
print(numItem(shopping_cart))
print(addMilk(shopping_cart))
print(milkAndCookies(shopping_cart))



# functions

