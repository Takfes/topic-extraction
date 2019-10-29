

import os
# import shutil
# shutil.copy(oldname,newname)

# os.chdir("\\".join([os.getcwd(),"projects\\WebScraping\\kdnuggets"]))

base = r"C:\Users\takis\Desktop\PyR\projects\WebScraping\kdnuggets\www.kdnuggets.com"
year = os.listdir("./projects/WebScraping/kdnuggets/www.kdnuggets.com")
month = [str(x).zfill(2) for x in range(1,13)]
excl = ['webinar','top-tweets','top-news','new_book','interview','index','news','bootcamp','article',"book"]
dest_dir = r"C:\Users\takis\Desktop\PyR\projects\WebScraping\kdnuggets\clean"

for y in year:
    for m in month:
        cur_dir = "\\".join([base,y,m])
        for file in os.listdir(cur_dir):
            if not any(e in file for e in excl):
                try:
                    oldname = "\\".join([cur_dir, file])
                    if not os.path.isdir(oldname):
                        if file.endswith(".html.txt"):
                            newsuff = ".".join(file.split("\\")[-1:][0].split(".")[:2])
                            newname = "\\".join([dest_dir, newsuff])
                            os.rename(oldname, newname)
                        if file.endswith(".html"):
                            newname = "\\".join([dest_dir, file])
                            os.rename(oldname, newname)
                except Exception as e:
                    pass
                    # print(e)










