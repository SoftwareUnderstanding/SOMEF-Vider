# checkbox

**Author:** Vitoriox

A simple checkbox component

```html
<checkbox v-model="value"/>
```

## Slots

| Name      | Description                             |
|-----------|-----------------------------------------|
| `default` |                                         |
| `label`   | Use this slot to set the checkbox label |

## Props

| Name               | Type    | Default | Description        |
|--------------------|---------|---------|--------------------|
| `model` *required* | `Array` |         | The checkbox model |


## Data

| Name           | Type     | Initial value | Description                                                                        |
|----------------|----------|---------------|------------------------------------------------------------------------------------|
| `initialValue` | `string` | `""`          | The initial component value. Used to detect changes and restore the initial value. |
| `currentValue` | `string` | `""`          |                                                                                    |

## Computed Properties

| Name              | Type     | Dependencies        | Description                                                                                      |
|-------------------|----------|---------------------|--------------------------------------------------------------------------------------------------|
| `color`           | `string` | `value` `threshold` | Defines de color of the chip depending on the diferences between the `value` and the `threshold` |
| `percentageValue` | `Number` | `value`             | Defines the percentage value showed on the chip depending of `value`                             |
## Events

| Name      | Payload | Description                                                                                            |
|-----------|---------|--------------------------------------------------------------------------------------------------------|
| `loaded`  |         | Emitted when the component has been loaded                                                             |
| `enabled` |         | Emitted the event `enabled` when loaded Multilign<br/>**Arguments**<br/><ul><li>**`x: any`**</li></ul> |

## Methods

### check()

Check if the input is checked

**Syntax**

```typescript
check(): void
```

### prop()

**Syntax**

```typescript
prop(): void
```

### dynamic()

Make component dynamic

**Syntax**

```typescript
dynamic(): void
```

### dynamicMode()

Enter to dynamic mode

**Syntax**

```typescript
dynamicMode(): void
```

### enable()

Enable the checkbox

**Syntax**

```typescript
enable(value: unknow): void
```
