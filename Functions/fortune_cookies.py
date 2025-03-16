# Write code below 💖
import random

options = [
  'keep working hard, you will get rewarded soon!',
  'good good study, day day up',
  "Don't just think. Act!",
  "All things are difficult before they are easy.",
  "Island Matcha Latte"]

def fortune_cookie():
  random_fortune_cookie = random.randint(0, len(options) - 1)
  print(options[random_fortune_cookie])
fortune_cookie()
