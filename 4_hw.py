class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)
rect3 = Rectangle(8, 4)

print(f"Площадь rect1: {rect1.area()}, Периметр rect1: {rect1.perimeter()}")
print(f"Площадь rect2: {rect2.area()}, Периметр rect2: {rect2.perimeter()}")
print(f"Площадь rect3: {rect3.area()}, Периметр rect3: {rect3.perimeter()}")

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b

math = Math(10, 5)
print(f"Сложение: {math.addition()}")
print(f"Умножение: {math.multiplication()}")
print(f"Деление: {math.division()}")
print(f"Вычитание: {math.subtraction()}")

class Button:
    def __init__(self, text, button_type="Кнопка", locator=""):
        self.text = text
        self.type = button_type
        self.locator = locator

    def click(self):
        return f"Клик по кнопке {self.text}"

text_box_button = Button("Text Box")
check_box_button = Button("Check Box")
radio_button_button = Button("Radio Button")
web_tables_button = Button("Web Tables")
buttons_button = Button("Buttons")
links_button = Button("Links")

buttons = [text_box_button, check_box_button, radio_button_button, web_tables_button, buttons_button, links_button]
for button in buttons:
    print(button.text)

for button in buttons:
    print(button.click())
