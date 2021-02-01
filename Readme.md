Este arquivo de texto contém informaçõs sobre a implementação 
do código que resolve os problemas propostos na prova além de informações sobre seu autor.


-------- Autor -------------------------------------------------------
Meu nome é Pedro Dardengo Mesquita, graduado e mestre em física 
pela universidade federal de viçosa. Desisti da ciência pois além 
de estar insatisfeito com o retorno financeiro desta área, gosto
muito de programação. Sempre programei, porém uma programação sempre
científica que lidava com algorítimos complicados, o que contrasta com 
a programação comercial em que os algorítimos são mais simples porém
fazem usos de módulos e plataformas diversas. 

Não tenho nenhuma experiência em empresas, porém meu objetivo é aprender
toda e qualquer tecnologia, linguagem ou plataforma de interesse da empresa.

Tive de aprender a utilizar os módulos presentes neste programa 
a medida que os implementava.
-----------------------------------------------------------------------



------- Código -------------------------------------------------------
Informações gerais:

- Devido as tarefas escolhidas serem de alto nível, me permiti a utilização
de módulos especializados.

- Tentei mostrar de forma geral um conjunto de técnicas em python que conheço.
	Entre eles
	- OOP (encapsulamento, utilização de classes)
	- Programação funcional
	- teste
	- boas práticas e convenções.

- Houveram momentos durante a prova que eu não soube ao certo o que exatamente
estava sendo pedido. Como no item 5, onde apesar da prova se utilizar o verbo
"renomear". A imagem mostra um arquivo sendo salvo, portanto decidi copiar o 
arquivo em questão e salvá-lo com outro nome na mesma pasta, afinal esse caminho
é ligeiramente mais complicado. Tudo, logicamente, é feito utilizando as janelas
de diálogo padrões do Windows. Ao final o programa questiona o usuário se ele deseja
deletar versão original não modificada.

Arquivos:

- Arquivo prova: 
	Arquivo que deve ser compilado para solução da prova.

Diretório services:
- Arquivo file_handler:
	Arquivo auxiliar encapsulado para lidar com métodos relacionados a arquivos.

- Arquivo function_press_enter_to_continue:
	Este arquivo auxiliar implementa a seguinte função no código.
		1. Pergunta se deseja acionar o modo passo a passo.
		a resposta deve ser 'y' (yes) ou 'n' (no).
		2. Caso negativo, o programa segue normalmente.
		3. Caso positivo, o programa é pausado em pontos específicos e
		deve-se pressionar enter para que ele prossiga.
		
	Apesar de inútil, já que existem debuggers. Foi uma forma
	de demonstrar um pouco de programação OOP para solucionar problemas em 
	um contexto onde objetos não são necessários. Utilizando os atributos do
	objeto para passar valores a variáveis apenas uma vez, mesmo que os métodos
	da classe sejam chamados várias vezes.

Diretório unittests:
- Arquivo test_user_input_handler:
	Utiliza o módulo unittest para implementar um simples teste.

	


 