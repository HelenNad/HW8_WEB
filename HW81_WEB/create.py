from models import Author, Quotes
import json

if __name__ == '__main__':
    with open("authors.json", "r") as fh:
        raw_expenses = json.load(fh)
        for el in raw_expenses:
            author = Author(fullname=el["fullname"],
                            born_data=el["born_date"],
                            born_location=el["born_location"],
                            description=el["description"]).save()

    with open("quotes.json", "r") as f:
        raw_expenses = json.load(f)
        for e in raw_expenses:
            author = Author.objects(fullname=e["author"])

            quote = Quotes(tags=e["tags"],
                           author=author[0].id,
                           quote=e["quote"]).save()
