try:
    import os, requests, functionality
    from bs4 import BeautifulSoup
except ImportError as error:
    print(f"The following import error occured: {error}")

def main():
    modulo= functionality.functionality()

    os.system("cls")
    varia= []
    urlsOriginales= ["https://www.theverge.com/", "https://www.phoronix.com/", "https://es.gizmodo.com/", "https://www.engadget.com/"]
    misPosts= []

    for i in urlsOriginales:
        htmlRes= requests.get(i)
        sopa= BeautifulSoup(htmlRes.content, "html.parser")

        nuevo= sopa.find_all(href= True)#Lo que tengo igualado en mi href es para quitar los None´s en caso de que hayan.
        for i in nuevo:
            temp= i.get("href")
            if ("rss" in temp) and ("https" in temp):
                varia.append(temp)
    
    #print(varia)
    for j in varia:
        misPosts.append(modulo.feedsEntries(j))
    
    if misPosts:
        modulo.archivoJSON(misPosts)
        print("Creation of the JSON file succeed!!")
    else:
        print("There´s no data")

if __name__== "__main__":
    try:
        main()
    except Exception as e:
        os.system("cls")
        print(f"The following error ocurred: {e}")