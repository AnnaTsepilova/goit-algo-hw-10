# Імпорт необхідної бібліотеки
import pulp

# Створення об'єкту задачі для максимізації
model = pulp.LpProblem(name="production-optimization", sense=pulp.LpMaximize)

# Оголошення змінних (кількість одиниць Лимонаду і Фруктового соку)
lemonade = pulp.LpVariable(name="lemonade", lowBound=0, cat="Integer")
fruit_juice = pulp.LpVariable(name="fruit_juice", lowBound=0, cat="Integer")

# Мета: Максимізувати загальну кількість вироблених одиниць напоїв
model += lemonade + fruit_juice, "Total_Products"

# Обмеження на ресурси
model += (2 * lemonade + 1 * fruit_juice <= 100), "Water_Constraint"
model += (1 * lemonade <= 50), "Sugar_Constraint"
model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

# Розв'язування задачі
model.solve()

# Виведення результатів
print(f"Максимальна кількість лимонаду: {lemonade.varValue}")
print(f"Максимальна кількість фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість напоїв: {lemonade.varValue + fruit_juice.varValue}")
print(f"Статус: {pulp.LpStatus[model.status]}")
