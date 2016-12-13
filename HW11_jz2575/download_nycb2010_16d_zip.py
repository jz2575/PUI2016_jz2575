import os
def download_nycb2010_16d_zip():
    os.system("curl -O http://www1.nyc.gov/assets/planning/download/zip/data-maps/open-data/nycb2010_16d.zip") 
    os.system("mv " + "nycb2010_16d.zip " + os.getenv("PUIDATA")+"/nycb2010_16d.zip")
    os.system("unzip " + os.getenv("PUIDATA")  + "/nycb2010_16d.zip -d " + os.getenv("PUIDATA"))
    os.system("rm " + os.getenv("PUIDATA") + "/nycb2010_16d.zip")

