# Observer Pattern (Subject-Observer)

## Description

A behavioral design pattern that defines a one-to-many dependency between objects so that when one object (the subject) changes state, all its dependents (observers) are notified automatically. The Observer pattern is also known as Pub-Sub (Publish-Subscribe) pattern. It enables loose coupling between components: the subject doesn't need to know the details of the observers, and observers can be added or removed dynamically.

**Key Characteristic**: Establishes a subscription mechanism where subjects notify multiple observers about state changes without tight coupling.

## When to Use

### Good Use Cases:
1. **Event Systems** - GUI frameworks notifying listeners of user interactions
2. **Model-View Architecture** - View updates when Model changes (MVC, MVVM)
3. **Real-Time Updates** - Stock prices, weather data, live notifications
4. **Publish-Subscribe Systems** - Message queues, event buses
5. **Change Notifications** - Database changes triggering multiple handlers
6. **UI Reactivity** - React's state management, Vue's reactive data
7. **Logging and Monitoring** - Multiple observers for log events
8. **Event Buses** - Decoupled communication between components

### When NOT to Use:
- **Tight Coupling is Acceptable** - Simple systems with few dependencies
- **Performance Critical** - Event propagation adds overhead
- **Few Notifications** - Direct method calls are simpler
- **Simple One-Way Communication** - When callbacks suffice
- **Synchronous Requirements** - Observer pattern inherently asynchronous

## Pros and Cons

### Pros:
- ✅ **Loose Coupling** - Subject and observers don't need to know each other
- ✅ **Dynamic Relationships** - Add/remove observers at runtime
- ✅ **Single Responsibility** - Subject focuses on state, observers on reactions
- ✅ **Scalability** - Easy to add many observers without modifying subject
- ✅ **Reusability** - Same observer can monitor multiple subjects
- ✅ **Separation of Concerns** - Logic separated from notification handling
- ✅ **Open/Closed Principle** - Open for extension, closed for modification

### Cons:
- ❌ **Memory Leaks** - Observers must be unregistered to avoid memory issues
- ❌ **Performance Overhead** - Notifying many observers can be slow
- ❌ **Order Dependency** - Observer notification order might matter
- ❌ **Debugging Difficulty** - Hard to trace when observers react
- ❌ **Unintended Updates** - All observers notified even if unrelated data changes
- ❌ **Hidden Dependencies** - Observers depend on subject implicitly

## Implementation Approaches

### Approach 1: Basic Observer Pattern (OOP)
```python
from abc import ABC, abstractmethod
from typing import List

# Subject Interface
class Subject(ABC):
    @abstractmethod
    def attach(self, observer: 'Observer'):
        pass
    
    @abstractmethod
    def detach(self, observer: 'Observer'):
        pass
    
    @abstractmethod
    def notify(self):
        pass

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject):
        pass

# Concrete Subject
class StockPrice(Subject):
    def __init__(self, ticker: str, price: float):
        self._ticker = ticker
        self._price = price
        self._observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        if observer not in self._observers:
            self._observers.append(observer)
            print(f"Observer attached to {self._ticker}")
    
    def detach(self, observer: Observer):
        if observer in self._observers:
            self._observers.remove(observer)
            print(f"Observer detached from {self._ticker}")
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
    
    @property
    def price(self) -> float:
        return self._price
    
    @property
    def ticker(self) -> str:
        return self._ticker
    
    @price.setter
    def price(self, new_price: float):
        print(f"\n{self._ticker} price changed from ${self._price} to ${new_price}")
        self._price = new_price
        self.notify()

# Concrete Observers
class Trader(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, subject: StockPrice):
        print(f"Trader {self.name}: Stock {subject.ticker} is now ${subject.price}")
        if subject.price < 50:
            print(f"  → {self.name}: BUY!")
        elif subject.price > 100:
            print(f"  → {self.name}: SELL!")

class StockDisplay(Observer):
    def __init__(self, name: str):
        self.name = name
    
    def update(self, subject: StockPrice):
        print(f"Display {self.name}: {subject.ticker} = ${subject.price}")

class Logger(Observer):
    def update(self, subject: StockPrice):
        print(f"[LOG] Stock update: {subject.ticker} = ${subject.price}")

# Usage
stock = StockPrice("AAPL", 150.00)

trader1 = Trader("Alice")
trader2 = Trader("Bob")
display = StockDisplay("MonitorA")
logger = Logger()

stock.attach(trader1)
stock.attach(trader2)
stock.attach(display)
stock.attach(logger)

# Notify all observers when price changes
stock.price = 145.50
stock.price = 48.00
stock.price = 105.00

stock.detach(trader2)
stock.price = 100.00
```

**Pros**: Clear structure, explicit interfaces, full control
**Cons**: More boilerplate, manual observer management

### Approach 2: Event-Based Observer (Python)
```python
from typing import Callable, List, Dict

# Event-based subject using callbacks
class EventEmitter:
    """Simple event-based subject using callbacks."""
    
    def __init__(self):
        self._listeners: Dict[str, List[Callable]] = {}
    
    def on(self, event: str, callback: Callable):
        """Register a listener for an event."""
        if event not in self._listeners:
            self._listeners[event] = []
        self._listeners[event].append(callback)
    
    def off(self, event: str, callback: Callable):
        """Unregister a listener from an event."""
        if event in self._listeners and callback in self._listeners[event]:
            self._listeners[event].remove(callback)
    
    def emit(self, event: str, data=None):
        """Trigger all listeners for an event."""
        if event in self._listeners:
            for callback in self._listeners[event]:
                callback(data)

# Subject
class UserAccount(EventEmitter):
    def __init__(self, username: str):
        super().__init__()
        self.username = username
        self._balance = 0.0
    
    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, amount: float):
        old_balance = self._balance
        self._balance = amount
        self.emit('balance_changed', {
            'username': self.username,
            'old_balance': old_balance,
            'new_balance': self._balance
        })

# Observers (callbacks)
def on_low_balance(data):
    if data['new_balance'] < 100:
        print(f"⚠️  WARNING: {data['username']} balance is low: ${data['new_balance']}")

def on_transaction(data):
    print(f"📊 Transaction: {data['username']} - ${data['old_balance']} → ${data['new_balance']}")

def on_deposit(data):
    if data['new_balance'] > data['old_balance']:
        print(f"💰 Deposit: {data['username']} received ${data['new_balance'] - data['old_balance']}")

# Usage
account = UserAccount("john_doe")

account.on('balance_changed', on_transaction)
account.on('balance_changed', on_low_balance)
account.on('balance_changed', on_deposit)

account.balance = 500
account.balance = 75
account.balance = 200

account.off('balance_changed', on_low_balance)
account.balance = 50
```

**Pros**: Simple, Pythonic, flexible callbacks
**Cons**: Less structured, harder to track listeners, no type safety

### Approach 3: Decorator-Based Observer
```python
from typing import Callable, List
from functools import wraps

class Subject:
    """Subject with decorator-based observer registration."""
    
    def __init__(self):
        self._observers: List[Callable] = []
        self._state = None
    
    def subscribe(self, func: Callable):
        """Decorator to subscribe to state changes."""
        self._observers.append(func)
        return func
    
    def unsubscribe(self, func: Callable):
        """Unsubscribe from state changes."""
        if func in self._observers:
            self._observers.remove(func)
    
    def notify(self, state):
        """Notify all observers of state change."""
        for observer in self._observers:
            observer(state)
    
    @property
    def state(self):
        return self._state
    
    @state.setter
    def state(self, value):
        self._state = value
        self.notify(value)

# Subject instance
data = Subject()

# Register observers using decorator syntax
@data.subscribe
def observer1(state):
    print(f"Observer1: State is {state}")

@data.subscribe
def observer2(state):
    print(f"Observer2: State is {state}, doubled = {state * 2}")

@data.subscribe
def observer3(state):
    print(f"Observer3: State is {state}, squared = {state ** 2}")

# Trigger notifications
data.state = 5
data.state = 10

# Unsubscribe
data.unsubscribe(observer2)
data.state = 15
```

**Pros**: Elegant decorator syntax, Pythonic, easy registration
**Cons**: Less explicit control, decorator must be used at definition time

### Approach 4: Observable Property (Property-Based)
```python
from typing import Callable, List, Any

class ObservableProperty:
    """Property that notifies observers on change."""
    
    def __init__(self, name: str, initial_value: Any = None):
        self.name = name
        self.value = initial_value
        self._observers: List[Callable] = []
    
    def subscribe(self, observer: Callable):
        """Subscribe to value changes."""
        self._observers.append(observer)
    
    def unsubscribe(self, observer: Callable):
        """Unsubscribe from value changes."""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def set_value(self, new_value: Any):
        """Set value and notify observers."""
        if self.value != new_value:
            old_value = self.value
            self.value = new_value
            self._notify(old_value, new_value)
    
    def _notify(self, old_value: Any, new_value: Any):
        """Notify all observers."""
        for observer in self._observers:
            observer(self.name, old_value, new_value)

# Model with observable properties
class Model:
    def __init__(self):
        self.name = ObservableProperty('name', 'Unknown')
        self.age = ObservableProperty('age', 0)
        self.email = ObservableProperty('email', '')

# Observers
def on_property_change(property_name: str, old_value: Any, new_value: Any):
    print(f"Property '{property_name}' changed: {old_value} → {new_value}")

def validate_age(property_name: str, old_value: Any, new_value: Any):
    if property_name == 'age':
        if not (0 <= new_value <= 150):
            print(f"⚠️  Invalid age: {new_value}")

# Usage
model = Model()

model.name.subscribe(on_property_change)
model.age.subscribe(on_property_change)
model.age.subscribe(validate_age)
model.email.subscribe(on_property_change)

model.name.set_value('Alice')
model.age.set_value(30)
model.age.set_value(200)
model.email.set_value('alice@example.com')
```

**Pros**: Fine-grained observation, per-property control
**Cons**: More verbose, multiple property instances

## Common Pitfalls

### 1. **Memory Leaks from Dangling Observers**
Forgetting to unsubscribe causes memory leaks and phantom notifications.

```python
# Bad: Observer never unregistered
class View:
    def __init__(self, model):
        model.attach(self)  # Attached but never detached
        # When View is deleted, it still receives notifications

# Better: Explicitly unregister
class View:
    def __init__(self, model):
        self.model = model
        model.attach(self)
    
    def __del__(self):
        self.model.detach(self)  # Cleanup
```

### 2. **Observer Notification Order Dependency**
Code depends on observers being called in specific order, causing bugs.

```python
# Bad: Depends on order
subject.attach(validator)      # Must be first
subject.attach(processor)      # Must be second
subject.attach(logger)         # Must be third

# Better: Make observers independent
# Each observer shouldn't depend on others being called before it
```

### 3. **Circular Dependencies Between Subject and Observer**
Subject and observer depend on each other, creating tight coupling.

```python
# Bad: Circular dependency
class Subject:
    def __init__(self, observer):
        self.observer = observer

class Observer:
    def __init__(self, subject):
        self.subject = subject

# Better: Loose coupling
subject = Subject()
observer = Observer()
subject.attach(observer)  # Register after creation
```

### 4. **Notifying Observers During State Modifications**
Observers modifying state or other observers during notification causes issues.

```python
# Bad: Modifying during notification
def notify(self):
    for observer in self._observers:
        observer.update(self)
        # Observer might add/remove other observers!

# Better: Copy observer list before notification
def notify(self):
    observers_copy = list(self._observers)
    for observer in observers_copy:
        observer.update(self)
```

### 5. **Unnecessary Notifications**
Notifying observers when data hasn't actually changed.

```python
# Bad: Always notifies
@property
def value(self):
    return self._value

@value.setter
def value(self, new_value):
    self._value = new_value
    self.notify()  # Notifies even if value unchanged

# Better: Notify only on actual change
@value.setter
def value(self, new_value):
    if self._value != new_value:
        self._value = new_value
        self.notify()
```

## Alternatives to Consider

| Alternative | When to Use | Pros | Cons |
|------------|-----------|------|------|
| **Direct Callbacks** | Simple one-off notifications | Minimal overhead | Tight coupling |
| **Event Bus** | Application-wide events | Decoupled communication | Can be overused |
| **Signals (Django)** | Web framework events | Framework integration | Framework dependency |
| **Reactive Programming** | Complex data flows | Powerful composition | Steep learning curve |
| **Message Queue** | Asynchronous updates | Decoupled, distributed | More infrastructure |
| **Polling** | Periodic checking | Simple to understand | Inefficient |

## Real-World Examples

### 1. **GUI Frameworks**
Button clicks notify multiple listeners (event handlers).

### 2. **Stock Market**
Price changes notify traders, displays, alerts, and databases.

### 3. **Game Development**
Health changes trigger UI updates, sound effects, and animation.

### 4. **Web Frameworks** (MVC/MVVM)
Model changes notify Views to update display.

### 5. **Node.js EventEmitter**
Express.js and many npm packages use Observer pattern extensively.

### 6. **React/Vue**
State changes trigger component re-renders.

## Summary

- Use Observer Pattern for **decoupled event handling**
- Choose when subjects need to **notify multiple listeners**
- **Always unregister observers** to prevent memory leaks
- Keep observers **independent** of each other
- Prefer **event-based** approach in Python for simplicity
- Use **property-based** observation for fine-grained control
- Document **what notifications** subjects send
- Consider **alternative patterns** for simple scenarios
- Test observers **in isolation** from subject
- Watch for **notification order dependencies** antipattern
