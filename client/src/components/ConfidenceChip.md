# Confidence Chip

**Author:** Vitoriox

Chip component for visualize percentage of confidence

```html
<confidence-chip
        :value="confidence"
        :threshold="threshold"
/>
```

## Props

| Name                   | Type     | Default | Description                                                |
|------------------------|----------|---------|------------------------------------------------------------|
| `value` *required*     | `Number` | 0       | Confidence value to be displayed. Must be between 0 and 1. |
| `threshold` *required* | `Number` | 0       | Threshold value that indicates de minimum confidence.      |


## Computed Properties

| Name              | Type     | Dependencies        | Description                                                                                      |
|-------------------|----------|---------------------|--------------------------------------------------------------------------------------------------|
| `color`           | `string` | `value` `threshold` | Defines de color of the chip depending on the diferences between the `value` and the `threshold` |
| `percentageValue` | `Number` | `value`             | Defines the percentage value showed on the chip depending of `value`                             |
