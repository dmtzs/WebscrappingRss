try:
    import feedparser, json
except ImportError as error:
    print(f"The following import error occured: {error}")

class functionality():
    def feedsEntries(self, urlRss):
        contador= 0
        #"https://www.theverge.com/rss/front-page/index.xml", "https://www.phoronix.com/rss.php", "https://es.gizmodo.com/rss", "https://www.engadget.com/rss.xml"
        nuevoFeed= feedparser.parse(urlRss)
        tagsEntries= nuevoFeed.entries
        postDetalles= {"Blog title": nuevoFeed.feed.title}
        #print(tagsEntries)

        listaPosts= self.entries(tagsEntries, contador)

        postDetalles["posts"]= listaPosts

        return postDetalles

    def entries(self, tagsEntries, contador):
        listaPosts= []
        for i in tagsEntries:
            if contador== 10:
                break
            else:
                diccionario= dict()
                try:
                    diccionario["Title"]= i.title
                    diccionario["Published"]= i.published
                    diccionario["Link"]= i.link
                    contador+= 1
                except Exception as e:
                    print(f"The following error ocurred: {e}")

                listaPosts.append(diccionario)
        return listaPosts

    def archivoJSON(self, misPosts):
        with open("results.json", "w") as file:
            for x in misPosts:
                json.dump(x, file, indent= 4)