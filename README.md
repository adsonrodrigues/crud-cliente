# Cliente CRUD
___
[![build](https://img.shields.io/badge/build-passing-green)](build) [![docker](https://img.shields.io/badge/docker%20build-automated-important)](docker) [![docker-version](https://img.shields.io/badge/version-19.03.8-important)](docker-version) [![license](https://img.shields.io/badge/license-MIT-blue)](license)

## Tabela de Conteúdo
___
* [Tabela de Conteudo](#tabela-de-conteudo)
* [Sobre o Projeto](#sobre-o-projeto)
  * [Feito Com](#feito-com)
* [Começando](#comecando)
  * [Pré-requisitos](#pre-requisitos)
  * [Instalação](#instalacao)
  * [Rode o Projeto](#rode-o-projeto)
* [API](#api)
* [Contribuição](#contribuicao)
* [Licença](#licenca)
* [Contato](#contato)

## Sobre o Projeto
___
_API Django REST simples que fornece crud do cliente com um login básico._

## Feito Com
___
- [Django](https://www.djangoproject.com/) - Django é uma estrutura da Web Python de alto nível que incentiva o desenvolvimento rápido e um design limpo e pragmático.
- [Django Rest Framework](https://www.django-rest-framework.org/) - A estrutura Django REST é um kit de ferramentas poderoso e flexível para construir APIs da Web.
- [Django Environ](https://github.com/joke2k/django-environ) - Django Environ permite que você use a metodologia de doze fatores para configurar sua aplicação Django com variáveis de ambiente.
- [Docker](https://www.docker.com/) - O Docker simplifica e acelera seu fluxo de trabalho, enquanto dá aos desenvolvedores a liberdade de inovar com sua escolha de ferramentas, pilhas de aplicativos e ambientes de implantação para cada projeto.
- [Docker Compose](https://docs.docker.com/compose/) - Compose é uma ferramenta para definir e executar aplicativos Docker de vários contêineres.

## Começando
___
_Para poder usar o projeto siga os passos abaixo._

### Pré-requisitos
___
###### docker

- [Documentação Oficial](https://docs.docker.com/get-docker/)
- [Como instalar no Fedora](https://docs.docker.com/engine/install/fedora/)
- [Como instalar no MacOS](https://docs.docker.com/docker-for-mac/install/)
- [Como instalar no Windows](https://docs.docker.com/docker-for-windows/install/)

###### docker compose

- [Como instalar docker compose](https://docs.docker.com/compose/install/)

### Instalação
___
```sh
$ docker-compose up -d --build # (only first)
$ docker-compose exec service python3 manage.py migrate # (only first)
$ docker-compose exec service python3 manage.py createsuperuser # (only first)
```

### Crie o .env do projeto
___
```sh
$ cd crud_cliente
$ touch .env
```

### Adicione as informações .env
___
```.env
SECRET_KEY='z6mew@b6g^)kx@z9565v88y^0p!4#cqlaemye++*1+bfk)=(v@'
DATABASE_URL='postgres://postgres:root1234@postgres:5432/crud'
DEBUG=True
```


_Caso não seja criado o .env do projeto o projeto irá rodar numa aplicação com variáveis default e com o banco SQlite._


### Rode o projeto
___
```sh
$ docker-compose up -d
$ docker-compose exec service python3 manage.py runserver 0.0.0.0:8000
```

## API
___
Está API contém seguintes endpoints:

#### Login
```
POST /auth/login/
```

#### Logout
```
POST /auth/logout/
```
#### Listar Clientes
```
GET /api/cliente/
```
#### Detalhe do Cliente
```
GET /api/cliente/<id>
```
#### Atualizar Cliente
```
PUT /api/cliente/<id>
```
#### Cadastrar novo Cliente
```
POST /api/cliente/
```


## Licença
___
The MIT License (MIT)

Copyright (c) [2020] [Adson Rodrigues](https://github.com/adsonrodrigues)

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Contato
___

Adson Rodrigues - [Linkedin](https://www.linkedin.com/in/adsonr/)