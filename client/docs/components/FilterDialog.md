# Filter Dialog

**Author:** Vitoriox

Dialog component that shows all the filter options for the metadata extracted.
Available filters are:
 - Technique: Technique used to obtain the data.

Hast two buttons with different behaviors:
 - Apply: Save selected filters, emit an `apply` event with the data.
 - Cancel: Emit a `cancel` event, do not save any filter selected.

```html
<filter-dialog
        :show-dialog="showDialog"
        @cancel="cancle()"
        @apply="apply()"
    />
```

## Props

| Name          | Type      | Default | Description                   |
|---------------|-----------|---------|-------------------------------|
| `show-dialog` | `Boolean` | False   | Flag to open/close the dialog |

## Data

| Name         | Type     | Initial value          | Description                                                                       |
|--------------|----------|------------------------|-----------------------------------------------------------------------------------|
| `techniques` | `Array`  | _TECHNIQUES_           | List of the current techniques available to be filtered                           |
| `prevFilter` | `Object` | {`techniquesIdx`: [] } | Previous state of the filter, It is only modified if the changes are applied      |
| `currFilter` | `Object` | {`techniquesIdx`: [] } | Current state of the filter, It is modified constantly during de filter selection |

## Events

| Name     | Payload      | Description                                 |
|----------|--------------|---------------------------------------------|
| `cancel` |              | Emitted when the button "Cancel" is pressed |
| `apply`  | `currFilter` | Emitted when the button "Apply" is pressed  |

## Methods

### cancel()

Emits `cancel` event and sets the `currFilter` value to the `prevFilter` value.

**Syntax**

```typescript
cancel(): void
```

### apply()

**Syntax**

Emits `apply` event with the filters selected and sets
the `prevFilter` value to the `currFilter` value.

```typescript
apply(): void
```
