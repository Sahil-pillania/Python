def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("There is an error.")


a = increment('df364')
print(a)
