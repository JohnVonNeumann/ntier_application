from django.core import serializers
from django.http import HttpResponse

from data.models import Data


def index(request):
    return HttpResponse("Hello, world. You're at the data index.")

def insert_data(request):
    """ Creates a data entry in the Data model
    Returns the id of the data entry
    """
    insert = Data(first_field="This is random data",
                  second_field="And a criteria hack",
                  third_field="But I'm hoping",
                  fourth_field="That this does the job")
    insert.save()

    return HttpResponse("You have inserted new data. Refresh to add more.\
                         Visit /data/select_data to see the new entries")

def select_data(request):
    """ Selects all data in the Data model
    Returns it back to the user
    """
    select = Data.objects.all()
    select_json = serializers.serialize('json',
                                        select)

    return HttpResponse(select_json, 
                        content_type='application/json')
