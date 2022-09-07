import os
import os.path

def dfs_showdir(path, depth=0):
    if depth == 0:
        print("root:[" + path + "]")

    for item in os.listdir(path):
        print("| " * depth + "--" + item)

        newitem = path +'/'+ item
        if os.path.isdir(newitem):
            dfs_showdir(newitem, depth +1)


if __name__ == '__main__':
    dfs_showdir('')
