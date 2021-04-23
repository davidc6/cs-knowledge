# GRASP principles

GRASP stands for General Responsibility Assignment Software Principles. These essential OOP principles help us write maintainable, extensible and modular code.

## Information expert

- Determine how responsibilities should be delegated
- A class should be given the responsibility if it has the information it needs to fulfill it
- If data is not available then we cannot assign responsibility
- Benefits: low coupling, simplifies code, increases encapsulation, makes code more reusable

```typescript
class Item {
  private id: string
  private name: string
  private price: number

  construct({ id, name, price }) {
    this.id = id
    this.name = name
    this.price = price
  }

  toJSON() {
    return {
      id: this.id,
      name: this.name,
      price: this.price
    }
  }
}

// since CheckoutBasket is aware of items, it can calculate the total basket value
class CheckoutBasket {
  private items: Item[] = []

  addToBasket(item: Item) {
    this.items.push(item)
  }

  getTotal() {
    return items.reduce((acc: number, curVal: Item) => acc + curVal.price)
  }
}

```

## Creator

- This principle is aimed at figuring out which class should be responsible for creating a new instance if another class
- Class `Two` should create class `One` if (the more points it covers, the better):
  - `Two` closely uses `One`
  - `Two` records `One`
  - `Two` has initializing data for `One`
  - `Two` contains or aggregates `One`

In the example below, `CheckoutBasket` aggregates `Discount` since `Discount` cannot exist without the `CheckoutBasket`. It also closely uses `Discount` and has data for `Discount`.

```typescript
class CheckoutBasket {
  private items: Item[] = []
  private total: number = 0
  private discount: Discount | null = null
  
  addToBasket(item: Item) {
    this.items.push(item)
  }

  applyDiscount(code: string) {
    const discount = new Discount(code)
    
    if (!discount.isValid()) {
      throw new Error('Sorry, this discount code is not valid')
    }
    
    this.discount = discount
  }

  getTotal() {
    const priceBeforeDiscount = items.reduce((acc: number, curVal: Item) => acc + curVal.price)

    if (this.discount === null) {
      return priceBeforeDiscount
    }
    
    return this.discount.applyTo(priceBeforeDiscount)
  }
}
```


## Controller

Todo

## Indirection

Todo

## Low coupling

- Coupling is a how one component is related to another
- Low coupling is achieved by assigning responsibilities so that unnecessary coupling is low
- High coupling means that components are very dependent on each other
- If objects are independent and isolated then we can change them without worrying that would break something
- SOLID principles are a great way to keep coupling low

## High cohesion

- High cohesion classes are focused, understandable, manageable
- If parts inside of a class are not related such class is low cohesion class
- If a class has many responsibilities then its cohesion drops since it has to deal with many things

## Polymorphism

Todo

## Protected variations

Todo

## Pure fabrication

