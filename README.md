# github-user-api

Como usar esse app no navegador?
R.: 
   1- Antes de mais nada, colocar seu Github Token na variável access_token dento de:
    ./app/github_token.py
   2- docker-compose up -d 
   3- ou vá até ao diretório app/app.py e executa: hypercorn app:app --reload e abra o localhost:8000/docs

Problema:

 - Obter dados de usuário de alguma conta do Github via sua API com Python e Testes e escrever os resultados obtidos num simples arquivo de texto


Requisitos:

 - Nome do usuário
 - URL para o perfil do usuário
 - Número de repositórios publicos do usuário
 - Número de seguidores do usuário
 - Número de pessoas que o usuário segue 


Parâmetros:

 - :param nome: string
 - :param url: string
 - :param quantidade_repos: int
 - :param quantidade_seguidores: int
 - :param quantidade_usu_segue: int


Plano de ação:
 
 - Determinar o tamanho do projeto e escolher as ferramentas mais adequadas! Lembrar de pesquisar frameworks, bibliotecas e ou plugins que contribuam no desenvolvimento minimizando esforços, tempo e aumentando a qualidade assim como também que resolvam problemas pontuais


Fontes:

 - https://docs.github.com/en/rest?apiVersion=2022-11-28
 - https://fastapi.tiangolo.com/
 - https://github.com/PyGithub/PyGithub
 - https://pygithub.readthedocs.io/en/latest/introduction.html
 - https://www.thepythoncode.com/article/using-github-api-in-python
 - https://github.com/LondonComputadores/backend-restapi-django-advanced-repo
 - https://github.com/LondonComputadores/data-structure-algo-practicings/blob/main/python-all/algomania/linked_list.py
 - https://github.com/LondonComputadores/backend-restapi-django-advanced-repo/blob/master/app/core/tests/test_models.py
 - https://docs.python.org/2/library/unittest.html#assert-methods
 - https://stackoverflow.com/questions/56362354/typeerror-assertequal-missing-1-required-positional-argument-second
 - https://testdriven.io/courses/tdd-fastapi/docker-config/
 - https://www.uvicorn.org/#hypercorn


Solução final:

 - 
