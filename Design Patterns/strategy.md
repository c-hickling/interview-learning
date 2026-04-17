# Strategy Pattern

## Description

A behavioral design pattern that defines a family of algorithms, encapsulates each one, and makes them interchangeable. The Strategy pattern lets the algorithm vary independently from clients that use it. Instead of implementing a single algorithm directly, you define multiple strategies and allow the client to choose which one to use at runtime or based on context.

**Key Characteristic**: Encapsulates a set of behaviors in separate classes, making them interchangeable while keeping the code decoupled from specific implementations.

## When to Use

### Good Use Cases:
1. **Multiple Algorithms** - Different ways to perform the same task (sorting: QuickSort, MergeSort, HeapSort)
2. **Runtime Selection** - Choose algorithm based on data size, performance requirements, or user preference
3. **Conditional Logic Replacement** - Replace complex if/elif chains with strategy objects
4. **Payment Processing** - Different payment methods (CreditCard, PayPal, Bitcoin, etc.)
5. **Compression Algorithms** - Different compression strategies (ZIP, RAR, 7Z, GZIP)
6. **Sorting Strategies** - Different sorting based on data characteristics
7. **Validation Rules** - Different validation strategies for different data types

### When NOT to Use:
- **Single Algorithm** - Overkill if there's only one way to do something
- **Simple Choices** - If a single if/else is clearer than strategy objects
- **Performance Critical** - Polymorphic calls add minimal but measurable overhead
- **Rarely Changing** - If algorithms never change, direct implementation is simpler

## Pros and Cons

### Pros:
- ✅ **Eliminates Conditionals** - Replaces large if/elif/else blocks with polymorphism
- ✅ **Easy to Add Strategies** - New algorithms without modifying existing code
- ✅ **Runtime Selection** - Choose strategy at runtime based on conditions
- ✅ **Testability** - Each strategy can be tested in isolation
- ✅ **Open/Closed Principle** - Open for extension, closed for modification
- ✅ **Flexibility** - Switch strategies dynamically during execution
- ✅ **Code Organization** - Better code structure and maintainability

### Cons:
- ❌ **Complexity** - Introduces additional classes and indirection
- ❌ **Overkill for Simple Cases** - Multiple strategy classes for simple logic
- ❌ **More Objects** - Creates more instances in memory
- ❌ **Learning Curve** - Developers need to understand strategy selection logic
- ❌ **Indirection** - Extra method calls add minimal but measurable overhead

## Implementation Approaches

### Approach 1: Simple Strategy Pattern (Basic)
```python
from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    """Abstract base class defining the payment strategy interface."""
    
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

# Concrete Strategies
class CreditCardStrategy(PaymentStrategy):
    def __init__(self, card_number: str, cvv: str):
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount: float) -> bool:
        print(f"Processing ${amount} with Credit Card {self.card_number[-4:]}")
        return True

class PayPalStrategy(PaymentStrategy):
    def __init__(self, email: str):
        self.email = email
    
    def pay(self, amount: float) -> bool:
        print(f"Processing ${amount} via PayPal ({self.email})")
        return True

class CryptocurrencyStrategy(PaymentStrategy):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address
    
    def pay(self, amount: float) -> bool:
        print(f"Processing ${amount} to wallet {self.wallet_address}")
        return True

# Context
class ShoppingCart:
    """Uses a payment strategy to process payments."""
    
    def __init__(self):
        self.items = []
        self.strategy = None
    
    def add_item(self, item: str, price: float):
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.strategy = strategy
    
    def checkout(self) -> bool:
        if not self.strategy:
            raise ValueError("Payment strategy not set")
        
        total = sum(price for _, price in self.items)
        print(f"Total amount: ${total}")
        return self.strategy.pay(total)

# Usage
cart = ShoppingCart()
cart.add_item("Laptop", 999.99)
cart.add_item("Mouse", 29.99)

# Use credit card
cart.set_payment_strategy(CreditCardStrategy("1234-5678-9012-3456", "123"))
cart.checkout()

# Switch to PayPal
cart.set_payment_strategy(PayPalStrategy("user@example.com"))
cart.checkout()

# Switch to Cryptocurrency
cart.set_payment_strategy(CryptocurrencyStrategy("1A1z7agoat4WFjbXxS5kNtukiFjqWLkzQd"))
cart.checkout()
```

**Pros**: Simple, easy to understand, clear separation of concerns
**Cons**: Manual strategy selection, requires boilerplate

### Approach 2: Strategy with Factory (Automated Selection)
```python
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict, Type

class CompressionType(Enum):
    ZIP = "zip"
    RAR = "rar"
    GZIP = "gzip"
    BZIP2 = "bzip2"

# Strategy Interface
class CompressionStrategy(ABC):
    @abstractmethod
    def compress(self, data: bytes) -> bytes:
        pass
    
    @abstractmethod
    def decompress(self, data: bytes) -> bytes:
        pass

# Concrete Strategies
class ZipCompressionStrategy(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        print("Compressing with ZIP...")
        return b"ZIP_COMPRESSED_DATA"
    
    def decompress(self, data: bytes) -> bytes:
        print("Decompressing ZIP...")
        return b"DECOMPRESSED_DATA"

class GzipCompressionStrategy(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        print("Compressing with GZIP...")
        return b"GZIP_COMPRESSED_DATA"
    
    def decompress(self, data: bytes) -> bytes:
        print("Decompressing GZIP...")
        return b"DECOMPRESSED_DATA"

class RarCompressionStrategy(CompressionStrategy):
    def compress(self, data: bytes) -> bytes:
        print("Compressing with RAR...")
        return b"RAR_COMPRESSED_DATA"
    
    def decompress(self, data: bytes) -> bytes:
        print("Decompressing RAR...")
        return b"DECOMPRESSED_DATA"

# Strategy Factory
class CompressionFactory:
    _strategies: Dict[CompressionType, Type[CompressionStrategy]] = {
        CompressionType.ZIP: ZipCompressionStrategy,
        CompressionType.GZIP: GzipCompressionStrategy,
        CompressionType.RAR: RarCompressionStrategy,
    }
    
    @classmethod
    def create_strategy(cls, compression_type: CompressionType) -> CompressionStrategy:
        strategy_class = cls._strategies.get(compression_type)
        if not strategy_class:
            raise ValueError(f"Unknown compression type: {compression_type}")
        return strategy_class()

# Context
class FileCompressor:
    def __init__(self, compression_type: CompressionType):
        self.strategy = CompressionFactory.create_strategy(compression_type)
    
    def compress_file(self, data: bytes) -> bytes:
        return self.strategy.compress(data)
    
    def decompress_file(self, data: bytes) -> bytes:
        return self.strategy.decompress(data)
    
    def change_compression(self, compression_type: CompressionType):
        self.strategy = CompressionFactory.create_strategy(compression_type)

# Usage
data = b"This is sample data to compress"

compressor = FileCompressor(CompressionType.ZIP)
compressed = compressor.compress_file(data)
print(compressed)

# Switch strategy
compressor.change_compression(CompressionType.GZIP)
compressed = compressor.compress_file(data)
print(compressed)
```

**Pros**: Automated selection, clean separation, factory handles creation
**Cons**: Additional factory class, more setup

### Approach 3: Strategy with Configuration (Data-Driven)
```python
from abc import ABC, abstractmethod
from typing import Dict, Any

# Strategy Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: list) -> list:
        pass

# Concrete Strategies
class QuickSortStrategy(SortingStrategy):
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

class MergeSortStrategy(SortingStrategy):
    def _merge(self, left: list, right: list) -> list:
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]
    
    def sort(self, data: list) -> list:
        if len(data) <= 1:
            return data
        mid = len(data) // 2
        left = self.sort(data[:mid])
        right = self.sort(data[mid:])
        return self._merge(left, right)

class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: list) -> list:
        data = data.copy()
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return data

# Strategy Registry
class SortingStrategyRegistry:
    _strategies: Dict[str, SortingStrategy] = {}
    
    @classmethod
    def register(cls, name: str, strategy: SortingStrategy):
        cls._strategies[name] = strategy
    
    @classmethod
    def get_strategy(cls, name: str) -> SortingStrategy:
        if name not in cls._strategies:
            raise ValueError(f"Strategy not registered: {name}")
        return cls._strategies[name]

# Register strategies
SortingStrategyRegistry.register("quicksort", QuickSortStrategy())
SortingStrategyRegistry.register("mergesort", MergeSortStrategy())
SortingStrategyRegistry.register("bubblesort", BubbleSortStrategy())

# Context
class Sorter:
    def __init__(self, strategy_name: str):
        self.strategy = SortingStrategyRegistry.get_strategy(strategy_name)
    
    def sort(self, data: list) -> list:
        return self.strategy.sort(data)

# Usage
data = [64, 34, 25, 12, 22, 11, 60]

# Choose strategy based on data size
if len(data) > 10000:
    sorter = Sorter("mergesort")  # Best for large datasets
elif len(data) < 50:
    sorter = Sorter("quicksort")  # Good for small datasets
else:
    sorter = Sorter("bubblesort")

sorted_data = sorter.sort(data)
print(sorted_data)
```

**Pros**: Registry-based, flexible, easy to add strategies, data-driven
**Cons**: More setup, requires registration

### Approach 4: Strategy with Lambdas (Functional Approach)
```python
from typing import Callable, Dict

# Strategy as a dictionary of functions
class TextProcessor:
    """Uses function-based strategies for text processing."""
    
    # Strategy functions
    STRATEGIES: Dict[str, Callable[[str], str]] = {
        'uppercase': lambda text: text.upper(),
        'lowercase': lambda text: text.lower(),
        'capitalize': lambda text: text.capitalize(),
        'reverse': lambda text: text[::-1],
        'title': lambda text: text.title(),
    }
    
    def __init__(self, strategy_name: str):
        if strategy_name not in self.STRATEGIES:
            raise ValueError(f"Unknown strategy: {strategy_name}")
        self.strategy = self.STRATEGIES[strategy_name]
    
    def process(self, text: str) -> str:
        return self.strategy(text)
    
    def get_available_strategies(self) -> list:
        return list(self.STRATEGIES.keys())

# Usage
processor = TextProcessor('uppercase')
print(processor.process("hello world"))  # Output: HELLO WORLD

processor = TextProcessor('reverse')
print(processor.process("hello world"))  # Output: dlrow olleh

print(processor.get_available_strategies())
# Output: ['uppercase', 'lowercase', 'capitalize', 'reverse', 'title']
```

**Pros**: Minimal code, flexible, Pythonic for simple strategies
**Cons**: Limited for complex strategies, harder to test

## Common Pitfalls

### 1. **Over-Complicating Simple Logic**
Using Strategy pattern for trivial decisions adds unnecessary complexity.

```python
# Bad: Strategy for simple choice
class IfTrueStrategy: ...
class IfFalseStrategy: ...

# Better: Just use a conditional
if condition:
    do_something()
else:
    do_something_else()
```

### 2. **Tightly Coupled Strategy Selection**
Hardcoding strategy selection defeats the pattern's purpose.

```python
# Bad: Hardcoded selection in context
class PaymentProcessor:
    def process(self):
        if payment_type == 'credit':
            strategy = CreditCardStrategy()
        elif payment_type == 'paypal':
            # ... 10 more conditions

# Better: Externalize strategy selection
def process(self, strategy: PaymentStrategy):
    strategy.pay(amount)
```

### 3. **Strategies with Shared Mutable State**
Strategies sharing state can cause unexpected behavior.

```python
# Bad: Shared state
class Counter:
    count = 0  # Shared across all instances
    def increment(self): self.count += 1

# Better: Instance state
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self): self.count += 1
```

### 4. **Missing Strategy Interface Definition**
Unclear what methods strategies must implement.

```python
# Bad: No clear interface
class Strategy1:
    def process(self): pass

class Strategy2:
    def handle(self): pass  # Different name!

# Better: Define interface clearly
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool: pass
```

### 5. **Creating Strategy Instances Every Time**
Repeatedly instantiating strategies wastes resources for stateless strategies.

```python
# Bad: New instance every call
def process(self):
    strategy = SortingStrategy()
    return strategy.sort(data)

# Better: Reuse or cache
self.strategy = SortingStrategy()
return self.strategy.sort(data)
```

## Alternatives to Consider

| Alternative | When to Use | Pros | Cons |
|------------|-----------|------|------|
| **Conditional Logic** | Simple if/else | Clear, minimal code | Hard to extend |
| **Polymorphism** | Multiple types | Object-oriented | Requires inheritance |
| **Decorator Pattern** | Add behavior dynamically | Flexible, composable | More complex |
| **Template Method** | Variable steps in algorithm | Good for similar algorithms | Requires inheritance |
| **Command Pattern** | Encapsulate requests | More flexible than Strategy | More overhead |
| **State Pattern** | Object behavior changes by state | State-dependent behavior | Can be complex |

## Real-World Examples

### 1. **Payment Processing**
Different payment methods with different processing logic and validation.

### 2. **Sorting/Searching**
Different algorithms chosen based on data characteristics (size, distribution, etc.).

### 3. **Caching Strategies**
Different cache eviction policies (LRU, LFU, FIFO, Random).

### 4. **Authentication Methods**
Different authentication strategies (OAuth, JWT, Basic Auth, SAML).

### 5. **Data Export Formats**
Different export strategies (CSV, JSON, XML, PDF, Excel).

## Summary

- Use Strategy Pattern when you have **multiple similar algorithms**
- Choose Strategy when **runtime selection** of algorithm is needed
- Replace **complex if/elif chains** with strategy objects
- Define a **clear interface** that all strategies must implement
- Keep strategies **independent and stateless** when possible
- Consider **factory or registry pattern** for strategy selection
- Use **functional approach** (lambdas) for simple strategies
- Prefer **Dependency Injection** to pass strategies to context
- Don't over-engineer: use Strategy only when it provides **real value**
- Each strategy should be **testable in isolation**
