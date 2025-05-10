When to Use:
Use a static method when:

You don’t need access to self (instance) or cls (class).
The method logically belongs to the class (utility/helper functions).

| Feature         | Instance Method     | Class Method     | Static Method        |
| --------------- | ------------------- | ---------------- | -------------------- |
| Accesses `self` | ✅                   | ❌                | ❌                    |
| Accesses `cls`  | ❌                   | ✅                | ❌                    |
| Decorator       | none                | `@classmethod`   | `@staticmethod`      |
| Use case        | Operate on instance | Operate on class | Utility/helper logic |



instace method
Key Features
Accessed using the object: obj.method()
Can read and update instance variables (like self.name)
Defined without any decorator

| Feature            | Instance Method | Class Method   | Static Method   |
| ------------------ | --------------- | -------------- | --------------- |
| Access `self`      | ✅               | ❌              | ❌               |
| Access `cls`       | ❌               | ✅              | ❌               |
| Modify object data | ✅               | ❌              | ❌               |
| Decorator          | *none*          | `@classmethod` | `@staticmethod` |





classmethod
Key Features
First argument is cls, which refers to the class.
Declared with the @classmethod decorator.
Can access/modify class variables, but not instance variables.
Called on the class itself or its instances.




Feature	Instance Method	Class Method	Static Method
Accesses self	✅	❌	❌
Accesses cls	❌	✅	❌
Decorator	None	@classmethod	@staticmethod
Use for class state	❌	✅	❌


--------------------------------
**********GENERATOR *********

--------------------------------

generator Advanteage
Lazy evaluation (generate values on demand).
Saves memory (especially with large datasets).
Cleaner code than manually writing iterator classes.

squares = (x * x for x in range(10))
print(next(squares))  # 0
print(next(squares))  # 1

