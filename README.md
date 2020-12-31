# mscScriptTool
## On English
 Dual languaged (rus+eng) tool for disassembling and assembling scripts .msc sfrom the visual novel's engine Stuff Script Engine (also known as Propeller Engine). With it thou can fully edit code, not just strings, as with some earlier tools. Thou can add line or even message breaks without restrictions!
 
 It has some useful features.
 Firstly, during assembling all message numbers recounts.
 Secondly, thou can make comments in txt file with "$" at the beginning of the string.
 Thirdly, some definations: "#0-" are "free bytes", "#1-" are commands (and "\[...]" are arguments below) and "#2-"/"#3-" are labels.
 
 ### Tested on
- [Bullet Butlers](https://vndb.org/v445)
 
## На русском
 Двуязычное (рус+англ) средство для разборки и сборки скриптов .msc движка визуальных новелл Stuff Script, известного также как Propeller Engine. С ним вы можете полностью редактирвоать код, а не только строки, как с ранее существовшими средствами. Вы можете добавлять разрывы текста по строкам и даже сообщениям без ограничений!
 
 В нём есть несколько полезных особенностей.
 Во-первых, во время сборки все номера сообщений пересчитываются.
 Во-вторых, можно делать комментарии, при этом в начало строки необходимо ставить "$".
 В-третьих, опишем некоторые определения: "#0-" есть "вольные байты", "#1-" есть команды (и под ними "\[...]" аргументы) и "#2-"/"#3-" есть метки.
 
 ### Протестировано на
 - [Пули да дворецкие](https://vndb.org/v445)
 
 # Usage / Использование
## On English
1. Enter a title of the .msc file in the top entry (do see, with extension). Thou can also enter relative or absolute path.
1.1. Just as so and after pushing the "(De)crypt" bytton thou can use (de)cryption panel to decrypt or encrypt script as needed.
2. Enter a title of the .txt file (do see, with extension). Thou can also enter relative or absolute path.
2.1. After that thou can optionaly to push the button "Analyze script" to get to know it's version or if it's encrypted.
3. For dissassemble push the button "Disassemble script".
4. For assemble push the button "Assemble script".
5. Status will be displayed on the text area below.

## На русском
1. Введите название файла .mes в верхней форме (заметьте, с расширением). Также можно вводить относительный или абсолютный до него путь.
1.1. Совершенно так же, а также после нажатия на кнопку "(Де)шифровать" на панели (де)шифровки вы можете расшифровать или зашифровать скрипт, коли вам то требуется.
2. Введите название файла .txt в нижней форме (заметьте, с расширением). Также можно вводить относительный или абсолютный до него путь.
2.1. Также опционально вы можете нажать на кнопку "Анализировать скрипт", дабы узнать его версию и зашифрован ли он.
3. Для разборки нажмите на кнопку "Разобрать скрипт".
4. Для сборки нажмите на кнопку "Собрать скрипт".
5. Статус сих операций будет отображаться на текстовом поле ниже.

# Line and Message Breaks Help / Помощь по организации переносов по строкам и сообщениям.
## On English
Sometimes there could be a very big problem: text may not fully get in textbox. But with this tool thou don't need to cut some part of text, no. Thou can use line and message breaks. Methods are below.
### For line breaks insert in the current message this tag (works correctly only before the autolinebreak).
```
_r
```
### For message breaks insert this below the current message ('SomeString' -> text on the new message).
```
#1-MESSAGE
[0, 0, 'SomeString_r']
```

## На русском
Иногда можно столкнуться с одной большой-пребольшой проблемой: текст может не полностью влезать в текстовое окно. Однако, с сим средством вам не нужно обрезать его, отнюдь. Вы можете организовывать переносы по строкам и сообщениям. Методы указаны ниже.
### Для переносов по строкам добавьте в текущее сообщение следующий тэг (работает корректно до выполнения автопереноса по символам).
```
_r
```
### Для переносов по сообщениям добавьте под текущее сообщение следующий код (вместо "Какая_то_строка" вставьте ваше сообщение).
```
#1-MESSAGE
[0, 0, 'Какая_то_строка_r']
```
