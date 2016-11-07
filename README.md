# Curso Desenvolvimento WEB
Códigos do curso de desenvolvedor web da MadCode

Abaixo você confere registro de todas as aulas, com os pontos mais importantes e links interessantes que foram mostrados em aula ou que complementam o que aprendemos.

---------------------------------------

## Aula 1

### WEB X Internet

Como discutimos em aula, vamos reforçar sempre lembrando: INTERNET = Plataforma ou insfraestrutura / WEB = Cultura

### História da internet

https://pt.wikipedia.org/wiki/Hist%C3%B3ria_da_Internet
www.evolutionoftheweb.com/?hl=pt-br

### Relação cliente servidor

De forma muito simples, servidores são os computadores da rede que fornecem recursos e clientes são os computadores da rede que acessam recursos.

![](https://upload.wikimedia.org/wikipedia/commons/1/1c/Cliente-Servidor.png)

---------------------------------------

## Aula 2

...

---------------------------------------

## Aula 3

### Box-model

Todos os elementos HTML são desenhados pelo navegador como um "quadrado". Para desenhar esse quadrado (box) temos algumas propriedades:

* altura (height)
* largura (width)
* margem externa (margin)
* margem interna (padding)
* borda (border)

Uma explicação mais detalhada pode ser vista [aqui](https://developer.mozilla.org/pt-BR/docs/Web/CSS/box_model)

### Idioma e caracteres

Para que o navegador renderize o documento de forma correta, precisamos indicar sempre que o documento é um HTML, seu idioma e em qual _enconding_ foi escrito o documento. Assim, sempres comece seus documentos HTML da seguinte forma:

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
	<meta charset="UTF-8">
```

### Inspecionador de código

Os navegadores modernos nos auxiliam no desenvolvimento com inspecionadores de código. Basta clicar com o botão direito do mouse em qualquer lugar da página (ou no lugar específico que você deseja inspecionar) e escolher no menu a opção **Inspecionar** (_Inspect Element_).

![](https://developer.chrome.com/devtools/images/elements-panel.png)

Com essa ferramenta, você pode tanto editar o código HTML quanto o CSS da página dinamicamente, visualizando cada alteração e desenhando a página como você gostaria. Um uso mais avançado é a correção de bugs, não só do HTML e do CSS, mas principalmente do JavaScript

### Atividade

Agora que já entendemos bem o HTML, vamos pegar modelos de HTML mais complexos e brincar com eles.
Busque na internet modelos HTML gratuitos (_free html templates_), ou acesse o site http://html5up.net.
Edite o template HTML escolhido pensando em montar seu currículo, portifólio ou qualquer página que conte um pouco sobre você, o que sabe fazer, etc...

---------------------------------------

### Aula 4

####DIV e SPAN

São elementos genéricos que servem como marcadores do código HTML para manipular pedaços do documento HTML no CSS ou no JavaScript.

#### Box-model - display

O atributo display configura como um elemento HTML é exibido pelo navegador segundo seu box-model. Vimos 3 valores possíveis para o atributo display:

* block
* inline
* inline-block

Existem outros atríbutos para o display que vamos ver em outras aulas.

#### atributos ID e CLASS do HTML

Os atributos ID e CLASS do HTML são fundamentais para manipular os elementos HTML. ID deve receber um valor único, algo que identifique exatamente aquele elemento. CLASS não precisa ser único, pois vários elementos podem pertencer a mesma classe. Fizemos uma analogia com seres vivos que está abaixo. _*ATENÇÃO!* O código abaixo é apenas uma metáfora, não é um código HTML funcional!_

```html
<humano id="João" class="menino adolescente nerd">
```

#### Construindo as regras em CSS

A principal forma de anexar um documento CSS a um documento HTML é usando a tag ```<link rel="stylesheet" type="text/css" href="estilo.css">``` dentro da tag ```<head>```.

Nesse documento escrevemos uma regra da seguinte forma:

seletor {
	atributo: valor;
}

Veja um exemplo abaixo:

```css
#menu a {
	padding: 0 20px;
	height: 50px;
	line-height: 50px;
	background-color: black;
	color: white;
	text-align: center;
	display: inline-block;
	text-decoration: none;
	margin: 0;
}
```

Para construir o seletor, podemos usar a tag html, o id, a classe além de pseudo-classes. A tag é escrita somente com o nome da tag, o id usa o 'hashtag' #, e a classe usa um ponto final.. No exemplo acima, estamos selecionando todos os elementos da tag 'a' que são filhos do elemento de id 'menu'.

Mais sobre como escrever o seletor CSS, veja [aqui](https://developer.mozilla.org/pt-BR/docs/Web/CSS/Getting_Started/Seletores).