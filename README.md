O projeto utiliza Django e Django REST Framework, para consumir a api pública do Github.
Como funciona? Foram criadas duas classes dentro da views de github_core, lá está o código que executa as requisições para exibição dos dados de usuários e repositórios;
Se caso queira dar um get em algum ausário, é preciso fazer assim:
url: apigithubprojeto.herokuapp.com/users/?search=nomeusuario
O nome que vai ser pesquisado deve ser igual o que está salvo no github.
