from models import Quotes, Author
from bson import ObjectId

if __name__ == '__main__':
    while True:
        command = input("Enter your command (command:value): ")

        command = command.split(":")
        com = []
        for el in command:
            com.append(el.strip())

        if com[0] == "exit":
            break

        elif com[0] == "name":
            author = Author.objects(fullname=com[1])

            quotes = Quotes.objects(author=ObjectId(author[0].id))
            q = []
            for quote in quotes:
                q.append(quote.quote)
            print(q)
        elif com[0] == "tag" or "tags":
            try:
                com[1] = com[1].split(",")
                print(com[1])
                q = []
                for c in com[1]:
                    quotes = Quotes.objects(tags=c)

                    for quote in quotes:
                        q.append(quote.quote)
                print(q)
            except IndexError:
                pass

        else:
            print("You wrong!")
