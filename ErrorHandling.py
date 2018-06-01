
try:
    f = open('aaa.text')
except FileNotFoundError:
    print('cannot open file')
except Exception as e:
    print(f'something went wrong : {e}')
else:
    print("try closure does not raise any error")
    f.read()
finally:
    f.close()

