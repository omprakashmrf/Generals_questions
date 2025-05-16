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

Synchronous programing
def task1():
    print("Task 1 started")
    time.sleep(2)
    print("Task 1 finished")

def task2():
    print("Task 2 started")

task1()
task2()

Asynchronous programminfg
import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 finished")

async def task2():
    print("Task 2 started")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())

| Feature           | Synchronous                | Asynchronous                    |
| ----------------- | -------------------------- | ------------------------------- |
| Task Execution    | One at a time              | Concurrent (non-blocking)       |
| Blocking Behavior | Blocks next line           | Doesn't block                   |
| Performance       | Slower for I/O-heavy tasks | Faster for I/O-bound operations |
| Complexity        | Easier to write/debug      | Requires `async/await`, harder  |



| Feature         | **Django**                     | **Flask**                     | **FastAPI**                               |
| --------------- | ------------------------------ | ----------------------------- | ----------------------------------------- |
| Type            | Full-stack framework           | Microframework                | Modern, async web framework               |
| Release Year    | 2005                           | 2010                          | 2018                                      |
| Async Support   | Limited (partial in Django 3+) | No (until Flask 2.0+)         | ✅ Excellent async support                 |
| Performance     | Moderate                       | Fast                          | ⚡ Very Fast (near Node.js)                |
| Learning Curve  | Steeper                        | Beginner-friendly             | Moderate (requires some typing knowledge) |
| Best For        | Large, structured apps         | Small to medium APIs/web apps | Modern APIs, async-heavy apps             |
| Built-in Admin  | ✅ Yes                          | ❌ No                          | ❌ No                                      |
| Data Validation | ❌ Manual or forms              | ❌ Manual                      | ✅ Automatic (via Pydantic)                |
| Routing Style   | Declarative, class-based       | Function-based                | Function + decorator + typing             |



