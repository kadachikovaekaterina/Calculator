# Калькулятор для работы с рациональными и комплексными числами

*Назначение программы*

Программа предназначена для осуществления простых арифметических операций (сложение, вычитание, умножение деление) с числами, включая коплексные и рациональные числа.

## Модули программы:
### **UI (User Interface)**
UI реализован в модуле view. Обеспечивает ввод чисел с клавиатуры, присвоение необходимого типа введённым числам, а также вывод результата.

**Модули, обспечивающие инициацию переменных, а также совершение простых арифметических операций:**

* model_div: деление
* model_mult: умножение
* model_subt: вычитание
* model_sum: сложение.
### **Guid**
Модуль guid содержит словари, которые используются в модуле controller:
- dict_ar: используется для вызова соответствующего метода, отвечающего за инициацию переменных и осуществление арифметических операций. Ключом в словаре является оператор, вводимый с клавиатуры, элементом - метод;
- dict_log: используется для внесения записи "Вид операции" при логировании действий. Ключом в словаре является оператор, вводимый с клавиатуры, элементом - наименование операции.

### **Logger**
Модуль, осущестялющий логирование операций и запись истории операций в текстовый файл log.txt. Запись осуществлется в следующем формате:
<Дата и время совершения операции>, операция: <наименование операции>; рзультат: <итоговое значение>.
Файл log.txt предназначен для хранения записей об истории операций.

### **Controller**
Центральный модуль программы, отвечающий вызов и выполнение всех необходимых модулей программы.

### **Main**
Модуль, запускающий выполнение программы.