import os,re,os.path,threading
from requests import session
ss = session()
if not os.path.exists('Images'):
    os.makedirs('Images')
def crawlImg(keyword):
    api = f'https://de.images.search.yahoo.com/yhs/search?hspart=1und1&hsimp=yhs-gmx_image&vm=r&type=image&p={keyword}'
    crawlData = ss.get(api)
    try:
        imangeData = re.findall("'aria-label='(.*?)&pid=Api",crawlData.text)
        if len(imangeData) == 0:
            pass
        else:
            for x in imangeData:
                imgLink = x.split("'><img data-src='")[1]
                name = imgLink.split('id=')[1]
                imageContent = ss.get(imgLink).content
                with open(f'Images\{keyword}_{name}.png','wb') as saveImg:
                    saveImg.write(imageContent)
                    print(f"Lưu thành công: {keyword}|{name}")
    except:
        pass
def runTools(thread_step):
    for i in range(thread_step,len(keywordFile),threadCount):
        keyword = keywordFile[i].strip()
        crawlImg(keyword)
threadCount = 10
keywordFile = open('key.txt','r',encoding='utf-8').readlines()
for x in range(threadCount):
    newThread = threading.Thread(target=runTools,args=(x,))
    newThread.start()