import registrator.registrator as registrator
from datetime import datetime

from mongoengine import EmbeddedDocument, Document, CASCADE
from mongoengine.fields import  DateField,\
                                EmbeddedDocumentField,\
                                ListField,\
                                StringField,\
                                ReferenceField



class Author(Document):
    fullname = StringField(unique=True)
    born_date = DateField()
    born_location = StringField()
    description = StringField()
    meta = {'collection': 'authors'}


class Tag(EmbeddedDocument):
    name = StringField()



class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)#, dbref=True)
    quote = StringField(unique=True)
    tags = ListField(EmbeddedDocumentField(Tag))
    meta = {'collection': 'quotes'}

class MODELS(registrator.REGISTRATOR):    ...
MODELS.register("", __name__, globals(), Document ,["__builtins__",], False)
registry = MODELS()
