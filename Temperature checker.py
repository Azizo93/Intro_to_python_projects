name = input("What is your name?: ")
temp = int(input("What is the temperature in degrees celsius?: "))

if temp <= 10:
    print(f"Hi {name}, the teperature is currently {temp} degrees celsius. Its cold outside, bring a jacket!")
elif temp >= 20:
    print(f"Hi {name}, the teperature is currently {temp} degrees celsius. It's hot outside, make sure to wear sunscreen!")
elif temp > 10:
    print(f"Hi {name}, the teperature is currently {temp} degrees celsius. It's nice outside!")




