# Singleton

## Description

A creational design pattern that restricts the instantiation of a class to a single object and provides a global access point to that instance. The Singleton pattern is useful when you need exactly one instance of a class to coordinate actions across your system. This prevents multiple instances from conflicting with each other, particularly for shared resources like database connections, configuration managers, or logging systems.

**Key Characteristic**: The class controls its own instantiation and ensures no other instance can be created.

## When to Use

### Good Use Cases:
1. **Database Connection Pool** - Single shared connection to avoid resource exhaustion
2. **Configuration Manager** - One centralized configuration for the entire application
3. **Logger** - Single logging instance to ensure consistent output and avoid race conditions
4. **Thread Pool** - One thread pool managing all background tasks
5. **Cache Manager** - Centralized caching to ensure all parts of the app share the same cache

### When NOT to Use:
- **Testing difficulties** - Singletons make unit testing harder (hard to mock/replace)
- **Hidden dependencies** - Globals obscure the true dependencies of a class
- **Multithreading complexities** - Thread-safe singletons add complexity
- **Violates dependency injection** - Creates tight coupling to global state
- **Simple objects** - Don't complicate simple data holders with singleton pattern

## Pros and Cons

### Pros:
- ✅ **Controlled access** - Guaranteed single instance
- ✅ **Lazy initialization** - Instance created only when needed
- ✅ **Global access point** - Easy to access from anywhere
- ✅ **Resource efficiency** - Avoids multiple instances competing for resources

### Cons:
- ❌ **Testing challenges** - Hard to mock and test in isolation
- ❌ **Global state** - Hides dependencies and complicates debugging
- ❌ **Thread-safety issues** - Simple implementations aren't thread-safe
- ❌ **Scalability problems** - Single instance can become a bottleneck
- ❌ **Violates Single Responsibility** - Class responsible for both logic and instance control

## Implementation Approaches

### Approach 1: Basic Implementation (NOT Thread-Safe)
```python
class Singleton:
    """Basic singleton using __new__ - NOT recommended for multithreaded environments."""
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Usage
obj1 = Singleton()
obj2 = Singleton()
print(obj1 is obj2)  # True → Both refer to the same instance
```

**Issue**: If two threads call `__new__` simultaneously before `_instance` is set, multiple instances can be created.

### Approach 2: Thread-Safe Singleton (Recommended)
```python
import threading

class ThreadSafeSingleton:
    """Thread-safe singleton using a lock and double-checked locking pattern."""
    _instance = None
    _lock = threading.Lock()
    
    def __new__(cls, *args, **kwargs):
        # First check without lock (performance optimization)
        if not cls._instance:
            # Acquire lock before creating instance
            with cls._lock:
                # Double-check: another thread may have created it while waiting
                if not cls._instance:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

# Usage
obj1 = ThreadSafeSingleton()
obj2 = ThreadSafeSingleton()
print(obj1 is obj2)  # True → Thread-safe guarantee
```

**Advantage**: Even with multiple threads, only one instance is created.

### Approach 3: Decorator-Based (Pythonic & Clean)
```python
def singleton(cls):
    """Decorator that converts a class into a singleton."""
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class DatabaseConnection:
    def __init__(self):
        self.connection = "Connected to DB"

# Usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)  # True
```

**Advantage**: Simple, readable, separates concern from class logic.

### Approach 4: Module-Level Singleton (Simplest in Python)
```python
# database.py
class _DatabaseConnection:
    """Private class - only one instance created as module attribute."""
    def __init__(self):
        self.connection = "Connected to DB"

# Public singleton instance
db_connection = _DatabaseConnection()

# Usage in other files:
# from database import db_connection
# db_connection.connection
```

**Advantage**: Pure, leverages Python's module caching - simplest and most Pythonic.

## Common Pitfalls

### 1. **Thread-Safety Neglect**
Creating singletons without considering multithreading leads to multiple instances in concurrent environments.

### 2. **Difficulty in Testing**
Singletons are hard to mock/replace in unit tests since they control their own creation.

```python
# Problem: How do you test with a fake database?
class Singleton:
    _instance = None
    # ... implementation
```

### 3. **Hidden Dependencies**
Global state makes it unclear what a class actually depends on:
```python
# Bad: ConfigManager dependency is hidden
class UserService:
    def save_user(self, user):
        config = Singleton.get_instance()  # Hidden dependency!
        # ...
```

### 4. **Inheritance Issues**
Subclassing singletons can lead to multiple instances:
```python
class Singleton: ...

class SpecialSingleton(Singleton):
    pass

# Both classes will have separate instances - not what you want!
```

### 5. **Coupling to Global State**
Singletons introduce coupling to global state, making code less maintainable and flexible.

## Alternatives to Consider

| Alternative | When to Use | Pros | Cons |
|------------|-----------|------|------|
| **Dependency Injection** | Always first choice | Testable, loose coupling | Requires setup |
| **Module-level instance** | Python-specific | Simple, clean | Less explicit |
| **Factory Pattern** | Need controlled creation | Flexible, testable | More complex |
| **Service Locator** | Service management | Centralized access | Still hides dependencies |

## Summary

- Use singletons **sparingly** for truly global resources (DB connection, logger)
- Prefer **Dependency Injection** for most cases to keep code testable
- If using singletons, ensure **thread-safety** in multithreaded environments
- Consider **decorator or module-level** approach for simplicity in Python
- Be aware of testing and dependency visibility challenges
