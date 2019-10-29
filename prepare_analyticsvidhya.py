
import os
# os.path.getsize('C:\\Python27\\Lib\\genericpath.py')



base = r"C:\Users\takis\Desktop\PyR\projects\WebScraping\analyticsvidhya\www.analyticsvidhya.com\blog"
os.listdir(base)
year = ['2013', '2014', '2015', '2016', '2017', '2018']

# excl = ['webinar','top-tweets','top-news','new_book','interview','index','news','bootcamp','article',"book"]
dest_dir = r"C:\Users\takis\Desktop\PyR\projects\WebScraping\analyticsvidhya\clean"

root_folders_to_parse = ["\\".join([base,y]) for y in year]

for folder in root_folders_to_parse:
    for c1 in os.listdir(folder): # 04,05,..12
        for c2 in os.listdir("\\".join([folder,c1])): # name of named folders
            if "index.html" in os.listdir("\\".join([folder,c1,c2])):
                oldname = "\\".join([folder, c1, c2,"index.html"])
                if os.path.getsize(oldname)>20:
                    # print(f"file: {oldname} is empty")
                    newname = "\\".join([dest_dir,c2+".html"])
                    # print(newname)
                    os.replace(oldname,newname)

jobstring = '-years-experience'
jobposts = r'C:\Users\takis\Desktop\PyR\projects\WebScraping\analyticsvidhya\clean\probablejobposts'
for html in os.listdir(dest_dir):
    # print(html)
    if jobstring in html:
        # print("FOUND ONE!!!!")
        fullname = "\\".join([dest_dir,html])
        newfull  = "\\".join([dest_dir,"probablejobposts",html])
        # print(fullname)
        # print(newfull)
        # print()
        # print()
        os.replace(fullname,newfull)











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
