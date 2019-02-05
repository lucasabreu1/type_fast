from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Frase
from .serializers import FraseSerializer
import json
from django.db.models import Max

import random

def fraseRandom(request):
	frases = getRandom()
	serializer = FraseSerializer(frases)
	return JsonResponse(serializer.data, json_dumps_params={"ensure_ascii":False})


def getRandom():
	max_id = Frase.objects.all().aggregate(max_id=Max("id"))['max_id']
	while True:
		pk = random.randint(1, max_id)
		frase = Frase.objects.filter(pk=pk).first()
		if frase:
			return frase