op Design Patterns for 5-Year Python Developer (JPMorgan Recommended)
1️⃣ Singleton Pattern

Used in: Config loader, DB connections, Logging system.

Python Example (Thread-safe)
class Singleton:
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

2️⃣ Factory Pattern

Used in:
Choosing correct database engine
Creating trade/order objects
Message parsers (JSON, XML, FIX protocol)

Example:
class Shape:
    def draw(self): pass

class Circle(Shape):
    def draw(self): return "Circle"

class Square(Shape):
    def draw(self): return "Square"

def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    if shape_type == "square":
        return Square()

3️⃣ Strategy Pattern

Used in:
Different risk calculation strategies
Trading strategies
Payment/discount logic
Swapping algorithms at runtime

Example:
class Strategy:
    def execute(self, a, b):
        pass

class Add(Strategy):
    def execute(self, a, b): return a + b

class Multiply(Strategy):
    def execute(self, a, b): return a * b

class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute(self, a, b):
        return self.strategy.execute(a, b)

4️⃣ Observer Pattern

Used in:
Event-driven market data feed
Notification systems
GUI event handling
Kafka consumer events

Example:
class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, obs):
        self.observers.append(obs)

    def notify(self, msg):
        for o in self.observers:
            o.update(msg)

class Observer:
    def update(self, msg):
        print("Received:", msg)

5️⃣ Decorator Pattern

Used in:
Logging
Caching
Authorization
Retry logic
Rate-limiting

Python Example:
def log(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def process():
    return "done"

6️⃣ Adapter Pattern
Used when sitting between two incompatible systems:
Different APIs
REST vs. SOAP
Python adapters for C++ libraries
Changing data model for ML model input

Example:
class OldAPI:
    def old_run(self):
        return "Old"

class Adapter:
    def __init__(self, old):
        self.old = old

    def run(self):
        return self.old.old_run()

7️⃣ Facade Pattern
Used in Banking to simplify complex subsystems:
Trade booking system
Risk calculation engine
Multi-service orchestration

Example:
class TradingFacade:
    def place_order(self, order):
        self.validate(order)
        self.route(order)
        self.confirm(order)

8️⃣ Builder Pattern
Used in:
Creating complex objects (Trade, Order, Policy)
Pandas pipeline builder
Config builders

Example:
class TradeBuilder:
    def __init__(self):
        self.trade = {}

    def price(self, val):
        self.trade['price'] = val
        return self

    def qty(self, val):
        self.trade['qty'] = val
        return self

    def build(self):
        return self.trade

9️⃣ Command Pattern
Used in:
Undo operations
Task scheduling
Audit logs

Encapsulating trading actions

Example:
class Command:
    def execute(self): pass

class BuyCommand(Command):
    def execute(self): return "Buy executed"

🔟 Proxy Pattern

Used in:
Access control
Lazy loading
Logging wrapper
Network proxy

Example:
class RealService:
    def request(self): return "data"

class Proxy:
    def __init__(self):
        self.service = RealService()

    def request(self):
        print("Logging from proxy")
        return self.service.request()

🧠 Most Asked by JPMorgan

Among all patterns, these are the most practical for banking domain:

Pattern	Why Important
Singleton	DB connection, configuration
Factory	Creating correct trade/order objects
Strategy	Different algo trading strategies
Observer	Market data feeds, event-driven systems
Decorator	Logging, rate limit, retry
Facade	Wrap complex trading engines
💬 Interview Questions JPMorgan Will Ask
1. Which design patterns have you used in your projects?

Explain:
Decorators
Factory
Singleton
Strategy

2. Difference between Strategy and State pattern?

Strategy = interchangeable behaviors
State = change behavior based on internal state

3. Why Singleton is dangerous?

Hard to test

Hidden dependencies

Global state
