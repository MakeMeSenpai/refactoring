"""Remove control flag"""
# by Kami Bigdely
# Reference: https://stackoverflow.com/a/10140333/81306
# This code snippet reads up to the end of the file

n = 16
with open('foobar.file', 'rb') as fp:
    running = True
    while running:
        chunk = fp.read(n)
        if chunk == '':
            # end of file, stop running.
            running = False
        # process(chunk)
        print(chunk)
