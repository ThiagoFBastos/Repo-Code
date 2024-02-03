# Repo-Code

Repositório local feito com Django para gardar códigos e procurá-los através de keywords e tags.

## Instalação
1. insira no terminal: python3 -m venv env
2. insira no terminal: source ./env/bin/activate ou \env\Scripts\activate no windows
3. insira no terminal: pip install -r requirements.txt
4. insira no terminal: python3 manage.py makemigrations
5. insira no terminal: python3 manage.py migrate

## Ferramentas

- É possível cadastrar um código juntamente com seu título, a sua descrição, que pode conter trechos em latex, e vinculá-lo a algumas categorias existentes.
- É possível filtrar um código baseado no seu título, na sua descrição e na data de cadastramento.
- É possível cadastrar tags juntamente com a sua descrição
- É possível editar o código no editor de texto embutido na página do código.
- É possível alterar o tema do editor para um dos existentes.

## Uso

1. Coloque no terminal o seguinte comando: python3 manage.py runserver
2. Visite no seu terminal a página: localhost:8000/repo
3. É possível adicionar descrições em html combinado com latex, que deve ser usado dentro da tag "\\(<código>\\)"

### Tela inicial
![Tela inicial](https://github.com/ThiagoFBastos/Repo-Code/blob/main/inicio.png)

### Tela inical dark theme
![Tela inicial Dark](https://github.com/ThiagoFBastos/Repo-Code/blob/main/inicio_dark.png)

### Resultados de uma busca
![Busca](https://github.com/ThiagoFBastos/Repo-Code/blob/main/busca.png)

### Todas as tags
![Tags](https://github.com/ThiagoFBastos/Repo-Code/blob/main/all_tags.png)

### Cadastro de tag
![Add tag](https://github.com/ThiagoFBastos/Repo-Code/blob/main/add-tag.png)

### Cadastro de código
![Add code](https://github.com/ThiagoFBastos/Repo-Code/blob/main/add_code.png)

### Problema One bit positions
![One bit positions 1](https://github.com/ThiagoFBastos/Repo-Code/blob/main/one_bit_positions_1.png)
![One bit positions 2](https://github.com/ThiagoFBastos/Repo-Code/blob/main/one_bit_positions_2.png)

### Problema Bitaro Party
![bitaro party 1](https://github.com/ThiagoFBastos/Repo-Code/blob/main/bitaro_party-1.png)
![bitaro party 2](https://github.com/ThiagoFBastos/Repo-Code/blob/main/bitaro_party-2.png)
![bitaro party 3](https://github.com/ThiagoFBastos/Repo-Code/blob/main/bitaro_party-3.png)
![bitaro party 4](https://github.com/ThiagoFBastos/Repo-Code/blob/main/bitaro_party-4.png)

### Problema Namoro dark theme
![namoro 1](https://github.com/ThiagoFBastos/Repo-Code/blob/main/namoro-1.png)
![namoro 2](https://github.com/ThiagoFBastos/Repo-Code/blob/main/namoro-2.png)
![namoro 3](https://github.com/ThiagoFBastos/Repo-Code/blob/main/namoro-3.png)
![namoro 4](https://github.com/ThiagoFBastos/Repo-Code/blob/main/namoro-4.png)

### Preferências
![preferencias](https://github.com/ThiagoFBastos/Repo-Code/blob/main/preferencias.png)

### Preferências dark theme
![preferencias dark](https://github.com/ThiagoFBastos/Repo-Code/blob/main/preferencias_dark.png)
