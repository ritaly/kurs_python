import os
import glob

def sorted_list():
    search_dir = '.'
    files = filter(os.path.isfile, glob.glob( + "*"))
    files.sort(key=lambda x: os.path.getmtime(x))
# Function to rename multiple files
def main():
    num = 1

    for filename in os.listdir('.'):
        if 'webhd_720p' not in filename:
            continue

        dst = "RPG(" + str(num) + ").mp4"
        src = filename
        dst = dst

        os.rename(src, dst)
        num += 1


if __name__ == '__main__':
    main()