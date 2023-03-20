from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
import json

# READ DE TODOS


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':

        users = User.objects.all()                                            

                                                                 
        serializer = UserSerializer(users, many=True)                        # Serialize os dados do objeto em json
                                                                                
        return Response(serializer.data)                                     #  Retorna os dados serializados

    return Response(status=status.HTTP_404_NOT_FOUND)


# Mostrar Por Nick (Primary Key)


@api_view(['GET'])
                                                           
def get_by_nick(request, nick):                                  # nick variavel que foi passado pela url
    try:
        user = User.objects.get(pk=nick)
    except:
                                                            
        return Response(status=status.HTTP_404_NOT_FOUND)       # se o usuario for encontrado vai estar dentro da variavel USER

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):
    # CRIANDO DADOS

    if request.method == 'POST':                         

        new_user = request.data                                                  # os dados do novo usuario vão vir nos dados do request

        serializer = UserSerializer(data=new_user)                               # serealizando dados agora que vem da requisicao, que ela tenha os mesmos campos do modelo do BD

        if serializer.is_valid():                                                 # verifica se esses dados são validos ( funcao do serializer )
            serializer.save()                                                      # se for valido, vai salvar no BD 
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)                          


# EDITANDO DADOS

    if request.method == 'PUT':                                                     

        nickname = request.data['user_nickname']                                 # indo nos dados do request e pegando o nickname (PK) / Inscrição do usuario por meio da requisição

        try:
            updated_user = User.objects.get(pk=nickname)                            # pega esse dado da nickname e buscamos no BD e coloca na variavel update
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(updated_user, data=request.data)                    # pega os dados da requisição tbm e indicar para o serializer qual o objeto vai ser editado, 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETAR DADOS (DELETE)

    if request.method == 'DELETE':

        try:
            user_to_delete = User.objects.get(pk=request.data['user_nickname'])         # Tentar buscar esse objeto e excluir na funcao delete. funcao bd django
            user_to_delete.delete()                                                                 
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
