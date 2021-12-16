# Last Modification Chip

**Author:** Vitoriox

Chip component for visualize the last modification date of the repository

```html
<last-modify-chip :value="date"/>
```

## Props

| Name               | Type   | Default | Description          |
|--------------------|--------|---------|----------------------|
| `value` *required* | `Date` | Null    | Date to be displayed |

## Computed Properties

| Name       | Type     | Dependencies | Description                                                                                               |
|------------|----------|--------------|-----------------------------------------------------------------------------------------------------------|
| `dateTime` | `Date`   | `value`      | Formatted `value` date to match the format [WWW, DD MMM YYYY hh:mm:ss]                                    |
| `color`    | `string` | `value`      | Defines de color of the border chip depending on the differences between the `value` and the current date |

