def pangrams(s):
    return "pangram" if set('abcdefghijklmnopqrstuvwxyz') <= set(s.lower()) else "not pangram"
if __name__ == "__main__":
    input_string = input()
    print(pangrams(input_string))
