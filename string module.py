# Sample string
my_str = "Hello, World!"

print("capitalize() =", my_str.capitalize())  # capitalize() = Hello, world!
print("casefold() =", my_str.casefold())      # casefold() = hello, world!
print("center() =", my_str.center(20, '-'))   # center() = ----Hello, World!-----
print("count('o') =", my_str.count('o'))      # count('o') = 2
print("encode() =", my_str.encode())          # encode() = b'Hello, World!'
print("endswith('!') =", my_str.endswith('!')) # endswith('!') = True
print("expandtabs(4) =", "Hello\tWorld".expandtabs(4))  # expandtabs(4) = Hello   World
print("find('World') =", my_str.find('World')) # find('World') = 7
print("format() =", "Hello, {}!".replace('{}', 'Alice')) # format() = Hello, Alice!
print("format_map() =", "{name} is {age} years old".replace('{name}', 'Alice').replace('{age}', '23')) # format_map() = Alice is 23 years old
print("index('World') =", my_str.index('World')) # index('World') = 7
print("isalnum() =", my_str.isalnum())        # isalnum() = False
print("isalpha() =", my_str.isalpha())        # isalpha() = False
print("isascii() =", my_str.isascii())        # isascii() = True
print("isdecimal() =", my_str.isdecimal())    # isdecimal() = False
print("isdigit() =", my_str.isdigit())        # isdigit() = False
print("isidentifier() =", my_str.isidentifier()) # isidentifier() = False
print("islower() =", my_str.islower())        # islower() = False
print("isnumeric() =", my_str.isnumeric())    # isnumeric() = False
print("isprintable() =", my_str.isprintable())# isprintable() = True
print("isspace() =", my_str.isspace())        # isspace() = False
print("istitle() =", my_str.istitle())        # istitle() = False
print("isupper() =", my_str.isupper())        # isupper() = False
print("join() =", ", ".join(['Hello', 'World'])) # join() = Hello, World
print("ljust(20, '-') =", my_str.ljust(20, '-')) # ljust(20, '-') = Hello, World!-------
print("lower() =", my_str.lower())            # lower() = hello, world!
print("lstrip('H') =", my_str.lstrip('H'))    # lstrip('H') = ello, World!
print("maketrans() and translate() =", my_str.translate(str.maketrans('H', 'J'))) # maketrans() and translate() = Jello, World!
print("partition(' ') =", my_str.partition(' ')) # partition(' ') = ('Hello,', ' ', 'World!')
print("replace('World', 'Everyone') =", my_str.replace('World', 'Everyone')) # replace('World', 'Everyone') = Hello, Everyone!
print("rfind('o') =", my_str.rfind('o'))      # rfind('o') = 8
print("rindex('o') =", my_str.rindex('o'))    # rindex('o') = 8
print("rjust(20, '-') =", my_str.rjust(20, '-')) # rjust(20, '-') = -------Hello, World!
print("rsplit(', ') =", my_str.rsplit(', '))  # rsplit(', ') = ['Hello', 'World!']
print("rstrip('!') =", my_str.rstrip('!'))    # rstrip('!') = Hello, World
print("split(', ') =", my_str.split(', '))    # split(', ') = ['Hello', 'World!']
print("splitlines() =", "Hello\nWorld".splitlines()) # splitlines() = ['Hello', 'World']
print("startswith('Hello') =", my_str.startswith('Hello')) # startswith('Hello') = True
print("strip('!') =", my_str.strip('!'))      # strip('!') = Hello, World
print("swapcase() =", my_str.swapcase())      # swapcase() = hELLO, wORLD!
print("title() =", my_str.title())            # title() = Hello, World!
print("translate(str.maketrans('World', 'Earth')) =", my_str.translate(str.maketrans('World', 'Earth'))) # translate(str.maketrans('World', 'Earth')) = Hello, Earth!
print("upper() =", my_str.upper())            # upper() = HELLO, WORLD!
print("zfill(20) =", my_str.zfill(20))        # zfill(20) = 0000000Hello, World!

