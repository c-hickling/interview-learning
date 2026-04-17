# Factory Method

## Description

A creational design pattern that creates objects without specifying the exact classes to create. Instead of directly instantiating classes, a factory method defines an interface for creating objects, allowing subclasses to determine which class to instantiate. This decouples the creation logic from the client code, making it easier to manage, extend, and maintain.

**Key Characteristic**: Encapsulates object creation logic in a dedicated method or class, promoting loose coupling and flexibility.

## When to Use

### Good Use Cases:
1. **Multiple Related Classes** - Different implementations of the same interface (PaymentProcessor: CreditCard, PayPal, Stripe)
2. **Unknown Types at Runtime** - Decide which object to create based on runtime conditions or configuration
3. **Reducing Dependencies** - Client doesn't need to know about concrete classes, only interfaces
4. **Extensibility** - Add new types without modifying existing client code
5. **Complex Initialization** - Encapsulate complicated object creation logic

### When NOT to Use:
- **Simple Single Class** - Overkill for creating only one type of object
- **Overengineering** - Don't add factory if you don't anticipate multiple object types
- **Performance Critical** - Factory indirection adds minimal overhead but may matter in tight loops
- **Clear Client Responsibility** - When clients need explicit control over creation

## Pros and Cons

### Pros:
- ✅ **Loose Coupling** - Client code doesn't depend on concrete classes
- ✅ **Extensibility** - Add new types without modifying existing code (Open/Closed Principle)
- ✅ **Centralized Logic** - All creation logic in one place, easier to maintain
- ✅ **Cleaner APIs** - Hides complex initialization details
- ✅ **Easy Testing** - Can mock factory to inject test objects
- ✅ **Flexibility** - Runtime decisions about which object to create

### Cons:
- ❌ **Complexity** - Introduces additional classes/methods
- ❌ **Indirection** - Developer needs to understand factory instead of direct class usage
- ❌ **Overhead** - Extra method calls add minimal but measurable overhead
- ❌ **Over-abstraction** - May hide details when direct instantiation would be clearer

## Implementation Approaches

### Approach 1: Simple Factory (Static Method)
```python
class ShapeFactory:
    """Simple factory using a static method to create shapes."""
    
    @staticmethod
    def create_shape(shape_type: str):
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        elif shape_type == 'triangle':
            return Triangle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Interface
class Shape:
    def draw(self): pass

# Implementations
class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

class Triangle(Shape):
    def draw(self):
        print("Drawing Triangle")

# Usage
shape = ShapeFactory.create_shape('circle')
shape.draw()  # Output: Drawing Circle
```

**Pros**: Simple, easy to understand, minimal code
**Cons**: Not easily extensible, all logic in one method

### Approach 2: Factory Method Pattern (Inheritance-Based)
```python
from abc import ABC, abstractmethod

# Abstract Factory
class DatabaseFactory(ABC):
    """Abstract factory defining the interface for creating databases."""
    
    @abstractmethod
    def create_connection(self):
        pass

# Concrete Factories
class MySQLFactory(DatabaseFactory):
    def create_connection(self):
        return MySQLConnection("localhost", 3306)

class PostgreSQLFactory(DatabaseFactory):
    def create_connection(self):
        return PostgreSQLConnection("localhost", 5432)

class MongoDBFactory(DatabaseFactory):
    def create_connection(self):
        return MongoDBConnection("localhost", 27017)

# Product Interface
class DatabaseConnection(ABC):
    @abstractmethod
    def connect(self): pass
    
    @abstractmethod
    def query(self, sql: str): pass

# Concrete Products
class MySQLConnection(DatabaseConnection):
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect(self):
        print(f"Connecting to MySQL at {self.host}:{self.port}")
    
    def query(self, sql: str):
        print(f"Executing MySQL query: {sql}")

class PostgreSQLConnection(DatabaseConnection):
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect(self):
        print(f"Connecting to PostgreSQL at {self.host}:{self.port}")
    
    def query(self, sql: str):
        print(f"Executing PostgreSQL query: {sql}")

class MongoDBConnection(DatabaseConnection):
    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def connect(self):
        print(f"Connecting to MongoDB at {self.host}:{self.port}")
    
    def query(self, sql: str):
        print(f"Executing MongoDB query: {sql}")

# Usage
factories = {
    'mysql': MySQLFactory(),
    'postgresql': PostgreSQLFactory(),
    'mongodb': MongoDBFactory()
}

def get_database(db_type: str):
    factory = factories.get(db_type)
    if not factory:
        raise ValueError(f"Unknown database type: {db_type}")
    return factory.create_connection()

# Client code
db = get_database('mysql')
db.connect()
db.query("SELECT * FROM users")
```

**Pros**: Highly extensible, follows Open/Closed Principle, proper use of inheritance
**Cons**: More boilerplate code, more complex

### Approach 3: Factory Class (Parameterized Factory)
```python
class PaymentFactory:
    """Centralized factory for creating payment processors."""
    
    _processors = {}
    
    @classmethod
    def register(cls, payment_type: str, processor_class):
        """Register a new payment processor."""
        cls._processors[payment_type] = processor_class
    
    @classmethod
    def create(cls, payment_type: str):
        """Create a payment processor of the specified type."""
        processor_class = cls._processors.get(payment_type)
        if not processor_class:
            raise ValueError(f"Unknown payment type: {payment_type}")
        return processor_class()

# Product Interface
class PaymentProcessor:
    def process_payment(self, amount: float): pass

# Concrete Products
class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount} via Credit Card")

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount} via PayPal")

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing ${amount} via Stripe")

# Registration (can happen at module load time or config)
PaymentFactory.register('credit_card', CreditCardProcessor)
PaymentFactory.register('paypal', PayPalProcessor)
PaymentFactory.register('stripe', StripeProcessor)

# Usage
processor = PaymentFactory.create('paypal')
processor.process_payment(99.99)  # Output: Processing $99.99 via PayPal
```

**Pros**: Highly extensible, easy registration, dynamic type management
**Cons**: Requires registration step, slightly more setup

### Approach 4: Factory with Configuration
```python
import json
from typing import Type, Dict

class PluginFactory:
    """Factory that loads plugins from configuration."""
    
    def __init__(self, config_file: str):
        with open(config_file, 'r') as f:
            self.config = json.load(f)
        self._cache = {}
    
    def create(self, plugin_name: str):
        """Create a plugin instance from configuration."""
        if plugin_name not in self.config:
            raise ValueError(f"Plugin not configured: {plugin_name}")
        
        if plugin_name in self._cache:
            return self._cache[plugin_name]
        
        plugin_config = self.config[plugin_name]
        plugin_class = self._get_class(plugin_config['class'])
        
        instance = plugin_class(**plugin_config.get('args', {}))
        self._cache[plugin_name] = instance
        return instance
    
    @staticmethod
    def _get_class(class_path: str):
        """Import and return a class from a module path."""
        module_name, class_name = class_path.rsplit('.', 1)
        module = __import__(module_name, fromlist=[class_name])
        return getattr(module, class_name)

# config.json example:
# {
#   "logger": {
#     "class": "loggers.FileLogger",
#     "args": {"filepath": "/var/log/app.log"}
#   },
#   "cache": {
#     "class": "cache.RedisCache",
#     "args": {"host": "localhost", "port": 6379}
#   }
# }

# Usage
factory = PluginFactory('config.json')
logger = factory.create('logger')
cache = factory.create('cache')
```

**Pros**: Configuration-driven, highly flexible, no hardcoding
**Cons**: Requires external config, more complex error handling

## Common Pitfalls

### 1. **Over-Engineering**
Creating a factory for a single class type adds unnecessary complexity.

```python
# Bad: Factory for one type
class SingleTypeFactory:
    @staticmethod
    def create_user():
        return User()

# Better: Just call User() directly
user = User()
```

### 2. **Hidden Complexity in Factory Logic**
Complex conditional logic in factory becomes a maintenance nightmare.

```python
# Bad: Too much logic in factory
def create(type_str):
    if type_str == 'A':
        obj = TypeA()
        # ... 20+ lines of initialization
    elif type_str == 'B':
        # ... more complex logic
    # ... more branches
```

### 3. **Tight Coupling to Concrete Classes**
Factory that imports all concrete classes still couples them.

```python
# Bad: Tight coupling
from payment import CreditCardProcessor, PayPalProcessor, StripeProcessor

def create_processor(type_str):
    if type_str == 'credit_card':
        return CreditCardProcessor()
    # ...

# Better: Use registry pattern or configuration
```

### 4. **Inconsistent Error Handling**
Factory returns None or raises exceptions inconsistently.

```python
# Bad: Inconsistent errors
def create(type_str):
    if type_str == 'known':
        return KnownClass()
    # Sometimes returns None implicitly
    # Sometimes should raise error

# Better: Consistent error handling
def create(type_str):
    if type_str not in self._registry:
        raise ValueError(f"Unknown type: {type_str}")
    return self._registry[type_str]()
```

### 5. **Not Documenting Expected Types**
Unclear what types factory can create.

```python
# Bad: No documentation
def create(db_type):
    # ...

# Better: Clear documentation
def create(self, db_type: str) -> DatabaseConnection:
    """
    Create a database connection.
    
    Args:
        db_type: One of 'mysql', 'postgresql', 'mongodb'
    
    Returns:
        DatabaseConnection instance
    
    Raises:
        ValueError: If db_type is not recognized
    """
```

## Alternatives to Consider

| Alternative | When to Use | Pros | Cons |
|------------|-----------|------|------|
| **Direct Instantiation** | Single class, simple cases | Clear, minimal code | Tight coupling to concrete class |
| **Dependency Injection** | Flexible object creation | Maximum testability | Requires DI framework setup |
| **Builder Pattern** | Complex object construction | Better for many options | More complex than factory |
| **Prototype Pattern** | Clone existing objects | Faster creation | Cloning overhead, complex setup |
| **Abstract Factory** | Families of related objects | Multiple product types | More complex than Factory Method |

## Summary

- Use Factory Pattern when you have **multiple related types** to create
- Choose **Simple Factory** for straightforward cases with few types
- Use **Factory Method Pattern** (inheritance) for true extensibility
- Consider **Registry-based factories** for dynamic plugin systems
- Always provide **clear documentation** of supported types
- Avoid over-engineering with factories for single-type scenarios
- Prefer **Dependency Injection** when possible for better testability
- Keep factory logic **simple and focused** on object creation
