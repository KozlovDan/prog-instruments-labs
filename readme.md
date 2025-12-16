# Order Processing System

Для выполнения лабораторной работы был использован собственный ранее написанный код (`code_before.py`).  
Был выполнен рефакторинг, направленный на:

- улучшение архитектуры
- повышение читаемости и удобства сопровождения
- устранение дублирования
- выделение отдельных слоёв системы
- повышение расширяемости кода

Результатом рефакторинга — файл `code_after.py`, в котором код был полностью структурирован по уровням ответственности в соответствии с принципами SOLID и рекомендациями PEP-8.

---

# Изменения после рефакторинга

### 1. Разделение на слои (архитектурная декомпозиция)

Теперь код разделён на уровни:

- **Сервисный слой (business logic)**: `OrderProcessor`
- **Модуль расчёта стоимости (pricing)**: `PricingService`
- **Сервис скидок (discounts)**: `DiscountService`
- **Сервис доставки (shipping)**: `ShippingService`
- **Сервис налогообложения (tax)**: `TaxService`
- **Исключения**: `InvalidOrderError`

Приводит к большей модульности, тестируемости и удобству расширения.

---

### 2. Принцип единственной ответственности 

Одна из проблем в изначальном коде заключалась в огромной функции `process_order`, содержащей:

- расчёт стоимости
- применение скидок
- вычисление доставки и налогов
- проверку корректности данных

До:

```python
def process_order(self, order):
    total_price = 0
    discount = 0
    shipping_cost = 0
    tax = 0
```
Теперь каждый класс выполняет только одну задачу:
```python
total = self.pricing.calculate_total(order["items"])
discount = self.discount.calculate(total, order["customer_type"])
shipping = self.shipping.calculate(order["delivery"])
tax = self.tax.calculate(total, order["country"])
```
---
### 3. Устранение дублирования кода
Ранее вычисление стоимости и налога по типу клиента и стране повторялось многократно:

До:
```python
if order["customer_type"] == "vip":
    discount = total_price * 0.1
elif order["customer_type"] == "employee":
    discount = total_price * 0.2
```
После:
```python
self.discount.calculate(total, order["customer_type"])
```
---
### 4. Инверсия зависимостей
Бизнес-логика больше не зависит от конкретных числовых значений или словарей.
Сервисы получают абстракции:
```python
processor = OrderProcessor(
    pricing=PricingService(),
    discount=DiscountService(),
    shipping=ShippingService(),
    tax=TaxService()
)
```
---
### 5. Добавлены доменные сервисы
Ранее расчёты выполнялись прямо в OrderProcessor, теперь выделены отдельные сервисы с логикой

- `PricingService` - вычисление суммы заказа
- `DiscountService` - скидки по типу клиента
- `ShippingService` - доставка
- `TaxService` - налоги

До:
```python
total_price += item["price"] * item["quantity"]
```

После:

```python
total = self.pricing.calculate_total(order["items"])
```
---
### 6. Улучшена читабельность, добавлены комментарии и docstrings

Код стал понятнее, каждый метод имеет чёткое назначение, а переменные имеют осмысленные имена.

---
### 7. Улучшена расширяемость

Теперь можно:
- Добавить новые типы скидок
- Изменить механизм расчёта доставки или налога
- Подключить веб-интерфейс вместо CLI
- Писать unit-тесты для отдельных сервисов
---
### 8. Использованы Python-инструменты для упрощения логики

Сложные условные блоки и циклы заменены на генераторы и словари:
```python
return total * self.DISCOUNTS.get(customer_type, 0)
```
```python
return self.SHIPPING_COSTS.get(delivery_type, 10)
```
---
### 9. Вынесены исключения в отдельный класс

Ранее возвращались строки "error". Теперь используются исключения:
```python
if not order or "items" not in order:
    raise InvalidOrderError("Invalid order structure")
```
---
### 10. Отдельные unit-тесты для каждого слоя

Ранее тестировалась только вся функция целиком.
Теперь есть тесты для:

- расчёта стоимости (`PricingService`)
- расчёта скидок (`DiscountService`)
- доставки (`ShippingService`)
- налогов (`TaxService`)
- обработки некорректных заказов (`OrderProcessor` + `InvalidOrderError`)