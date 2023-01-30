import math as m

print("m回中n回x%を引き当てた時の確率を計算するよ")
print("v2。コードがちょっとすっきりした！")
print()

def aho():
  print("ばーか")
def gnn():
  print("ぐぬぬ...")
def tryfloat(x):
  try:
    float(x)
  except ValueError:
    return False
  else:
    return True



nums = input("「m n x」つまり「試行回数 当たりの回数 当たりの確率[%]」となるように入力してね(例:10 3 5): ")

try:
    tries , wins , odds = map(str,nums.split())
except ValueError:
    aho()
else:
    if tries.isdecimal() == False or wins.isdecimal() == False or tryfloat(odds) == False:
        aho()
    else:
        tries = int(tries)
        wins = int(wins)
        odds = float(odds)

        if tries <= 0 or wins < 0 or tries < wins or odds <= 0:
            gnn()
        else:
            odds = odds / 100
            answer = m.factorial(tries) / m.factorial(tries - wins) / m.factorial(wins) * (odds ** wins) * ((1 - odds) ** (tries - wins))
            print(str(round(answer * 100 , 3)) + "%です")