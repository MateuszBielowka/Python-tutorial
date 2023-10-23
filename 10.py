x = 0
y = 12

try:
    print(y/x)
    print("Grają")
except (ZeroDivisionError, TypeError):
    print("Grają - Niegrają, nastąpiło dzielenie przez zero")
print("Śpiff")