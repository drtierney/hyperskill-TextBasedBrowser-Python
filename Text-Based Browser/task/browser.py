import os
import argparse


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''

# write your code here
parser = argparse.ArgumentParser()
parser.add_argument("dir_for_files")
args = parser.parse_args()

if not os.access(args.dir_for_files, os.F_OK):
    os.mkdir(args.dir_for_files)

urls = {"bloomberg.com": bloomberg_com, "nytimes.com": nytimes_com}
tabs = set()

while True:
    url = input()
    site = url.split(".")[0]
    filepath = os.path.join(args.dir_for_files, site)

    if url == "exit":
        exit()
    if url in urls.keys() and site not in tabs:
        print(urls[url])
        with open(filepath, "w") as f:
            f.write(urls[url])
        tabs.add(site)
    if site in tabs:
        with open(filepath, "r") as f:
            lines = f.readlines()
            for line in lines:
                print(line.strip())
    else:
        print("Error: Incorrect URL")
