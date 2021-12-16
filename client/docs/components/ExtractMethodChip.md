# Confidence Chip

**Author:** Vitoriox

Chip component for visualize the extraction method used.

```html
<extract-method-chip
        :value="method"
/>
```

## Props

| Name               | Type   | Default | Description                                              |
|--------------------|--------|---------|----------------------------------------------------------|
| `value` *required* | String | ''      | `idName` of the extraction method that must be displayed |

## Data

| Name               | Type  | Initial Value                    | Description                                                                 |
|--------------------|-------|----------------------------------|-----------------------------------------------------------------------------|
| `methodsItemsList` | Array | [`methodItem`,`methodItem`, ...] | List containing all the possible `methodItem` objects that can be displayed |

## Computed Properties

| Name         | Type     | Dependencies | Description                                                                                                                          |
|--------------|----------|--------------|--------------------------------------------------------------------------------------------------------------------------------------|
| `methodItem` | `Object` | `value`      | { `idName`: Identifiers name, `icon`: MDI icon to display, `color`: Color for the chip, `name`: Text to be displayed in the tooltip} |
